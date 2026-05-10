from . import base_types
from .PartyAddress1 import PartyAddress1
from .PartyIdentification203Choice import PartyIdentification203Choice
from .Max350Text import Max350Text

class PartyIdentification214(base_types._BaseFieldType):

	__slots__ = ["_RspnRcptAdr", "_Id", "_RcptNm"]
	@property
	def RspnRcptAdr(self):
		return self._RspnRcptAdr

	@RspnRcptAdr.setter
	def RspnRcptAdr(self, value):
		self._RspnRcptAdr = value if type(value) != base_types.auto else self.make_default("RspnRcptAdr")

	@RspnRcptAdr.deleter
	def RspnRcptAdr(self):
		del self._RspnRcptAdr
		self._RspnRcptAdr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def RcptNm(self):
		return self._RcptNm

	@RcptNm.setter
	def RcptNm(self, value):
		self._RcptNm = value if type(value) != base_types.auto else self.make_default("RcptNm")

	@RcptNm.deleter
	def RcptNm(self):
		del self._RcptNm
		self._RcptNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspnRcptAdr', type=PartyAddress1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification203Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcptNm', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))

