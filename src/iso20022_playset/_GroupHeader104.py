from . import base_types
from .Max35Text import Max35Text
from .SettlementInstruction14 import SettlementInstruction14
from .ISODateTime import ISODateTime
from .DecimalNumber import DecimalNumber
from .Max15NumericText import Max15NumericText

class GroupHeader104(base_types._BaseFieldType):

	__slots__ = ["_CtrlSum", "_CreDtTm", "_MsgId", "_SttlmInf", "_NbOfSttlmReqs"]
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
	def SttlmInf(self):
		return self._SttlmInf

	@SttlmInf.setter
	def SttlmInf(self, value):
		self._SttlmInf = value if type(value) != base_types.auto else self.make_default("SttlmInf")

	@SttlmInf.deleter
	def SttlmInf(self):
		del self._SttlmInf
		self._SttlmInf = None

	@property
	def NbOfSttlmReqs(self):
		return self._NbOfSttlmReqs

	@NbOfSttlmReqs.setter
	def NbOfSttlmReqs(self, value):
		self._NbOfSttlmReqs = value if type(value) != base_types.auto else self.make_default("NbOfSttlmReqs")

	@NbOfSttlmReqs.deleter
	def NbOfSttlmReqs(self):
		del self._NbOfSttlmReqs
		self._NbOfSttlmReqs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInf', type=SettlementInstruction14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfSttlmReqs', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))

