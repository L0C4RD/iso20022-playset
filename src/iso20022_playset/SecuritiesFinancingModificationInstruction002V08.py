from . import base_types
from .SecurityIdentification20 import SecurityIdentification20
from .SettlementParties107 import SettlementParties107
from .AmountAndDirection66 import AmountAndDirection66
from .SettlementDetails172 import SettlementDetails172
from .QuantityAndAccount105 import QuantityAndAccount105
from .TransactionTypeAndAdditionalParameters20 import TransactionTypeAndAdditionalParameters20
from .SecuritiesTradeDetails103 import SecuritiesTradeDetails103
from .SecuritiesFinancingTransactionDetails48 import SecuritiesFinancingTransactionDetails48
from .SupplementaryData1 import SupplementaryData1

class SecuritiesFinancingModificationInstruction002V08(base_types._BaseFieldType):

	__slots__ = ["_OpngSttlmAmt", "_SctiesFincgAddtlDtls", "_RcvgSttlmPties", "_TxTpAndModAddtlParams", "_TradDtls", "_DlvrgSttlmPties", "_FinInstrmId", "_SplmtryData", "_QtyAndAcctDtls", "_SttlmParams"]
	@property
	def OpngSttlmAmt(self):
		return self._OpngSttlmAmt

	@OpngSttlmAmt.setter
	def OpngSttlmAmt(self, value):
		self._OpngSttlmAmt = value if type(value) != auto else self.make_default("OpngSttlmAmt")

	@OpngSttlmAmt.deleter
	def OpngSttlmAmt(self):
		del self._OpngSttlmAmt
		self._OpngSttlmAmt = None

	@property
	def SctiesFincgAddtlDtls(self):
		return self._SctiesFincgAddtlDtls

	@SctiesFincgAddtlDtls.setter
	def SctiesFincgAddtlDtls(self, value):
		self._SctiesFincgAddtlDtls = value if type(value) != auto else self.make_default("SctiesFincgAddtlDtls")

	@SctiesFincgAddtlDtls.deleter
	def SctiesFincgAddtlDtls(self):
		del self._SctiesFincgAddtlDtls
		self._SctiesFincgAddtlDtls = None

	@property
	def RcvgSttlmPties(self):
		return self._RcvgSttlmPties

	@RcvgSttlmPties.setter
	def RcvgSttlmPties(self, value):
		self._RcvgSttlmPties = value if type(value) != auto else self.make_default("RcvgSttlmPties")

	@RcvgSttlmPties.deleter
	def RcvgSttlmPties(self):
		del self._RcvgSttlmPties
		self._RcvgSttlmPties = None

	@property
	def TxTpAndModAddtlParams(self):
		return self._TxTpAndModAddtlParams

	@TxTpAndModAddtlParams.setter
	def TxTpAndModAddtlParams(self, value):
		self._TxTpAndModAddtlParams = value if type(value) != auto else self.make_default("TxTpAndModAddtlParams")

	@TxTpAndModAddtlParams.deleter
	def TxTpAndModAddtlParams(self):
		del self._TxTpAndModAddtlParams
		self._TxTpAndModAddtlParams = None

	@property
	def TradDtls(self):
		return self._TradDtls

	@TradDtls.setter
	def TradDtls(self, value):
		self._TradDtls = value if type(value) != auto else self.make_default("TradDtls")

	@TradDtls.deleter
	def TradDtls(self):
		del self._TradDtls
		self._TradDtls = None

	@property
	def DlvrgSttlmPties(self):
		return self._DlvrgSttlmPties

	@DlvrgSttlmPties.setter
	def DlvrgSttlmPties(self, value):
		self._DlvrgSttlmPties = value if type(value) != auto else self.make_default("DlvrgSttlmPties")

	@DlvrgSttlmPties.deleter
	def DlvrgSttlmPties(self):
		del self._DlvrgSttlmPties
		self._DlvrgSttlmPties = None

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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def QtyAndAcctDtls(self):
		return self._QtyAndAcctDtls

	@QtyAndAcctDtls.setter
	def QtyAndAcctDtls(self, value):
		self._QtyAndAcctDtls = value if type(value) != auto else self.make_default("QtyAndAcctDtls")

	@QtyAndAcctDtls.deleter
	def QtyAndAcctDtls(self):
		del self._QtyAndAcctDtls
		self._QtyAndAcctDtls = None

	@property
	def SttlmParams(self):
		return self._SttlmParams

	@SttlmParams.setter
	def SttlmParams(self, value):
		self._SttlmParams = value if type(value) != auto else self.make_default("SttlmParams")

	@SttlmParams.deleter
	def SttlmParams(self):
		del self._SttlmParams
		self._SttlmParams = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OpngSttlmAmt', type=AmountAndDirection66, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesFincgAddtlDtls', type=SecuritiesFinancingTransactionDetails48, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgSttlmPties', type=SettlementParties107, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTpAndModAddtlParams', type=TransactionTypeAndAdditionalParameters20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtls', type=SecuritiesTradeDetails103, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrgSttlmPties', type=SettlementParties107, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QtyAndAcctDtls', type=QuantityAndAccount105, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmParams', type=SettlementDetails172, min=0, max=1, mutex_group=None, array=False),
	))

