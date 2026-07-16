# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceValuation4

class PriceReport3(base_types._BaseFieldType):

	__slots__ = ["_PricValtnDtls"]
	@property
	def PricValtnDtls(self):
		return self._PricValtnDtls

	@PricValtnDtls.setter
	def PricValtnDtls(self, value):
		self._PricValtnDtls = value if value is not None else base_types.UninitialisedField(self, 'PricValtnDtls', PriceValuation4, True)

	@PricValtnDtls.deleter
	def PricValtnDtls(self):
		del self._PricValtnDtls
		self._PricValtnDtls = base_types.UninitialisedField(self, 'PricValtnDtls', PriceValuation4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricValtnDtls', type=PriceValuation4, min=1, max=None, mutex_group=None, array=True),
	))