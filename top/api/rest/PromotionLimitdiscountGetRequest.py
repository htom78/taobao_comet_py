'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class PromotionLimitdiscountGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.limit_discount_id = None
		self.page_number = None
		self.start_time = None
		self.status = None

	def getapiname(self):
		return 'taobao.promotion.limitdiscount.get'
