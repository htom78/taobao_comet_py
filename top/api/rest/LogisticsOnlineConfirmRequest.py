'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class LogisticsOnlineConfirmRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.is_split = None
		self.out_sid = None
		self.seller_ip = None
		self.sub_tid = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.online.confirm'
