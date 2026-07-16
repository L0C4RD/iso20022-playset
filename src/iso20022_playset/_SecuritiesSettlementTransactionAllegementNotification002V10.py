# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection92
from . import CashParties40
from . import FinancialInstrumentAttributes122
from . import Max35Text
from . import OtherAmounts36
from . import OtherParties37
from . import QuantityAndAccount106
from . import RestrictedFINXMax16Text
from . import SecuritiesFinancingTransactionDetails50
from . import SecuritiesTradeDetails126
from . import SecurityIdentification20
from . import SettlementDetails191
from . import SettlementParties105
from . import SettlementTypeAndAdditionalParameters15
from . import SupplementaryData1

class SecuritiesSettlementTransactionAllegementNotification002V10(base_types._BaseFieldType):

	__slots__ = ["_CshPties", "_CtrPtyMktInfrstrctrTxId", "_DlvrgSttlmPties", "_FinInstrmAttrbts", "_FinInstrmId", "_MktInfrstrctrTxId", "_OthrAmts", "_OthrBizPties", "_QtyAndAcctDtls", "_RcvgSttlmPties", "_SctiesFincgDtls", "_SplmtryData", "_SttlmAmt", "_SttlmParams", "_SttlmTpAndAddtlParams", "_TradDtls", "_TxId"]
	@property
	def CshPties(self):
		return self._CshPties

	@CshPties.setter
	def CshPties(self, value):
		self._CshPties = value if value is not None else base_types.UninitialisedField(self, 'CshPties', CashParties40, False)

	@CshPties.deleter
	def CshPties(self):
		del self._CshPties
		self._CshPties = base_types.UninitialisedField(self, 'CshPties', CashParties40, False)

	@property
	def CtrPtyMktInfrstrctrTxId(self):
		return self._CtrPtyMktInfrstrctrTxId

	@CtrPtyMktInfrstrctrTxId.setter
	def CtrPtyMktInfrstrctrTxId(self, value):
		self._CtrPtyMktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyMktInfrstrctrTxId', Max35Text, False)

	@CtrPtyMktInfrstrctrTxId.deleter
	def CtrPtyMktInfrstrctrTxId(self):
		del self._CtrPtyMktInfrstrctrTxId
		self._CtrPtyMktInfrstrctrTxId = base_types.UninitialisedField(self, 'CtrPtyMktInfrstrctrTxId', Max35Text, False)

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties105, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties105, False)

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes122, False)

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = base_types.UninitialisedField(self, 'FinInstrmAttrbts', FinancialInstrumentAttributes122, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification20, False)

	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if value is not None else base_types.UninitialisedField(self, 'MktInfrstrctrTxId', RestrictedFINXMax16Text, False)

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = base_types.UninitialisedField(self, 'MktInfrstrctrTxId', RestrictedFINXMax16Text, False)

	@property
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if value is not None else base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts36, False)

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts36, False)

	@property
	def OthrBizPties(self):
		return self._OthrBizPties

	@OthrBizPties.setter
	def OthrBizPties(self, value):
		self._OthrBizPties = value if value is not None else base_types.UninitialisedField(self, 'OthrBizPties', OtherParties37, False)

	@OthrBizPties.deleter
	def OthrBizPties(self):
		del self._OthrBizPties
		self._OthrBizPties = base_types.UninitialisedField(self, 'OthrBizPties', OtherParties37, False)

	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount106, False)

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount106, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties105, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties105, False)

	@property
	def SctiesFincgDtls(self):
		return self._SctiesFincgDtls

	@SctiesFincgDtls.setter
	def SctiesFincgDtls(self, value):
		self._SctiesFincgDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgDtls', SecuritiesFinancingTransactionDetails50, False)

	@SctiesFincgDtls.deleter
	def SctiesFincgDtls(self):
		del self._SctiesFincgDtls
		self._SctiesFincgDtls = base_types.UninitialisedField(self, 'SctiesFincgDtls', SecuritiesFinancingTransactionDetails50, False)

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
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection92, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection92, False)

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if value is not None else base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails191, False)

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails191, False)

	@property
	def SttlmTpAndAddtlParams(self):
		return self._SttlmTpAndAddtlParams

	@SttlmTpAndAddtlParams.setter
	def SttlmTpAndAddtlParams(self, value):
		self._SttlmTpAndAddtlParams = value if value is not None else base_types.UninitialisedField(self, 'SttlmTpAndAddtlParams', SettlementTypeAndAdditionalParameters15, False)

	@SttlmTpAndAddtlParams.deleter
	def SttlmTpAndAddtlParams(self):
		del self._SttlmTpAndAddtlParams
		self._SttlmTpAndAddtlParams = base_types.UninitialisedField(self, 'SttlmTpAndAddtlParams', SettlementTypeAndAdditionalParameters15, False)

	@property
	def TradDtls(self):
		return self._TradDtls

	@TradDtls.setter
	def TradDtls(self, value):
		self._TradDtls = value if value is not None else base_types.UninitialisedField(self, 'TradDtls', SecuritiesTradeDetails126, False)

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = base_types.UninitialisedField(self, 'TradDtls', SecuritiesTradeDetails126, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', RestrictedFINXMax16Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', RestrictedFINXMax16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshPties', type=CashParties40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyMktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties105, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes122, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrBizPties', type=OtherParties37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount106, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties105, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgDtls', type=SecuritiesFinancingTransactionDetails50, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection92, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails191, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTpAndAddtlParams', type=SettlementTypeAndAdditionalParameters15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails126, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
	))