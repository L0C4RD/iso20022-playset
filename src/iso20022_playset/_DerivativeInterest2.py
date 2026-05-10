from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class DerivativeInterest2(base_types._BaseFieldType):

	__slots__ = ["_OthrNtnlCcy"]
	@property
	def OthrNtnlCcy(self):
		return self._OthrNtnlCcy

	@OthrNtnlCcy.setter
	def OthrNtnlCcy(self, value):
		self._OthrNtnlCcy = value if type(value) != base_types.auto else self.make_default("OthrNtnlCcy")

	@OthrNtnlCcy.deleter
	def OthrNtnlCcy(self):
		del self._OthrNtnlCcy
		self._OthrNtnlCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrNtnlCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))

