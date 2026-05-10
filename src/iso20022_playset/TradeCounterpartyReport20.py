from . import base_types
from .TradeCounterpartyRelationshipRecord1 import TradeCounterpartyRelationshipRecord1
from .PartyIdentification248Choice import PartyIdentification248Choice
from .OrganisationIdentification15Choice import OrganisationIdentification15Choice
from .Counterparty45 import Counterparty45
from .Counterparty46 import Counterparty46

class TradeCounterpartyReport20(base_types._BaseFieldType):

	__slots__ = ["_SubmitgAgt", "_Brkr", "_NttyRspnsblForRpt", "_RptgCtrPty", "_Bnfcry", "_OthrCtrPty", "_ExctnAgt", "_ClrMmb", "_RltshRcrd"]
	@property
	def SubmitgAgt(self):
		return self._SubmitgAgt

	@SubmitgAgt.setter
	def SubmitgAgt(self, value):
		self._SubmitgAgt = value if type(value) != auto else self.make_default("SubmitgAgt")

	@SubmitgAgt.deleter
	def SubmitgAgt(self):
		del self._SubmitgAgt
		self._SubmitgAgt = None

	@property
	def Brkr(self):
		return self._Brkr

	@Brkr.setter
	def Brkr(self, value):
		self._Brkr = value if type(value) != auto else self.make_default("Brkr")

	@Brkr.deleter
	def Brkr(self):
		del self._Brkr
		self._Brkr = None

	@property
	def NttyRspnsblForRpt(self):
		return self._NttyRspnsblForRpt

	@NttyRspnsblForRpt.setter
	def NttyRspnsblForRpt(self, value):
		self._NttyRspnsblForRpt = value if type(value) != auto else self.make_default("NttyRspnsblForRpt")

	@NttyRspnsblForRpt.deleter
	def NttyRspnsblForRpt(self):
		del self._NttyRspnsblForRpt
		self._NttyRspnsblForRpt = None

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if type(value) != auto else self.make_default("RptgCtrPty")

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = None

	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if type(value) != auto else self.make_default("Bnfcry")

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = None

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if type(value) != auto else self.make_default("OthrCtrPty")

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = None

	@property
	def ExctnAgt(self):
		return self._ExctnAgt

	@ExctnAgt.setter
	def ExctnAgt(self, value):
		self._ExctnAgt = value if type(value) != auto else self.make_default("ExctnAgt")

	@ExctnAgt.deleter
	def ExctnAgt(self):
		del self._ExctnAgt
		self._ExctnAgt = None

	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if type(value) != auto else self.make_default("ClrMmb")

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = None

	@property
	def RltshRcrd(self):
		return self._RltshRcrd

	@RltshRcrd.setter
	def RltshRcrd(self, value):
		self._RltshRcrd = value if type(value) != auto else self.make_default("RltshRcrd")

	@RltshRcrd.deleter
	def RltshRcrd(self):
		del self._RltshRcrd
		self._RltshRcrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubmitgAgt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brkr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyRspnsblForRpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=Counterparty45, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bnfcry', type=PartyIdentification248Choice, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrCtrPty', type=Counterparty46, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnAgt', type=OrganisationIdentification15Choice, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification248Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltshRcrd', type=TradeCounterpartyRelationshipRecord1, min=0, max=None, mutex_group=None, array=True),
	))

