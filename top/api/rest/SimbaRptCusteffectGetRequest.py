'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class SimbaRptCusteffectGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.nick = None
		self.page_no = None
		self.page_size = None
		self.source = None
		self.start_time = None
		self.subway_token = None

	def getapiname(self):
		return 'taobao.simba.rpt.custeffect.get'
