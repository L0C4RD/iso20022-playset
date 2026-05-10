from . import base_types
import ISODate
import PartyIdentification35Choice
import PartyIdentificationAndAccount31
import Price4
import AmountAndDirection27
import SafekeepingPlaceFormat7Choice
import Max35Text
import PartyIdentification34Choice
import SecuritiesAccount19
import SecurityIdentification14
import FinancialInstrumentQuantity1Choice

class SettlementObligation7(base_types._BaseFieldType):

	__slots__ = ["_ClrSgmt", "_DealPric", "_SfkpgAcct", "_NonClrMmb", "_PrvsBuyInId", "_IntnddSttlmDt", "_SttlmAmt", "_CSDTxId", "_RmngQtyToBeSttld", "_Dpstry", "_FinInstrmId", "_RmngAmtToBeSttld", "_TradDt", "_DlvryAcct", "_Qty", "_CntrlCtrPtyTxId", "_SfkpgPlc"]
	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if type(value) != auto else self.make_default("ClrSgmt")

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = None

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if type(value) != auto else self.make_default("DealPric")

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if type(value) != auto else self.make_default("NonClrMmb")

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = None

	@property
	def PrvsBuyInId(self):
		return self._PrvsBuyInId

	@PrvsBuyInId.setter
	def PrvsBuyInId(self, value):
		self._PrvsBuyInId = value if type(value) != auto else self.make_default("PrvsBuyInId")

	@PrvsBuyInId.deleter
	def PrvsBuyInId(self):
		del self._PrvsBuyInId
		self._PrvsBuyInId = None

	@property
	def IntnddSttlmDt(self):
		return self._IntnddSttlmDt

	@IntnddSttlmDt.setter
	def IntnddSttlmDt(self, value):
		self._IntnddSttlmDt = value if type(value) != auto else self.make_default("IntnddSttlmDt")

	@IntnddSttlmDt.deleter
	def IntnddSttlmDt(self):
		del self._IntnddSttlmDt
		self._IntnddSttlmDt = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def CSDTxId(self):
		return self._CSDTxId

	@CSDTxId.setter
	def CSDTxId(self, value):
		self._CSDTxId = value if type(value) != auto else self.make_default("CSDTxId")

	@CSDTxId.deleter
	def CSDTxId(self):
		del self._CSDTxId
		self._CSDTxId = None

	@property
	def RmngQtyToBeSttld(self):
		return self._RmngQtyToBeSttld

	@RmngQtyToBeSttld.setter
	def RmngQtyToBeSttld(self, value):
		self._RmngQtyToBeSttld = value if type(value) != auto else self.make_default("RmngQtyToBeSttld")

	@RmngQtyToBeSttld.deleter
	def RmngQtyToBeSttld(self):
		del self._RmngQtyToBeSttld
		self._RmngQtyToBeSttld = None

	@property
	def Dpstry(self):
		return self._Dpstry

	@Dpstry.setter
	def Dpstry(self, value):
		self._Dpstry = value if type(value) != auto else self.make_default("Dpstry")

	@Dpstry.deleter
	def Dpstry(self):
		del self._Dpstry
		self._Dpstry = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def RmngAmtToBeSttld(self):
		return self._RmngAmtToBeSttld

	@RmngAmtToBeSttld.setter
	def RmngAmtToBeSttld(self, value):
		self._RmngAmtToBeSttld = value if type(value) != auto else self.make_default("RmngAmtToBeSttld")

	@RmngAmtToBeSttld.deleter
	def RmngAmtToBeSttld(self):
		del self._RmngAmtToBeSttld
		self._RmngAmtToBeSttld = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def DlvryAcct(self):
		return self._DlvryAcct

	@DlvryAcct.setter
	def DlvryAcct(self, value):
		self._DlvryAcct = value if type(value) != auto else self.make_default("DlvryAcct")

	@DlvryAcct.deleter
	def DlvryAcct(self):
		del self._DlvryAcct
		self._DlvryAcct = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def CntrlCtrPtyTxId(self):
		return self._CntrlCtrPtyTxId

	@CntrlCtrPtyTxId.setter
	def CntrlCtrPtyTxId(self, value):
		self._CntrlCtrPtyTxId = value if type(value) != auto else self.make_default("CntrlCtrPtyTxId")

	@CntrlCtrPtyTxId.deleter
	def CntrlCtrPtyTxId(self):
		del self._CntrlCtrPtyTxId
		self._CntrlCtrPtyTxId = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsBuyInId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntnddSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection27, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CSDTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngQtyToBeSttld', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dpstry', type=PartyIdentification34Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngAmtToBeSttld', type=AmountAndDirection27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrlCtrPtyTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat7Choice, min=0, max=1, mutex_group=None, array=False),
	))

