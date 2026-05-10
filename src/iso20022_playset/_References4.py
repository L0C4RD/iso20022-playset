from . import base_types
from ._Max70Text import Max70Text
from ._MessageIdentification1 import MessageIdentification1

class References4(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_PrcId", "_AttchdDocNm"]
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
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AttchdDocNm', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
	))

