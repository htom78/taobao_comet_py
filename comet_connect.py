#encoding:utf-8
'''
Created on 2013年8月22日

@author: ganlv
'''
from datetime import datetime
import daemon
import json
import logging
import pika
import requests
import sys
import time
import top.api



#这个链接也断开的问题


def main_program():
    APP_KEY=''
    APP_SECRET=''
    EXCHNAGE='CRM.TOP.NOTIFY.EXCHANGE'
    ROUTE_KEY="CRM.TOP.NOTIFY.ALL"
    
    logging.basicConfig(filename='/data/logs/comet_log.log', level=logging.WARN, 
                                        format="%(asctime)s %(module)s.%(funcName)s Line:%(lineno)d - %(message)s",
                                        datefmt="%Y-%m-%d %H-%M-%S")
    logging.addLevelName("WARN", "pika.adapters.base_connection")
    log = logging.getLogger('root') 
    
    def connet_taobao_stream():
        params={}
        timestamp =datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
        params['timestamp']=timestamp
        params['app_key'] = APP_KEY
        sign = top.api.base.sign(APP_SECRET, params);
        params['sign']=sign
        response = requests.post("http://stream.api.taobao.com/stream",params,stream=True)
        return response
    
    def main_handle():
        log.warn("main")
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))
            channel = connection.channel()
            properties =pika.spec.BasicProperties(content_type='text',content_encoding='UTF-8')
            
            #设置pika
            response =  connet_taobao_stream();
            lines = response.iter_lines()
            while True:
                try:
                    message = lines.next()
                    json_result = json.loads(message)
                    json_result = json_result['packet']
                    code =  json_result['code']
                    if code == 200:#确认连接
                        log.warn("Start Connect")
                    elif code == 201:#心跳检测
                        log.warn("Heart Beat")
                    elif code == 202:#推送消息
                        message_json = json_result['msg']
                        comet_message = json.dumps(message_json)
                        try:
                            channel.basic_publish(exchange=EXCHNAGE,routing_key=ROUTE_KEY,body=comet_message,properties=properties)
                        except Exception,e:#断开重连
                            log.error("disconnect rabbit mq,reconnect:%s",e);
                            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))
                            channel = connection.channel()
                    elif code ==203:#重发消息
                        log.warn("resend message:%s"%message);
                    elif code == 101:#客户端连接断开
                        log.error("close by client")
                        break;
                    elif code == 102:#服务端连接诶断开,有启动时间可以用message来控制重新启动
                        need_sleep_seconds = json_result['msg']
                        time.sleep(need_sleep_seconds)
                        main_handle()
                        break;
                    elif code == 103:#服务端连接断开，休息一点时间之后就可以重新连接了
                        time.sleep(3)
                        main_handle()
                        break;
                    elif code == 104:#重复连接断开
                        log.error("closed by repeat connet")
                        sys.exit() #need重连
                        break;
                    elif code==105:#断开连接，服务端信息大量积压导致出问题，连接断开
                        log.error("closed by too more message")
                        sys.exit()#need重连
                        break;
                except Exception,e:
                    log.error("%s"%e)
                    time.sleep(2);
        except Exception,e:
            connection.close()
            log.exception("ERROR,%s",e)
            sys.exit()
    main_handle()

if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[ 1]=='-d':
        print "Damon"
        with daemon.DaemonContext():
            main_program()
    else:
        main_program()
        
