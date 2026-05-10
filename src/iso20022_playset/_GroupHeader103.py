from . import base_types
from ._Max35Text import Max35Text
from ._Max15NumericText import Max15NumericText
from ._DecimalNumber import DecimalNumber
from ._ISODateTime import ISODateTime

class GroupHeader103(base_types._BaseFieldType):

	__slots__ = ["_NbOfChqs", "_CreDtTm", "_MsgId", "_CtrlSum"]
	@property
	def NbOfChqs(self):
		return self._NbOfChqs

	@NbOfChqs.setter
	def NbOfChqs(self, value):
		self._NbOfChqs = value if type(value) != base_types.auto else self.make_default("NbOfChqs")

	@NbOfChqs.deleter
	def NbOfChqs(self):
		del self._NbOfChqs
		self._NbOfChqs = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

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
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if type(value) != base_types.auto else self.make_default("CtrlSum")

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfChqs', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

