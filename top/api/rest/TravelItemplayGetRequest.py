'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class TravelItemplayGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cid = None
		self.dest_codes = None
		self.play_type = None

	def getapiname(self):
		return 'taobao.travel.itemplay.get'
