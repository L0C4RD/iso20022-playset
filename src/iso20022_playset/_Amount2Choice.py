# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ImpliedCurrencyAndAmount

class Amount2Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtWthCcy", "_AmtWthtCcy"]
	@property
	def AmtWthCcy(self):
		return self._AmtWthCcy

	@AmtWthCcy.setter
	def AmtWthCcy(self, value):
		self._AmtWthCcy = value if value is not None else base_types.UninitialisedField(self, 'AmtWthCcy', ActiveCurrencyAndAmount, False)

	@AmtWthCcy.deleter
	def AmtWthCcy(self):
		del self._AmtWthCcy
		self._AmtWthCcy = base_types.UninitialisedField(self, 'AmtWthCcy', ActiveCurrencyAndAmount, False)

	@property
	def AmtWthtCcy(self):
		return self._AmtWthtCcy

	@AmtWthtCcy.setter
	def AmtWthtCcy(self, value):
		self._AmtWthtCcy = value if value is not None else base_types.UninitialisedField(self, 'AmtWthtCcy', ImpliedCurrencyAndAmount, False)

	@AmtWthtCcy.deleter
	def AmtWthtCcy(self):
		del self._AmtWthtCcy
		self._AmtWthtCcy = base_types.UninitialisedField(self, 'AmtWthtCcy', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtWthCcy', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtWthtCcy', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))