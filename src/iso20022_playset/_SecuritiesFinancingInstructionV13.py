# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection94
from . import CashParties41
from . import DigitalPaymentSettlement1
from . import FinancialInstrumentAttributes111
from . import Linkages79
from . import Max35Text
from . import NumberCount2Choice
from . import OtherAmounts45
from . import OtherParties43
from . import QuantityAndAccount117
from . import SecuritiesFinancingTransactionDetails56
from . import SecuritiesTradeDetails116
from . import SecurityIdentification19
from . import SettlementDetails226
from . import SettlementParties126
from . import StandingSettlementInstruction20
from . import SupplementaryData1
from . import TransactionTypeAndAdditionalParameters21

class SecuritiesFinancingInstructionV13(base_types._BaseFieldType):

	__slots__ = ["_CshPties", "_DgtlPmtSttlm", "_DlvrgSttlmPties", "_FinInstrmAttrbts", "_FinInstrmId", "_Lnkgs", "_NbCounts", "_OpngSttlmAmt", "_OthrAmts", "_OthrBizPties", "_QtyAndAcctDtls", "_RcvgSttlmPties", "_SctiesFincgDtls", "_SplmtryData", "_StgSttlmInstrDtls", "_SttlmParams", "_TradDtls", "_TxId", "_TxTpAndAddtlParams"]
	@property
	def CshPties(self):
		return self._CshPties

	@CshPties.setter
	def CshPties(self, value):
		self._CshPties = value if value is not None else base_types.UninitialisedField(self, 'CshPties', CashParties41, False)

	@CshPties.deleter
	def CshPties(self):
		del self._CshPties
		self._CshPties = base_types.UninitialisedField(self, 'CshPties', CashParties41, False)

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
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties126, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties126, False)

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
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if value is not None else base_types.UninitialisedField(self, 'Lnkgs', Linkages79, True)

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = base_types.UninitialisedField(self, 'Lnkgs', Linkages79, True)

	@property
	def NbCounts(self):
		return self._NbCounts

	@NbCounts.setter
	def NbCounts(self, value):
		self._NbCounts = value if value is not None else base_types.UninitialisedField(self, 'NbCounts', NumberCount2Choice, False)

	@NbCounts.deleter
	def NbCounts(self):
		del self._NbCounts
		self._NbCounts = base_types.UninitialisedField(self, 'NbCounts', NumberCount2Choice, False)

	@property
	def OpngSttlmAmt(self):
		return self._OpngSttlmAmt

	@OpngSttlmAmt.setter
	def OpngSttlmAmt(self, value):
		self._OpngSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'OpngSttlmAmt', AmountAndDirection94, False)

	@OpngSttlmAmt.deleter
	def OpngSttlmAmt(self):
		del self._OpngSttlmAmt
		self._OpngSttlmAmt = base_types.UninitialisedField(self, 'OpngSttlmAmt', AmountAndDirection94, False)

	@property
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if value is not None else base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts45, False)

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts45, False)

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if value is not None else base_types.UninitialisedField(self, 'OthrBizPties', OtherParties43, False)

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = base_types.UninitialisedField(self, 'OthrBizPties', OtherParties43, False)

	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount117, False)

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount117, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties126, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties126, False)

	@property
	def SctiesFincgDtls(self):
		return self._SctiesFincgDtls

	@SctiesFincgDtls.setter
	def SctiesFincgDtls(self, value):
		self._SctiesFincgDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgDtls', SecuritiesFinancingTransactionDetails56, False)

	@SctiesFincgDtls.deleter
	def SctiesFincgDtls(self):
		del self._SctiesFincgDtls
		self._SctiesFincgDtls = base_types.UninitialisedField(self, 'SctiesFincgDtls', SecuritiesFinancingTransactionDetails56, False)

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
	def StgSttlmInstrDtls(self):
		return self._StgSttlmInstrDtls

	@StgSttlmInstrDtls.setter
	def StgSttlmInstrDtls(self, value):
		self._StgSttlmInstrDtls = value if value is not None else base_types.UninitialisedField(self, 'StgSttlmInstrDtls', StandingSettlementInstruction20, False)

	@StgSttlmInstrDtls.deleter
	def StgSttlmInstrDtls(self):
		del self._StgSttlmInstrDtls
		self._StgSttlmInstrDtls = base_types.UninitialisedField(self, 'StgSttlmInstrDtls', StandingSettlementInstruction20, False)

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if value is not None else base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails226, False)

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails226, False)

	@property
	def TradDtls(self):
		return self._TradDtls

	@TradDtls.setter
	def TradDtls(self, value):
		self._TradDtls = value if value is not None else base_types.UninitialisedField(self, 'TradDtls', SecuritiesTradeDetails116, False)

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = base_types.UninitialisedField(self, 'TradDtls', SecuritiesTradeDetails116, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@property
	def TxTpAndAddtlParams(self):
		return self._TxTpAndAddtlParams

	@TxTpAndAddtlParams.setter
	def TxTpAndAddtlParams(self, value):
		self._TxTpAndAddtlParams = value if value is not None else base_types.UninitialisedField(self, 'TxTpAndAddtlParams', TransactionTypeAndAdditionalParameters21, False)

	@TxTpAndAddtlParams.deleter
	def TxTpAndAddtlParams(self):
		del self._TxTpAndAddtlParams
		self._TxTpAndAddtlParams = base_types.UninitialisedField(self, 'TxTpAndAddtlParams', TransactionTypeAndAdditionalParameters21, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshPties', type=CashParties41, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlPmtSttlm', type=DigitalPaymentSettlement1, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes111, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages79, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbCounts', type=NumberCount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngSttlmAmt', type=AmountAndDirection94, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts45, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount117, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgDtls', type=SecuritiesFinancingTransactionDetails56, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StgSttlmInstrDtls', type=StandingSettlementInstruction20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails226, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails116, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTpAndAddtlParams', type=TransactionTypeAndAdditionalParameters21, min=1, max=1, mutex_group=None, array=False),
	))