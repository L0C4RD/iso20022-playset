import base_types
import ClearingAccountType1Code
import FinancialInstrumentQuantity1Choice
import AmountAndDirection27
import ReceiveDelivery1Code
import MarketIdentification84
import SecuritiesAccount19
import DeliveryReceiptType2Code
import SettlementParties38Choice
import SettlementObligation10
import Max35Text
import DateFormat65Choice
import SafekeepingPlaceFormat43Choice
import TradeDate3Choice
import TradingCapacity5Code
import SecurityIdentification48

class SettlementObligation9(base_types._BaseFieldType):

	__slots__ = ["_ClrAcctTp", "_IntnddSttlmDt", "_SfkpgAcct", "_SttlmOblgtnId", "_PlcOfTrad", "_Pmt", "_Qty", "_SfkpgPlc", "_SttlmPties", "_AddtlSttlmOblgtnDtls", "_SttlmAmt", "_SctiesMvmntTp", "_TradDt", "_FinInstrmId", "_TradgCpcty"]
	@property
	def ClrAcctTp(self):
		return self._ClrAcctTp

	@ClrAcctTp.setter
	def ClrAcctTp(self, value):
		self._ClrAcctTp = value if type(value) != auto else self.make_default("ClrAcctTp")

	@ClrAcctTp.deleter
	def ClrAcctTp(self):
		del self._ClrAcctTp
		self._ClrAcctTp = None

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
	def SttlmOblgtnId(self):
		return self._SttlmOblgtnId

	@SttlmOblgtnId.setter
	def SttlmOblgtnId(self, value):
		self._SttlmOblgtnId = value if type(value) != auto else self.make_default("SttlmOblgtnId")

	@SttlmOblgtnId.deleter
	def SttlmOblgtnId(self):
		del self._SttlmOblgtnId
		self._SttlmOblgtnId = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

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
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def SttlmPties(self):
		return self._SttlmPties

	@SttlmPties.setter
	def SttlmPties(self, value):
		self._SttlmPties = value if type(value) != auto else self.make_default("SttlmPties")

	@SttlmPties.deleter
	def SttlmPties(self):
		del self._SttlmPties
		self._SttlmPties = None

	@property
	def AddtlSttlmOblgtnDtls(self):
		return self._AddtlSttlmOblgtnDtls

	@AddtlSttlmOblgtnDtls.setter
	def AddtlSttlmOblgtnDtls(self, value):
		self._AddtlSttlmOblgtnDtls = value if type(value) != auto else self.make_default("AddtlSttlmOblgtnDtls")

	@AddtlSttlmOblgtnDtls.deleter
	def AddtlSttlmOblgtnDtls(self):
		del self._AddtlSttlmOblgtnDtls
		self._AddtlSttlmOblgtnDtls = None

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
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if type(value) != auto else self.make_default("SctiesMvmntTp")

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = None

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
	def TradgCpcty(self):
		return self._TradgCpcty

	@TradgCpcty.setter
	def TradgCpcty(self, value):
		self._TradgCpcty = value if type(value) != auto else self.make_default("TradgCpcty")

	@TradgCpcty.deleter
	def TradgCpcty(self):
		del self._TradgCpcty
		self._TradgCpcty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrAcctTp', type=ClearingAccountType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntnddSttlmDt', type=DateFormat65Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmOblgtnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=MarketIdentification84, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPties', type=SettlementParties38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlSttlmOblgtnDtls', type=SettlementObligation10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection27, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification48, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCpcty', type=TradingCapacity5Code, min=0, max=1, mutex_group=None, array=False),
	))

