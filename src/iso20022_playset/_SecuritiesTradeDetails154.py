# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection52
from . import DeliveryReceiptType2Code
from . import DigitalPaymentSettlement1
from . import FinancialInstrumentAttributes111
from . import Max35Text
from . import Max3Number
from . import OtherAmounts29
from . import OtherParties39
from . import PortfolioTransferStatus2Choice
from . import Quantity48
from . import ReceiveDelivery1Code
from . import Reporting7Choice
from . import SecurityIdentification19
from . import SettlementDate17Choice
from . import SettlementDetails236
from . import SettlementParties128
from . import SupplementaryData1
from . import TradeDate8Choice

class SecuritiesTradeDetails154(base_types._BaseFieldType):

	__slots__ = ["_CmonId", "_DgtlPmtSttlm", "_DlvrgSttlmPties", "_FinInstrmAttrbts", "_FinInstrmId", "_NbOfDaysAcrd", "_NtfctnRcvrTxId", "_NtfctnSndrTxId", "_OthrAmts", "_OthrBizPties", "_Pmt", "_QtyDtls", "_RcvgSttlmPties", "_Rptg", "_SctiesMvmntTp", "_SplmtryData", "_Sts", "_SttlmAmt", "_SttlmDt", "_SttlmParams", "_TradDt"]
	@property
	def CmonId(self):
		return self._CmonId

	@CmonId.setter
	def CmonId(self, value):
		self._CmonId = value if value is not None else base_types.UninitialisedField(self, 'CmonId', Max35Text, False)

	@CmonId.deleter
	def CmonId(self):
		del self._CmonId
		self._CmonId = base_types.UninitialisedField(self, 'CmonId', Max35Text, False)

	@property
	def DgtlPmtSttlm(self):
		return self._DgtlPmtSttlm

	@DgtlPmtSttlm.setter
	def DgtlPmtSttlm(self, value):
		self._DgtlPmtSttlm = value if value is not None else base_types.UninitialisedField(self, 'DgtlPmtSttlm', DigitalPaymentSettlement1, True)

	@DgtlPmtSttlm.deleter
	def DgtlPmtSttlm(self):
		del self._DgtlPmtSttlm
		self._DgtlPmtSttlm = base_types.UninitialisedField(self, 'DgtlPmtSttlm', DigitalPaymentSettlement1, True)

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties128, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties128, False)

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes111, False)

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes111, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDaysAcrd', Max3Number, False)

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = base_types.UninitialisedField(self, 'NbOfDaysAcrd', Max3Number, False)

	@property
	def NtfctnRcvrTxId(self):
		return self._NtfctnRcvrTxId

	@NtfctnRcvrTxId.setter
	def NtfctnRcvrTxId(self, value):
		self._NtfctnRcvrTxId = value if value is not None else base_types.UninitialisedField(self, 'NtfctnRcvrTxId', Max35Text, False)

	@NtfctnRcvrTxId.deleter
	def NtfctnRcvrTxId(self):
		del self._NtfctnRcvrTxId
		self._NtfctnRcvrTxId = base_types.UninitialisedField(self, 'NtfctnRcvrTxId', Max35Text, False)

	@property
	def NtfctnSndrTxId(self):
		return self._NtfctnSndrTxId

	@NtfctnSndrTxId.setter
	def NtfctnSndrTxId(self, value):
		self._NtfctnSndrTxId = value if value is not None else base_types.UninitialisedField(self, 'NtfctnSndrTxId', Max35Text, False)

	@NtfctnSndrTxId.deleter
	def NtfctnSndrTxId(self):
		del self._NtfctnSndrTxId
		self._NtfctnSndrTxId = base_types.UninitialisedField(self, 'NtfctnSndrTxId', Max35Text, False)

	@property
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if value is not None else base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts29, False)

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts29, False)

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if value is not None else base_types.UninitialisedField(self, 'OthrBizPties', OtherParties39, False)

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = base_types.UninitialisedField(self, 'OthrBizPties', OtherParties39, False)

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
	def QtyDtls(self):
		return self._QtyDtls

	@QtyDtls.setter
	def QtyDtls(self, value):
		self._QtyDtls = value if value is not None else base_types.UninitialisedField(self, 'QtyDtls', Quantity48, False)

	@QtyDtls.deleter
	def QtyDtls(self):
		del self._QtyDtls
		self._QtyDtls = base_types.UninitialisedField(self, 'QtyDtls', Quantity48, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties128, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties128, False)

	@property
	def Rptg(self):
		return self._Rptg

	@Rptg.setter
	def Rptg(self, value):
		self._Rptg = value if value is not None else base_types.UninitialisedField(self, 'Rptg', Reporting7Choice, True)

	@Rptg.deleter
	def Rptg(self):
		del self._Rptg
		self._Rptg = base_types.UninitialisedField(self, 'Rptg', Reporting7Choice, True)

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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', PortfolioTransferStatus2Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', PortfolioTransferStatus2Choice, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection52, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection52, False)

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', SettlementDate17Choice, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', SettlementDate17Choice, False)

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if value is not None else base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails236, False)

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails236, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', TradeDate8Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', TradeDate8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlPmtSttlm', type=DigitalPaymentSettlement1, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties128, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnRcvrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnSndrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyDtls', type=Quantity48, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties128, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rptg', type=Reporting7Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=PortfolioTransferStatus2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection52, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate17Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails236, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
	))