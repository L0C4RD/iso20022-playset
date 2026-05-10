from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount

class Amount2Choice(base_types._BaseFieldType):

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
		base_types.FieldEntry(name='AmtWthCcy', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtWthtCcy', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))

