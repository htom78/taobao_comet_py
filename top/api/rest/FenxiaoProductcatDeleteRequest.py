'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class FenxiaoProductcatDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.product_line_id = None

	def getapiname(self):
		return 'taobao.fenxiao.productcat.delete'
