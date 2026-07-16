# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection66
from . import QuantityAndAccount105
from . import SecuritiesFinancingTransactionDetails48
from . import SecuritiesTradeDetails103
from . import SecurityIdentification20
from . import SettlementDetails172
from . import SettlementParties107
from . import SupplementaryData1
from . import TransactionTypeAndAdditionalParameters20

class SecuritiesFinancingModificationInstruction002V08(base_types._BaseFieldType):

	__slots__ = ["_DlvrgSttlmPties", "_FinInstrmId", "_OpngSttlmAmt", "_QtyAndAcctDtls", "_RcvgSttlmPties", "_SctiesFincgAddtlDtls", "_SplmtryData", "_SttlmParams", "_TradDtls", "_TxTpAndModAddtlParams"]
	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties107, False)

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = base_types.UninitialisedField(self, 'DlvrgSttlmPties', SettlementParties107, False)

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
	def OpngSttlmAmt(self):
		return self._OpngSttlmAmt

	@OpngSttlmAmt.setter
	def OpngSttlmAmt(self, value):
		self._OpngSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'OpngSttlmAmt', AmountAndDirection66, False)

	@OpngSttlmAmt.deleter
	def OpngSttlmAmt(self):
		del self._OpngSttlmAmt
		self._OpngSttlmAmt = base_types.UninitialisedField(self, 'OpngSttlmAmt', AmountAndDirection66, False)

	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount105, False)

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = base_types.UninitialisedField(self, 'QtyAndAcctDtls', QuantityAndAccount105, False)

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties107, False)

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = base_types.UninitialisedField(self, 'RcvgSttlmPties', SettlementParties107, False)

	@property
	def SctiesFincgAddtlDtls(self):
		return self._SctiesFincgAddtlDtls

	@SctiesFincgAddtlDtls.setter
	def SctiesFincgAddtlDtls(self, value):
		self._SctiesFincgAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgAddtlDtls', SecuritiesFinancingTransactionDetails48, False)

	@SctiesFincgAddtlDtls.deleter
	def SctiesFincgAddtlDtls(self):
		del self._SctiesFincgAddtlDtls
		self._SctiesFincgAddtlDtls = base_types.UninitialisedField(self, 'SctiesFincgAddtlDtls', SecuritiesFinancingTransactionDetails48, False)

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
		self._SttlmParams = value if value is not None else base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails172, False)

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = base_types.UninitialisedField(self, 'SttlmParams', SettlementDetails172, False)

	@property
	def TradDtls(self):
		return self._TradDtls

	@TradDtls.setter
	def TradDtls(self, value):
		self._TradDtls = value if value is not None else base_types.UninitialisedField(self, 'TradDtls', SecuritiesTradeDetails103, False)

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = base_types.UninitialisedField(self, 'TradDtls', SecuritiesTradeDetails103, False)

	@property
	def TxTpAndModAddtlParams(self):
		return self._TxTpAndModAddtlParams

	@TxTpAndModAddtlParams.setter
	def TxTpAndModAddtlParams(self, value):
		self._TxTpAndModAddtlParams = value if value is not None else base_types.UninitialisedField(self, 'TxTpAndModAddtlParams', TransactionTypeAndAdditionalParameters20, False)

	@TxTpAndModAddtlParams.deleter
	def TxTpAndModAddtlParams(self):
		del self._TxTpAndModAddtlParams
		self._TxTpAndModAddtlParams = base_types.UninitialisedField(self, 'TxTpAndModAddtlParams', TransactionTypeAndAdditionalParameters20, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties107, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngSttlmAmt', type=AmountAndDirection66, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount105, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties107, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgAddtlDtls', type=SecuritiesFinancingTransactionDetails48, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails172, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails103, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTpAndModAddtlParams', type=TransactionTypeAndAdditionalParameters20, min=1, max=1, mutex_group=None, array=False),
	))