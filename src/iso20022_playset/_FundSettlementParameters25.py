from . import base_types
from ._Max35Text import Max35Text
from ._SettlementParties131 import SettlementParties131
from ._SettlementTransactionCondition30Choice import SettlementTransactionCondition30Choice
from ._TradeTransactionCondition8Choice import TradeTransactionCondition8Choice

class FundSettlementParameters25(base_types._BaseFieldType):

	__slots__ = ["_RcvgSdDtls", "_SctiesSttlmSysId", "_SttlmTxCond", "_TradTxCond"]
	@property
	def RcvgSdDtls(self):
		return self._RcvgSdDtls

	@RcvgSdDtls.setter
	def RcvgSdDtls(self, value):
		self._RcvgSdDtls = value if type(value) != base_types.auto else self.make_default("RcvgSdDtls")

	@RcvgSdDtls.deleter
	def RcvgSdDtls(self):
		del self._RcvgSdDtls
		self._RcvgSdDtls = None

	@property
	def SctiesSttlmSysId(self):
		return self._SctiesSttlmSysId

	@SctiesSttlmSysId.setter
	def SctiesSttlmSysId(self, value):
		self._SctiesSttlmSysId = value if type(value) != base_types.auto else self.make_default("SctiesSttlmSysId")

	@SctiesSttlmSysId.deleter
	def SctiesSttlmSysId(self):
		del self._SctiesSttlmSysId
		self._SctiesSttlmSysId = None

	@property
	def SttlmTxCond(self):
		return self._SttlmTxCond

	@SttlmTxCond.setter
	def SttlmTxCond(self, value):
		self._SttlmTxCond = value if type(value) != base_types.auto else self.make_default("SttlmTxCond")

	@SttlmTxCond.deleter
	def SttlmTxCond(self):
		del self._SttlmTxCond
		self._SttlmTxCond = None

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if type(value) != base_types.auto else self.make_default("TradTxCond")

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcvgSdDtls', type=SettlementParties131, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSttlmSysId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxCond', type=SettlementTransactionCondition30Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition8Choice, min=0, max=None, mutex_group=None, array=True),
	))

