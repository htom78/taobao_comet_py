'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class TripJipiaoAgentOrderFindRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.begin_time = None
		self.end_time = None
		self.page = None
		self.policy_id = None

	def getapiname(self):
		return 'taobao.trip.jipiao.agent.order.find'
