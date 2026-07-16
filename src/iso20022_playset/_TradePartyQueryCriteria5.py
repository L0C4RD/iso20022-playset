# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Operation3Code
from . import TradePartyIdentificationQuery8
from . import TradePartyIdentificationQuery9

class TradePartyQueryCriteria5(base_types._BaseFieldType):

	__slots__ = ["_AgtLndr", "_Bnfcry", "_Brkr", "_CCP", "_Oprtr", "_OthrCtrPty", "_OthrCtrPtyBrnch", "_RptgCtrPty", "_RptgCtrPtyBrnch", "_SubmitgAgt", "_TrptyAgt"]
	@property
	def AgtLndr(self):
		return self._AgtLndr

	@AgtLndr.setter
	def AgtLndr(self, value):
		self._AgtLndr = value if value is not None else base_types.UninitialisedField(self, 'AgtLndr', TradePartyIdentificationQuery8, False)

	@AgtLndr.deleter
	def AgtLndr(self):
		del self._AgtLndr
		self._AgtLndr = base_types.UninitialisedField(self, 'AgtLndr', TradePartyIdentificationQuery8, False)

	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if value is not None else base_types.UninitialisedField(self, 'Bnfcry', TradePartyIdentificationQuery8, False)

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = base_types.UninitialisedField(self, 'Bnfcry', TradePartyIdentificationQuery8, False)

	@property
	def Brkr(self):
		return self._Brkr

	@Brkr.setter
	def Brkr(self, value):
		self._Brkr = value if value is not None else base_types.UninitialisedField(self, 'Brkr', TradePartyIdentificationQuery8, False)

	@Brkr.deleter
	def Brkr(self):
		del self._Brkr
		self._Brkr = base_types.UninitialisedField(self, 'Brkr', TradePartyIdentificationQuery8, False)

	@property
	def CCP(self):
		return self._CCP

	@CCP.setter
	def CCP(self, value):
		self._CCP = value if value is not None else base_types.UninitialisedField(self, 'CCP', TradePartyIdentificationQuery8, False)

	@CCP.deleter
	def CCP(self):
		del self._CCP
		self._CCP = base_types.UninitialisedField(self, 'CCP', TradePartyIdentificationQuery8, False)

	@property
	def Oprtr(self):
		return self._Oprtr

	@Oprtr.setter
	def Oprtr(self, value):
		self._Oprtr = value if value is not None else base_types.UninitialisedField(self, 'Oprtr', Operation3Code, False)

	@Oprtr.deleter
	def Oprtr(self):
		del self._Oprtr
		self._Oprtr = base_types.UninitialisedField(self, 'Oprtr', Operation3Code, False)

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrCtrPty', TradePartyIdentificationQuery8, False)

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = base_types.UninitialisedField(self, 'OthrCtrPty', TradePartyIdentificationQuery8, False)

	@property
	def OthrCtrPtyBrnch(self):
		return self._OthrCtrPtyBrnch

	@OthrCtrPtyBrnch.setter
	def OthrCtrPtyBrnch(self, value):
		self._OthrCtrPtyBrnch = value if value is not None else base_types.UninitialisedField(self, 'OthrCtrPtyBrnch', TradePartyIdentificationQuery9, False)

	@OthrCtrPtyBrnch.deleter
	def OthrCtrPtyBrnch(self):
		del self._OthrCtrPtyBrnch
		self._OthrCtrPtyBrnch = base_types.UninitialisedField(self, 'OthrCtrPtyBrnch', TradePartyIdentificationQuery9, False)

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if value is not None else base_types.UninitialisedField(self, 'RptgCtrPty', TradePartyIdentificationQuery8, False)

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = base_types.UninitialisedField(self, 'RptgCtrPty', TradePartyIdentificationQuery8, False)

	@property
	def RptgCtrPtyBrnch(self):
		return self._RptgCtrPtyBrnch

	@RptgCtrPtyBrnch.setter
	def RptgCtrPtyBrnch(self, value):
		self._RptgCtrPtyBrnch = value if value is not None else base_types.UninitialisedField(self, 'RptgCtrPtyBrnch', TradePartyIdentificationQuery9, False)

	@RptgCtrPtyBrnch.deleter
	def RptgCtrPtyBrnch(self):
		del self._RptgCtrPtyBrnch
		self._RptgCtrPtyBrnch = base_types.UninitialisedField(self, 'RptgCtrPtyBrnch', TradePartyIdentificationQuery9, False)

	@property
	def SubmitgAgt(self):
		return self._SubmitgAgt

	@SubmitgAgt.setter
	def SubmitgAgt(self, value):
		self._SubmitgAgt = value if value is not None else base_types.UninitialisedField(self, 'SubmitgAgt', TradePartyIdentificationQuery8, False)

	@SubmitgAgt.deleter
	def SubmitgAgt(self):
		del self._SubmitgAgt
		self._SubmitgAgt = base_types.UninitialisedField(self, 'SubmitgAgt', TradePartyIdentificationQuery8, False)

	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgt', TradePartyIdentificationQuery8, False)

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = base_types.UninitialisedField(self, 'TrptyAgt', TradePartyIdentificationQuery8, False)

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