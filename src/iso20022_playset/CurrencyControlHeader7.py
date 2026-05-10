import base_types
import BranchAndFinancialInstitutionIdentification8
import Max35Text
import PartyIdentification272
import Max15NumericText
import ISODateTime

class CurrencyControlHeader7(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_RegnAgt", "_MsgId", "_RcvgPty", "_NbOfItms"]
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

	@property
	def RegnAgt(self):
		return self._RegnAgt

	@RegnAgt.setter
	def RegnAgt(self, value):
		self._RegnAgt = value if type(value) != auto else self.make_default("RegnAgt")

	@RegnAgt.deleter
	def RegnAgt(self):
		del self._RegnAgt
		self._RegnAgt = None

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
	def RcvgPty(self):
		return self._RcvgPty

	@RcvgPty.setter
	def RcvgPty(self, value):
		self._RcvgPty = value if type(value) != auto else self.make_default("RcvgPty")

	@RcvgPty.deleter
	def RcvgPty(self):
		del self._RcvgPty
		self._RcvgPty = None

	@property
	def NbOfItms(self):
		return self._NbOfItms

	@NbOfItms.setter
	def NbOfItms(self, value):
		self._NbOfItms = value if type(value) != auto else self.make_default("NbOfItms")

	@NbOfItms.deleter
	def NbOfItms(self):
		del self._NbOfItms
		self._NbOfItms = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgPty', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfItms', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
	))

