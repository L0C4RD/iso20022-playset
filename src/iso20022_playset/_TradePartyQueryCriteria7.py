# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Operation3Code
from . import TradePartyIdentificationQuery10Choice
from . import TradePartyIdentificationQuery11Choice

class TradePartyQueryCriteria7(base_types._BaseFieldType):

	__slots__ = ["_Bnfcry", "_Brkr", "_CCP", "_ClrMmb", "_NttyRspnsblForRpt", "_Oprtr", "_OthrCtrPty", "_RptgCtrPty", "_SubmitgAgt"]
	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if value is not None else base_types.UninitialisedField(self, 'Bnfcry', TradePartyIdentificationQuery10Choice, False)

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = base_types.UninitialisedField(self, 'Bnfcry', TradePartyIdentificationQuery10Choice, False)

	@property
	def Brkr(self):
		return self._Brkr

	@Brkr.setter
	def Brkr(self, value):
		self._Brkr = value if value is not None else base_types.UninitialisedField(self, 'Brkr', TradePartyIdentificationQuery11Choice, False)

	@Brkr.deleter
	def Brkr(self):
		del self._Brkr
		self._Brkr = base_types.UninitialisedField(self, 'Brkr', TradePartyIdentificationQuery11Choice, False)

	@property
	def CCP(self):
		return self._CCP

	@CCP.setter
	def CCP(self, value):
		self._CCP = value if value is not None else base_types.UninitialisedField(self, 'CCP', TradePartyIdentificationQuery11Choice, False)

	@CCP.deleter
	def CCP(self):
		del self._CCP
		self._CCP = base_types.UninitialisedField(self, 'CCP', TradePartyIdentificationQuery11Choice, False)

	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if value is not None else base_types.UninitialisedField(self, 'ClrMmb', TradePartyIdentificationQuery10Choice, False)

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = base_types.UninitialisedField(self, 'ClrMmb', TradePartyIdentificationQuery10Choice, False)

	@property
	def NttyRspnsblForRpt(self):
		return self._NttyRspnsblForRpt

	@NttyRspnsblForRpt.setter
	def NttyRspnsblForRpt(self, value):
		self._NttyRspnsblForRpt = value if value is not None else base_types.UninitialisedField(self, 'NttyRspnsblForRpt', TradePartyIdentificationQuery11Choice, False)

	@NttyRspnsblForRpt.deleter
	def NttyRspnsblForRpt(self):
		del self._NttyRspnsblForRpt
		self._NttyRspnsblForRpt = base_types.UninitialisedField(self, 'NttyRspnsblForRpt', TradePartyIdentificationQuery11Choice, False)

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
		self._OthrCtrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrCtrPty', TradePartyIdentificationQuery10Choice, False)

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = base_types.UninitialisedField(self, 'OthrCtrPty', TradePartyIdentificationQuery10Choice, False)

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if value is not None else base_types.UninitialisedField(self, 'RptgCtrPty', TradePartyIdentificationQuery10Choice, False)

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = base_types.UninitialisedField(self, 'RptgCtrPty', TradePartyIdentificationQuery10Choice, False)

	@property
	def SubmitgAgt(self):
		return self._SubmitgAgt

	@SubmitgAgt.setter
	def SubmitgAgt(self, value):
		self._SubmitgAgt = value if value is not None else base_types.UninitialisedField(self, 'SubmitgAgt', TradePartyIdentificationQuery11Choice, False)

	@SubmitgAgt.deleter
	def SubmitgAgt(self):
		del self._SubmitgAgt
		self._SubmitgAgt = base_types.UninitialisedField(self, 'SubmitgAgt', TradePartyIdentificationQuery11Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bnfcry', type=TradePartyIdentificationQuery10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brkr', type=TradePartyIdentificationQuery11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CCP', type=TradePartyIdentificationQuery11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmb', type=TradePartyIdentificationQuery10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NttyRspnsblForRpt', type=TradePartyIdentificationQuery11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oprtr', type=Operation3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=TradePartyIdentificationQuery10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgCtrPty', type=TradePartyIdentificationQuery10Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitgAgt', type=TradePartyIdentificationQuery11Choice, min=0, max=1, mutex_group=None, array=False),
	))