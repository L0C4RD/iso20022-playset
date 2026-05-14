from . import base_types
from ._AmountAndDirection5 import AmountAndDirection5
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from ._Number import Number
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._TradeTransactionCondition5Choice import TradeTransactionCondition5Choice

class PenaltyNetMovementRecord1(base_types._BaseFieldType):

	__slots__ = ["_NbOfNtries", "_SctiesShrtfll", "_SfkpgAcct", "_ShrtfllValtn", "_TradTxCond"]
	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if type(value) != base_types.auto else self.make_default("NbOfNtries")

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = None

	@property
	def SctiesShrtfll(self):
		return self._SctiesShrtfll

	@SctiesShrtfll.setter
	def SctiesShrtfll(self, value):
		self._SctiesShrtfll = value if type(value) != base_types.auto else self.make_default("SctiesShrtfll")

	@SctiesShrtfll.deleter
	def SctiesShrtfll(self):
		del self._SctiesShrtfll
		self._SctiesShrtfll = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def ShrtfllValtn(self):
		return self._ShrtfllValtn

	@ShrtfllValtn.setter
	def ShrtfllValtn(self, value):
		self._ShrtfllValtn = value if type(value) != base_types.auto else self.make_default("ShrtfllValtn")

	@ShrtfllValtn.deleter
	def ShrtfllValtn(self):
		del self._ShrtfllValtn
		self._ShrtfllValtn = None

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
		base_types.FieldEntry(name='NbOfNtries', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesShrtfll', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtfllValtn', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition5Choice, min=0, max=None, mutex_group=None, array=True),
	))

