from . import base_types
from ._TradePartyIdentificationQuery11Choice import TradePartyIdentificationQuery11Choice
from ._Operation3Code import Operation3Code
from ._TradePartyIdentificationQuery10Choice import TradePartyIdentificationQuery10Choice

class TradePartyQueryCriteria7(base_types._BaseFieldType):

	__slots__ = ["_NttyRspnsblForRpt", "_SubmitgAgt", "_Oprtr", "_Brkr", "_Bnfcry", "_OthrCtrPty", "_RptgCtrPty", "_CCP", "_ClrMmb"]
	@property
	def NttyRspnsblForRpt(self):
		return self._NttyRspnsblForRpt

	@NttyRspnsblForRpt.setter
	def NttyRspnsblForRpt(self, value):
		self._NttyRspnsblForRpt = value if type(value) != base_types.auto else self.make_default("NttyRspnsblForRpt")

	@NttyRspnsblForRpt.deleter
	def NttyRspnsblForRpt(self):
		del self._NttyRspnsblForRpt
		self._NttyRspnsblForRpt = None

	@property
	def SubmitgAgt(self):
		return self._SubmitgAgt

	@SubmitgAgt.setter
	def SubmitgAgt(self, value):
		self._SubmitgAgt = value if type(value) != base_types.auto else self.make_default("SubmitgAgt")

	@SubmitgAgt.deleter
	def SubmitgAgt(self):
		del self._SubmitgAgt
		self._SubmitgAgt = None

	@property
	def Oprtr(self):
		return self._Oprtr

	@Oprtr.setter
	def Oprtr(self, value):
		self._Oprtr = value if type(value) != base_types.auto else self.make_default("Oprtr")

	@Oprtr.deleter
	def Oprtr(self):
		del self._Oprtr
		self._Oprtr = None

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
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if type(value) != base_types.auto else self.make_default("OthrCtrPty")

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = None

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if type(value) != base_types.auto else self.make_default("RptgCtrPty")

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = None

	@property
	def CCP(self):
		return self._CCP

	@CCP.setter
	def CCP(self, value):
		self._CCP = value if type(value) != base_types.auto else self.make_default("CCP")

	@CCP.deleter
	def CCP(self):
		del self._CCP
		self._CCP = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='NttyRspnsblForRpt', type=TradePartyIdentificationQuery11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitgAgt', type=TradePartyIdentificationQuery11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oprtr', type=Operation3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brkr', type=TradePartyIdentificationQuery11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bnfcry', type=TradePartyIdentificationQuery10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=TradePartyIdentificationQuery10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=TradePartyIdentificationQuery10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCP', type=TradePartyIdentificationQuery11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmb', type=TradePartyIdentificationQuery10Choice, min=0, max=1, mutex_group=None, array=False),
	))

