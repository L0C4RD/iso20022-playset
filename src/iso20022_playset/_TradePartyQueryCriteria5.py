from . import base_types
from ._TradePartyIdentificationQuery9 import TradePartyIdentificationQuery9
from ._TradePartyIdentificationQuery8 import TradePartyIdentificationQuery8
from ._Operation3Code import Operation3Code

class TradePartyQueryCriteria5(base_types._BaseFieldType):

	__slots__ = ["_OthrCtrPtyBrnch", "_RptgCtrPty", "_TrptyAgt", "_CCP", "_OthrCtrPty", "_RptgCtrPtyBrnch", "_SubmitgAgt", "_AgtLndr", "_Brkr", "_Bnfcry", "_Oprtr"]
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
	def OthrCtrPtyBrnch(self):
		return self._OthrCtrPtyBrnch

	@OthrCtrPtyBrnch.setter
	def OthrCtrPtyBrnch(self, value):
		self._OthrCtrPtyBrnch = value if type(value) != base_types.auto else self.make_default("OthrCtrPtyBrnch")

	@OthrCtrPtyBrnch.deleter
	def OthrCtrPtyBrnch(self):
		del self._OthrCtrPtyBrnch
		self._OthrCtrPtyBrnch = None

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
	def RptgCtrPtyBrnch(self):
		return self._RptgCtrPtyBrnch

	@RptgCtrPtyBrnch.setter
	def RptgCtrPtyBrnch(self, value):
		self._RptgCtrPtyBrnch = value if type(value) != base_types.auto else self.make_default("RptgCtrPtyBrnch")

	@RptgCtrPtyBrnch.deleter
	def RptgCtrPtyBrnch(self):
		del self._RptgCtrPtyBrnch
		self._RptgCtrPtyBrnch = None

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
		base_types.FieldEntry(name='AgtLndr', type=TradePartyIdentificationQuery8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bnfcry', type=TradePartyIdentificationQuery8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brkr', type=TradePartyIdentificationQuery8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCP', type=TradePartyIdentificationQuery8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oprtr', type=Operation3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=TradePartyIdentificationQuery8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPtyBrnch', type=TradePartyIdentificationQuery9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=TradePartyIdentificationQuery8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPtyBrnch', type=TradePartyIdentificationQuery9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitgAgt', type=TradePartyIdentificationQuery8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgt', type=TradePartyIdentificationQuery8, min=0, max=1, mutex_group=None, array=False),
	))

