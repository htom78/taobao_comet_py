'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class TaobaokeWidgetShopsConvertRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.is_mobile = None
		self.outer_code = None
		self.seller_nicks = None

	def getapiname(self):
		return 'taobao.taobaoke.widget.shops.convert'
