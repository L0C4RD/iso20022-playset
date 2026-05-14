# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._PercentageRate import PercentageRate

class PriceRateOrAmount6Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtWthCcy", "_Rate"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def AmtWthCcy(self):
		return self._AmtWthCcy

	@AmtWthCcy.setter
	def AmtWthCcy(self, value):
		self._AmtWthCcy = value if type(value) != base_types.auto else self.make_default("AmtWthCcy")

	@AmtWthCcy.deleter
	def AmtWthCcy(self):
		del self._AmtWthCcy
		self._AmtWthCcy = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtWthCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))