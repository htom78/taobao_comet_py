'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class FenxiaoCooperationUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.distributor_id = None
		self.grade_id = None
		self.trade_type = None

	def getapiname(self):
		return 'taobao.fenxiao.cooperation.update'
