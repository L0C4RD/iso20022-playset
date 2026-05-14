# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class Amount3Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtWthCcy", "_AmtWthtCcy"]
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
	def AmtWthtCcy(self):
		return self._AmtWthtCcy

	@AmtWthtCcy.setter
	def AmtWthtCcy(self, value):
		self._AmtWthtCcy = value if type(value) != base_types.auto else self.make_default("AmtWthtCcy")

	@AmtWthtCcy.deleter
	def AmtWthtCcy(self):
		del self._AmtWthtCcy
		self._AmtWthtCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtWthCcy', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtWthtCcy', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))