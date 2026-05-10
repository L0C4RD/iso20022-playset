from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._AccountIdentification4Choice import AccountIdentification4Choice
from ._PartyIdentificationAndAccount31 import PartyIdentificationAndAccount31

class Contribution1(base_types._BaseFieldType):

	__slots__ = ["_IncrCvrgAmt", "_Acct", "_ReqrdAmt", "_NonClrMmb"]
	@property
	def IncrCvrgAmt(self):
		return self._IncrCvrgAmt

	@IncrCvrgAmt.setter
	def IncrCvrgAmt(self, value):
		self._IncrCvrgAmt = value if type(value) != base_types.auto else self.make_default("IncrCvrgAmt")

	@IncrCvrgAmt.deleter
	def IncrCvrgAmt(self):
		del self._IncrCvrgAmt
		self._IncrCvrgAmt = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def ReqrdAmt(self):
		return self._ReqrdAmt

	@ReqrdAmt.setter
	def ReqrdAmt(self, value):
		self._ReqrdAmt = value if type(value) != base_types.auto else self.make_default("ReqrdAmt")

	@ReqrdAmt.deleter
	def ReqrdAmt(self):
		del self._ReqrdAmt
		self._ReqrdAmt = None

	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if type(value) != base_types.auto else self.make_default("NonClrMmb")

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncrCvrgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqrdAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount31, min=0, max=1, mutex_group=None, array=False),
	))

