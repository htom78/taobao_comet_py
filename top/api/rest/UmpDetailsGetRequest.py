'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class UmpDetailsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.act_id = None
		self.page_no = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.ump.details.get'
