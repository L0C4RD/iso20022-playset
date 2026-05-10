from . import base_types
from .Max70Text import Max70Text
from .MessageIdentification1 import MessageIdentification1
from .Max35Text import Max35Text

class References3(base_types._BaseFieldType):

	__slots__ = ["_PrcId", "_MsgId", "_ReqToBeCmpltdId", "_ReqRsn", "_AttchdDocNm"]
	@property
	def PrcId(self):
		return self._PrcId

	@PrcId.setter
	def PrcId(self, value):
		self._PrcId = value if type(value) != base_types.auto else self.make_default("PrcId")

	@PrcId.deleter
	def PrcId(self):
		del self._PrcId
		self._PrcId = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def ReqToBeCmpltdId(self):
		return self._ReqToBeCmpltdId

	@ReqToBeCmpltdId.setter
	def ReqToBeCmpltdId(self, value):
		self._ReqToBeCmpltdId = value if type(value) != base_types.auto else self.make_default("ReqToBeCmpltdId")

	@ReqToBeCmpltdId.deleter
	def ReqToBeCmpltdId(self):
		del self._ReqToBeCmpltdId
		self._ReqToBeCmpltdId = None

	@property
	def ReqRsn(self):
		return self._ReqRsn

	@ReqRsn.setter
	def ReqRsn(self, value):
		self._ReqRsn = value if type(value) != base_types.auto else self.make_default("ReqRsn")

	@ReqRsn.deleter
	def ReqRsn(self):
		del self._ReqRsn
		self._ReqRsn = None

	@property
	def AttchdDocNm(self):
		return self._AttchdDocNm

	@AttchdDocNm.setter
	def AttchdDocNm(self, value):
		self._AttchdDocNm = value if type(value) != base_types.auto else self.make_default("AttchdDocNm")

	@AttchdDocNm.deleter
	def AttchdDocNm(self):
		del self._AttchdDocNm
		self._AttchdDocNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqToBeCmpltdId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqRsn', type=Max35Text, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AttchdDocNm', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
	))

