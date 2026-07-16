# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection27
from . import ClearingAccountType1Code
from . import DateFormat65Choice
from . import DeliveryReceiptType2Code
from . import FinancialInstrumentQuantity1Choice
from . import MarketIdentification84
from . import Max35Text
from . import ReceiveDelivery1Code
from . import SafekeepingPlaceFormat43Choice
from . import SecuritiesAccount19
from . import SecurityIdentification48
from . import SettlementObligation10
from . import SettlementParties38Choice
from . import TradeDate3Choice
from . import TradingCapacity5Code

class SettlementObligation9(base_types._BaseFieldType):

	__slots__ = ["_AddtlSttlmOblgtnDtls", "_ClrAcctTp", "_FinInstrmId", "_IntnddSttlmDt", "_PlcOfTrad", "_Pmt", "_Qty", "_SctiesMvmntTp", "_SfkpgAcct", "_SfkpgPlc", "_SttlmAmt", "_SttlmOblgtnId", "_SttlmPties", "_TradDt", "_TradgCpcty"]
	@property
	def AddtlSttlmOblgtnDtls(self):
		return self._AddtlSttlmOblgtnDtls

	@AddtlSttlmOblgtnDtls.setter
	def AddtlSttlmOblgtnDtls(self, value):
		self._AddtlSttlmOblgtnDtls = value if value is not None else base_types.UninitialisedField(self, 'AddtlSttlmOblgtnDtls', SettlementObligation10, True)

	@AddtlSttlmOblgtnDtls.deleter
	def AddtlSttlmOblgtnDtls(self):
		del self._AddtlSttlmOblgtnDtls
		self._AddtlSttlmOblgtnDtls = base_types.UninitialisedField(self, 'AddtlSttlmOblgtnDtls', SettlementObligation10, True)

	@property
	def ClrAcctTp(self):
		return self._ClrAcctTp

	@ClrAcctTp.setter
	def ClrAcctTp(self, value):
		self._ClrAcctTp = value if value is not None else base_types.UninitialisedField(self, 'ClrAcctTp', ClearingAccountType1Code, False)

	@ClrAcctTp.deleter
	def ClrAcctTp(self):
		del self._ClrAcctTp
		self._ClrAcctTp = base_types.UninitialisedField(self, 'ClrAcctTp', ClearingAccountType1Code, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification48, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification48, False)

	@property
	def IntnddSttlmDt(self):
		return self._IntnddSttlmDt

	@IntnddSttlmDt.setter
	def IntnddSttlmDt(self, value):
		self._IntnddSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntnddSttlmDt', DateFormat65Choice, False)

	@IntnddSttlmDt.deleter
	def IntnddSttlmDt(self):
		del self._IntnddSttlmDt
		self._IntnddSttlmDt = base_types.UninitialisedField(self, 'IntnddSttlmDt', DateFormat65Choice, False)

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', MarketIdentification84, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', MarketIdentification84, False)

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if value is not None else base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = base_types.UninitialisedField(self, 'Pmt', DeliveryReceiptType2Code, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity1Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity1Choice, False)

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = base_types.UninitialisedField(self, 'SctiesMvmntTp', ReceiveDelivery1Code, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat43Choice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormat43Choice, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection27, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection27, False)

	@property
	def SttlmOblgtnId(self):
		return self._SttlmOblgtnId

	@SttlmOblgtnId.setter
	def SttlmOblgtnId(self, value):
		self._SttlmOblgtnId = value if value is not None else base_types.UninitialisedField(self, 'SttlmOblgtnId', Max35Text, False)

	@SttlmOblgtnId.deleter
	def SttlmOblgtnId(self):
		del self._SttlmOblgtnId
		self._SttlmOblgtnId = base_types.UninitialisedField(self, 'SttlmOblgtnId', Max35Text, False)

	@property
	def SttlmPties(self):
		return self._SttlmPties

	@SttlmPties.setter
	def SttlmPties(self, value):
		self._SttlmPties = value if value is not None else base_types.UninitialisedField(self, 'SttlmPties', SettlementParties38Choice, False)

	@SttlmPties.deleter
	def SttlmPties(self):
		del self._SttlmPties
		self._SttlmPties = base_types.UninitialisedField(self, 'SttlmPties', SettlementParties38Choice, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', TradeDate3Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', TradeDate3Choice, False)

	@property
	def TradgCpcty(self):
		return self._TradgCpcty

	@TradgCpcty.setter
	def TradgCpcty(self, value):
		self._TradgCpcty = value if value is not None else base_types.UninitialisedField(self, 'TradgCpcty', TradingCapacity5Code, False)

	@TradgCpcty.deleter
	def TradgCpcty(self):
		del self._TradgCpcty
		self._TradgCpcty = base_types.UninitialisedField(self, 'TradgCpcty', TradingCapacity5Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSttlmOblgtnDtls', type=SettlementObligation10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrAcctTp', type=ClearingAccountType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification48, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntnddSttlmDt', type=DateFormat65Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=MarketIdentification84, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection27, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmOblgtnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmPties', type=SettlementParties38Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCpcty', type=TradingCapacity5Code, min=0, max=1, mutex_group=None, array=False),
	))