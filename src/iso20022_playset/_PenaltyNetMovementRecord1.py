# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection5
from . import FinancialInstrumentQuantity1Choice
from . import Number
from . import SecuritiesAccount19
from . import TradeTransactionCondition5Choice

class PenaltyNetMovementRecord1(base_types._BaseFieldType):

	__slots__ = ["_NbOfNtries", "_SctiesShrtfll", "_SfkpgAcct", "_ShrtfllValtn", "_TradTxCond"]
	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if value is not None else base_types.UninitialisedField(self, 'NbOfNtries', Number, False)

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = base_types.UninitialisedField(self, 'NbOfNtries', Number, False)

	@property
	def SctiesShrtfll(self):
		return self._SctiesShrtfll

	@SctiesShrtfll.setter
	def SctiesShrtfll(self, value):
		self._SctiesShrtfll = value if value is not None else base_types.UninitialisedField(self, 'SctiesShrtfll', FinancialInstrumentQuantity1Choice, False)

	@SctiesShrtfll.deleter
	def SctiesShrtfll(self):
		del self._SctiesShrtfll
		self._SctiesShrtfll = base_types.UninitialisedField(self, 'SctiesShrtfll', FinancialInstrumentQuantity1Choice, False)

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = base_types.UninitialisedField(self, 'SfkpgAcct', SecuritiesAccount19, False)

	@property
	def ShrtfllValtn(self):
		return self._ShrtfllValtn

	@ShrtfllValtn.setter
	def ShrtfllValtn(self, value):
		self._ShrtfllValtn = value if value is not None else base_types.UninitialisedField(self, 'ShrtfllValtn', AmountAndDirection5, False)

	@ShrtfllValtn.deleter
	def ShrtfllValtn(self):
		del self._ShrtfllValtn
		self._ShrtfllValtn = base_types.UninitialisedField(self, 'ShrtfllValtn', AmountAndDirection5, False)

	@property
	def TradTxCond(self):
		return self._TradTxCond

	@TradTxCond.setter
	def TradTxCond(self, value):
		self._TradTxCond = value if value is not None else base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition5Choice, True)

	@TradTxCond.deleter
	def TradTxCond(self):
		del self._TradTxCond
		self._TradTxCond = base_types.UninitialisedField(self, 'TradTxCond', TradeTransactionCondition5Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfNtries', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesShrtfll', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtfllValtn', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTxCond', type=TradeTransactionCondition5Choice, min=0, max=None, mutex_group=None, array=True),
	))