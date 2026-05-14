# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountAndDirection49 import AmountAndDirection49
from ._QuantityAndAccount119 import QuantityAndAccount119
from ._SecuritiesFinancingTransactionDetails58 import SecuritiesFinancingTransactionDetails58
from ._SecuritiesTradeDetails100 import SecuritiesTradeDetails100
from ._SecurityIdentification19 import SecurityIdentification19
from ._SettlementDetails148 import SettlementDetails148
from ._SettlementParties127 import SettlementParties127
from ._SupplementaryData1 import SupplementaryData1
from ._TransactionTypeAndAdditionalParameters23 import TransactionTypeAndAdditionalParameters23

class SecuritiesFinancingModificationInstructionV09(base_types._BaseFieldType):

	__slots__ = ["_DlvrgSttlmPties", "_FinInstrmId", "_OpngSttlmAmt", "_QtyAndAcctDtls", "_RcvgSttlmPties", "_SctiesFincgAddtlDtls", "_SplmtryData", "_SttlmParams", "_TradDtls", "_TxTpAndModAddtlParams"]
	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if type(value) != base_types.auto else self.make_default("DlvrgSttlmPties")

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def OpngSttlmAmt(self):
		return self._OpngSttlmAmt

	@OpngSttlmAmt.setter
	def OpngSttlmAmt(self, value):
		self._OpngSttlmAmt = value if type(value) != base_types.auto else self.make_default("OpngSttlmAmt")

	@OpngSttlmAmt.deleter
	def OpngSttlmAmt(self):
		del self._OpngSttlmAmt
		self._OpngSttlmAmt = None

	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if type(value) != base_types.auto else self.make_default("QtyAndAcctDtls")

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = None

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if type(value) != base_types.auto else self.make_default("RcvgSttlmPties")

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = None

	@property
	def SctiesFincgAddtlDtls(self):
		return self._SctiesFincgAddtlDtls

	@SctiesFincgAddtlDtls.setter
	def SctiesFincgAddtlDtls(self, value):
		self._SctiesFincgAddtlDtls = value if type(value) != base_types.auto else self.make_default("SctiesFincgAddtlDtls")

	@SctiesFincgAddtlDtls.deleter
	def SctiesFincgAddtlDtls(self):
		del self._SctiesFincgAddtlDtls
		self._SctiesFincgAddtlDtls = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if type(value) != base_types.auto else self.make_default("SttlmParams")

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = None

	@property
	def TradDtls(self):
		return self._TradDtls

	@TradDtls.setter
	def TradDtls(self, value):
		self._TradDtls = value if type(value) != base_types.auto else self.make_default("TradDtls")

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = None

	@property
	def TxTpAndModAddtlParams(self):
		return self._TxTpAndModAddtlParams

	@TxTpAndModAddtlParams.setter
	def TxTpAndModAddtlParams(self, value):
		self._TxTpAndModAddtlParams = value if type(value) != base_types.auto else self.make_default("TxTpAndModAddtlParams")

	@TxTpAndModAddtlParams.deleter
	def TxTpAndModAddtlParams(self):
		del self._TxTpAndModAddtlParams
		self._TxTpAndModAddtlParams = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties127, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngSttlmAmt', type=AmountAndDirection49, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount119, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties127, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgAddtlDtls', type=SecuritiesFinancingTransactionDetails58, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails148, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTpAndModAddtlParams', type=TransactionTypeAndAdditionalParameters23, min=1, max=1, mutex_group=None, array=False),
	))