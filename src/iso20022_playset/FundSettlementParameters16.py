import base_types
import Max35Text
import TradeTransactionCondition8Choice
import SettlementParties94
import SettlementTransactionCondition30Choice

class FundSettlementParameters16(base_types._BaseFieldType):

	__slots__ = ["_TradTxCond", "_RcvgSdDtls", "_SctiesSttlmSysId", "_SttlmTxCond"]
	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if type(value) != auto else self.make_default("TradTxCond")

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = None

	@property
	def RcvgSdDtls(self):
		return self._RcvgSdDtls

	@RcvgSdDtls.setter
	def RcvgSdDtls(self, value):
		self._RcvgSdDtls = value if type(value) != auto else self.make_default("RcvgSdDtls")

	@RcvgSdDtls.deleter
	def RcvgSdDtls(self):
		del self._RcvgSdDtls
		self._RcvgSdDtls = None

	@property
	def SctiesSttlmSysId(self):
		return self._SctiesSttlmSysId

	@SctiesSttlmSysId.setter
	def SctiesSttlmSysId(self, value):
		self._SctiesSttlmSysId = value if type(value) != auto else self.make_default("SctiesSttlmSysId")

	@SctiesSttlmSysId.deleter
	def SctiesSttlmSysId(self):
		del self._SctiesSttlmSysId
		self._SctiesSttlmSysId = None

	@property
	def SttlmTxCond(self):
		return self._SttlmTxCond

	@SttlmTxCond.setter
	def SttlmTxCond(self, value):
		self._SttlmTxCond = value if type(value) != auto else self.make_default("SttlmTxCond")

	@SttlmTxCond.deleter
	def SttlmTxCond(self):
		del self._SttlmTxCond
		self._SttlmTxCond = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition8Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcvgSdDtls', type=SettlementParties94, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSttlmSysId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTxCond', type=SettlementTransactionCondition30Choice, min=0, max=None, mutex_group=None, array=True),
	))

