from . import base_types
from .ISODateTime import ISODateTime
from .Max15NumericText import Max15NumericText
from .PartyIdentification272 import PartyIdentification272
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .Max35Text import Max35Text

class CurrencyControlHeader8(base_types._BaseFieldType):

	__slots__ = ["_NbOfItms", "_MsgId", "_FwdgAgt", "_CreDtTm", "_InitgPty"]
	@property
	def NbOfItms(self):
		return self._NbOfItms

	@NbOfItms.setter
	def NbOfItms(self, value):
		self._NbOfItms = value if type(value) != base_types.auto else self.make_default("NbOfItms")

	@NbOfItms.deleter
	def NbOfItms(self):
		del self._NbOfItms
		self._NbOfItms = None

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
	def FwdgAgt(self):
		return self._FwdgAgt

	@FwdgAgt.setter
	def FwdgAgt(self, value):
		self._FwdgAgt = value if type(value) != base_types.auto else self.make_default("FwdgAgt")

	@FwdgAgt.deleter
	def FwdgAgt(self):
		del self._FwdgAgt
		self._FwdgAgt = None

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
	def InitgPty(self):
		return self._InitgPty

	@InitgPty.setter
	def InitgPty(self, value):
		self._InitgPty = value if type(value) != base_types.auto else self.make_default("InitgPty")

	@InitgPty.deleter
	def InitgPty(self):
		del self._InitgPty
		self._InitgPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfItms', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwdgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitgPty', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
	))

