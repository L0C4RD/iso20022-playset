from . import base_types
from ._OrganisationIdentification15Choice import OrganisationIdentification15Choice
from ._PartyIdentification236Choice import PartyIdentification236Choice
from ._SettlementParties34Choice import SettlementParties34Choice

class TransactionCounterpartyData11(base_types._BaseFieldType):

	__slots__ = ["_AgtLndr", "_Bnfcry", "_Brkr", "_ClrMmb", "_SttlmPties", "_TrptyAgt"]
	@property
	def AgtLndr(self):
		return self._AgtLndr

	@AgtLndr.setter
	def AgtLndr(self, value):
		self._AgtLndr = value if type(value) != base_types.auto else self.make_default("AgtLndr")

	@AgtLndr.deleter
	def AgtLndr(self):
		del self._AgtLndr
		self._AgtLndr = None

	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if type(value) != base_types.auto else self.make_default("Bnfcry")

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = None

	@property
	def Brkr(self):
		return self._Brkr

	@Brkr.setter
	def Brkr(self, value):
		self._Brkr = value if type(value) != base_types.auto else self.make_default("Brkr")

	@Brkr.deleter
	def Brkr(self):
		del self._Brkr
		self._Brkr = None

	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if type(value) != base_types.auto else self.make_default("ClrMmb")

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = None

	@property
	def SttlmPties(self):
		return self._SttlmPties

	@SttlmPties.setter
	def SttlmPties(self, value):
		self._SttlmPties = value if type(value) != base_types.auto else self.make_default("SttlmPties")

	@SttlmPties.deleter
	def SttlmPties(self):
		del self._SttlmPties
		self._SttlmPties = None

	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if type(value) != base_types.auto else self.make_default("TrptyAgt")

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtLndr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bnfcry', type=PartyIdentification236Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brkr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmb', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPties', type=SettlementParties34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
	))

