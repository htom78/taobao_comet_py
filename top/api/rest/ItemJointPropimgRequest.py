'''
Created by auto_sdk on 2013-06-16 16:36:02
'''
from top.api.base import RestApi
class ItemJointPropimgRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.id = None
		self.num_iid = None
		self.pic_path = None
		self.position = None
		self.properties = None

	def getapiname(self):
		return 'taobao.item.joint.propimg'
