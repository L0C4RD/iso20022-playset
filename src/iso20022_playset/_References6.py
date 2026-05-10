from . import base_types
from ._Max350Text import Max350Text
from ._Max70Text import Max70Text
from ._MessageIdentification1 import MessageIdentification1
from ._UseCases1Code import UseCases1Code

class References6(base_types._BaseFieldType):

	__slots__ = ["_AttchdDocNm", "_MsgId", "_PrcId", "_RjctdReqId", "_RjctdReqTp", "_RjctnRsn"]
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
	def RjctdReqId(self):
		return self._RjctdReqId

	@RjctdReqId.setter
	def RjctdReqId(self, value):
		self._RjctdReqId = value if type(value) != base_types.auto else self.make_default("RjctdReqId")

	@RjctdReqId.deleter
	def RjctdReqId(self):
		del self._RjctdReqId
		self._RjctdReqId = None

	@property
	def RjctdReqTp(self):
		return self._RjctdReqTp

	@RjctdReqTp.setter
	def RjctdReqTp(self, value):
		self._RjctdReqTp = value if type(value) != base_types.auto else self.make_default("RjctdReqTp")

	@RjctdReqTp.deleter
	def RjctdReqTp(self):
		del self._RjctdReqTp
		self._RjctdReqTp = None

	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if type(value) != base_types.auto else self.make_default("RjctnRsn")

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchdDocNm', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdReqTp', type=UseCases1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=Max350Text, min=1, max=None, mutex_group=None, array=True),
	))

