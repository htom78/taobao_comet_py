'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class HotelNameGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.city = None
		self.country = None
		self.district = None
		self.domestic = None
		self.name = None
		self.province = None

	def getapiname(self):
		return 'taobao.hotel.name.get'
