'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class WangwangEserviceChatpeersGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.charset = None
		self.chat_id = None
		self.end_date = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.wangwang.eservice.chatpeers.get'
