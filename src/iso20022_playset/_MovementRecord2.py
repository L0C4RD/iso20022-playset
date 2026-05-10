from . import base_types
from ._Number import Number
from ._AmountAndDirection5 import AmountAndDirection5
from ._PartyIdentification272 import PartyIdentification272
from ._Max35Text import Max35Text
from ._CashAccount40 import CashAccount40

class MovementRecord2(base_types._BaseFieldType):

	__slots__ = ["_SttlmAgtAcct", "_PtcptAcct", "_Ptcpt", "_Ref", "_Id", "_SeqNb", "_SttlmAgt", "_Amt"]
	@property
	def SttlmAgtAcct(self):
		return self._SttlmAgtAcct

	@SttlmAgtAcct.setter
	def SttlmAgtAcct(self, value):
		self._SttlmAgtAcct = value if type(value) != base_types.auto else self.make_default("SttlmAgtAcct")

	@SttlmAgtAcct.deleter
	def SttlmAgtAcct(self):
		del self._SttlmAgtAcct
		self._SttlmAgtAcct = None

	@property
	def PtcptAcct(self):
		return self._PtcptAcct

	@PtcptAcct.setter
	def PtcptAcct(self, value):
		self._PtcptAcct = value if type(value) != base_types.auto else self.make_default("PtcptAcct")

	@PtcptAcct.deleter
	def PtcptAcct(self):
		del self._PtcptAcct
		self._PtcptAcct = None

	@property
	def Ptcpt(self):
		return self._Ptcpt

	@Ptcpt.setter
	def Ptcpt(self, value):
		self._Ptcpt = value if type(value) != base_types.auto else self.make_default("Ptcpt")

	@Ptcpt.deleter
	def Ptcpt(self):
		del self._Ptcpt
		self._Ptcpt = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

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
	def SeqNb(self):
		return self._SeqNb

	@SeqNb.setter
	def SeqNb(self, value):
		self._SeqNb = value if type(value) != base_types.auto else self.make_default("SeqNb")

	@SeqNb.deleter
	def SeqNb(self):
		del self._SeqNb
		self._SeqNb = None

	@property
	def SttlmAgt(self):
		return self._SttlmAgt

	@SttlmAgt.setter
	def SttlmAgt(self, value):
		self._SttlmAgt = value if type(value) != base_types.auto else self.make_default("SttlmAgt")

	@SttlmAgt.deleter
	def SttlmAgt(self):
		del self._SttlmAgt
		self._SttlmAgt = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SttlmAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtcptAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ptcpt', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAgt', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=AmountAndDirection5, min=1, max=1, mutex_group=None, array=False),
	))

