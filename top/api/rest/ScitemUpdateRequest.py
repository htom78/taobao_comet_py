'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class ScitemUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.bar_code = None
		self.brand_id = None
		self.brand_name = None
		self.height = None
		self.is_area_sale = None
		self.is_costly = None
		self.is_dangerous = None
		self.is_friable = None
		self.is_warranty = None
		self.item_id = None
		self.item_name = None
		self.item_type = None
		self.length = None
		self.matter_status = None
		self.outer_code = None
		self.price = None
		self.remark = None
		self.remove_properties = None
		self.spu_id = None
		self.update_properties = None
		self.volume = None
		self.weight = None
		self.width = None
		self.wms_code = None

	def getapiname(self):
		return 'taobao.scitem.update'
