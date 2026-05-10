from . import base_types
import PartyIdentification242Choice

class SettlementParties120(base_types._BaseFieldType):

	__slots__ = ["_BnfcryInstn", "_Intrmy", "_RcvgAgt", "_DlvryAgt"]
	@property
	def BnfcryInstn(self):
		return self._BnfcryInstn

	@BnfcryInstn.setter
	def BnfcryInstn(self, value):
		self._BnfcryInstn = value if type(value) != auto else self.make_default("BnfcryInstn")

	@BnfcryInstn.deleter
	def BnfcryInstn(self):
		del self._BnfcryInstn
		self._BnfcryInstn = None

	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if type(value) != auto else self.make_default("Intrmy")

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = None

	@property
	def RcvgAgt(self):
		return self._RcvgAgt

	@RcvgAgt.setter
	def RcvgAgt(self, value):
		self._RcvgAgt = value if type(value) != auto else self.make_default("RcvgAgt")

	@RcvgAgt.deleter
	def RcvgAgt(self):
		del self._RcvgAgt
		self._RcvgAgt = None

	@property
	def DlvryAgt(self):
		return self._DlvryAgt

	@DlvryAgt.setter
	def DlvryAgt(self, value):
		self._DlvryAgt = value if type(value) != auto else self.make_default("DlvryAgt")

	@DlvryAgt.deleter
	def DlvryAgt(self):
		del self._DlvryAgt
		self._DlvryAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BnfcryInstn', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmy', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgAgt', type=PartyIdentification242Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAgt', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
	))

