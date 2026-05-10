from . import base_types
import OriginalBusinessQuery1
import RequestType4Choice
import Max35Text
import ISODateTime

class MessageHeader11(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_ReqTp", "_OrgnlBizQry", "_CreDtTm"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def ReqTp(self):
		return self._ReqTp

	@ReqTp.setter
	def ReqTp(self, value):
		self._ReqTp = value if type(value) != auto else self.make_default("ReqTp")

	@ReqTp.deleter
	def ReqTp(self):
		del self._ReqTp
		self._ReqTp = None

	@property
	def OrgnlBizQry(self):
		return self._OrgnlBizQry

	@OrgnlBizQry.setter
	def OrgnlBizQry(self, value):
		self._OrgnlBizQry = value if type(value) != auto else self.make_default("OrgnlBizQry")

	@OrgnlBizQry.deleter
	def OrgnlBizQry(self):
		del self._OrgnlBizQry
		self._OrgnlBizQry = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqTp', type=RequestType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBizQry', type=OriginalBusinessQuery1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

