'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class TradeFullinfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.fullinfo.get'
