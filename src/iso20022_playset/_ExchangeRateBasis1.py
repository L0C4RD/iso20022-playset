from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode

class ExchangeRateBasis1(base_types._BaseFieldType):

	__slots__ = ["_BaseCcy", "_QtdCcy"]
	@property
	def BaseCcy(self):
		return self._BaseCcy

	@BaseCcy.setter
	def BaseCcy(self, value):
		self._BaseCcy = value if type(value) != base_types.auto else self.make_default("BaseCcy")

	@BaseCcy.deleter
	def BaseCcy(self):
		del self._BaseCcy
		self._BaseCcy = None

	@property
	def QtdCcy(self):
		return self._QtdCcy

	@QtdCcy.setter
	def QtdCcy(self, value):
		self._QtdCcy = value if type(value) != base_types.auto else self.make_default("QtdCcy")

	@QtdCcy.deleter
	def QtdCcy(self):
		del self._QtdCcy
		self._QtdCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BaseCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtdCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))

