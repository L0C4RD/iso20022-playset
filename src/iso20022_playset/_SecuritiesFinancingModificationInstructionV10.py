# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection49
from . import DigitalPaymentSettlement2
from . import QuantityAndAccount119
from . import SecuritiesFinancingTransactionDetails58
from . import SecuritiesTradeDetails100
from . import SecurityIdentification19
from . import SettlementDetails226
from . import SettlementParties127
from . import SupplementaryData1
from . import TransactionTypeAndAdditionalParameters23

class SecuritiesFinancingModificationInstructionV10(base_types._BaseFieldType):

	__slots__ = ["_DlvrgSttlmPties", "_FinInstrmId", "_OpngDgtlSttlmAmt", "_OpngSttlmAmt", "_QtyAndAcctDtls", "_RcvgSttlmPties", "_SctiesFincgAddtlDtls", "_SplmtryData", "_SttlmParams", "_TradDtls", "_TxTpAndModAddtlParams"]
	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties127, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties127, False)

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
	def OpngDgtlSttlmAmt(self):
		return self._OpngDgtlSttlmAmt

	@OpngDgtlSttlmAmt.setter
	def OpngDgtlSttlmAmt(self, value):
		self._OpngDgtlSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'OpngDgtlSttlmAmt', DigitalPaymentSettlement2, False)

	@OpngDgtlSttlmAmt.deleter
	def OpngDgtlSttlmAmt(self):
		del self._OpngDgtlSttlmAmt
		self._OpngDgtlSttlmAmt = base_types.UninitialisedField(self, 'OpngDgtlSttlmAmt', DigitalPaymentSettlement2, False)

	@property
	def OpngSttlmAmt(self):
		return self._OpngSttlmAmt

	@OpngSttlmAmt.setter
	def OpngSttlmAmt(self, value):
		self._OpngSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'OpngSttlmAmt', AmountAndDirection49, False)

	@OpngSttlmAmt.deleter
	def OpngSttlmAmt(self):
		del self._OpngSttlmAmt
		self._OpngSttlmAmt = base_types.UninitialisedField(self, 'OpngSttlmAmt', AmountAndDirection49, False)

	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount119, False)

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount119, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties127, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties127, False)

	@property
	def SctiesFincgAddtlDtls(self):
		return self._SctiesFincgAddtlDtls

	@SctiesFincgAddtlDtls.setter
	def SctiesFincgAddtlDtls(self, value):
		self._SctiesFincgAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgAddtlDtls', SecuritiesFinancingTransactionDetails58, False)

	@SctiesFincgAddtlDtls.deleter
	def SctiesFincgAddtlDtls(self):
		del self._SctiesFincgAddtlDtls
		self._SctiesFincgAddtlDtls = base_types.UninitialisedField(self, 'SctiesFincgAddtlDtls', SecuritiesFinancingTransactionDetails58, False)

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
		self._TradDtls = value if value is not None else base_types.UninitialisedField(self, 'TradDtls', SecuritiesTradeDetails100, False)

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = base_types.UninitialisedField(self, 'TradDtls', SecuritiesTradeDetails100, False)

	@property
	def TxTpAndModAddtlParams(self):
		return self._TxTpAndModAddtlParams

	@TxTpAndModAddtlParams.setter
	def TxTpAndModAddtlParams(self, value):
		self._TxTpAndModAddtlParams = value if value is not None else base_types.UninitialisedField(self, 'TxTpAndModAddtlParams', TransactionTypeAndAdditionalParameters23, False)

	@TxTpAndModAddtlParams.deleter
	def TxTpAndModAddtlParams(self):
		del self._TxTpAndModAddtlParams
		self._TxTpAndModAddtlParams = base_types.UninitialisedField(self, 'TxTpAndModAddtlParams', TransactionTypeAndAdditionalParameters23, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties127, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngDgtlSttlmAmt', type=DigitalPaymentSettlement2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngSttlmAmt', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount119, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties127, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgAddtlDtls', type=SecuritiesFinancingTransactionDetails58, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails226, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTpAndModAddtlParams', type=TransactionTypeAndAdditionalParameters23, min=1, max=1, mutex_group=None, array=False),
	))