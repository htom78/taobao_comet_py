'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class AlipayMicropayOrderFreezepayurlGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.alipay_order_no = None
		self.auth_token = None

	def getapiname(self):
		return 'alipay.micropay.order.freezepayurl.get'
