from . import base_types
from ._PriceValuation4 import PriceValuation4

class PriceReport3(base_types._BaseFieldType):

	__slots__ = ["_PricValtnDtls"]
	@property
	def PricValtnDtls(self):
		return self._PricValtnDtls

	@PricValtnDtls.setter
	def PricValtnDtls(self, value):
		self._PricValtnDtls = value if type(value) != base_types.auto else self.make_default("PricValtnDtls")

	@PricValtnDtls.deleter
	def PricValtnDtls(self):
		del self._PricValtnDtls
		self._PricValtnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricValtnDtls', type=PriceValuation4, min=1, max=None, mutex_group=None, array=True),
	))

