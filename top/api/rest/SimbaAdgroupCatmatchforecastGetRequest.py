'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class SimbaAdgroupCatmatchforecastGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adgroup_id = None
		self.catmatch_price = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.adgroup.catmatchforecast.get'
