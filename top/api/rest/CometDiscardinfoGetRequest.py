'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class CometDiscardinfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end = None
		self.nick = None
		self.start = None
		self.types = None
		self.user_id = None

	def getapiname(self):
		return 'taobao.comet.discardinfo.get'
