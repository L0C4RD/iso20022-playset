# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import QuantityRangeBoundary1

class FromToQuantityRange1(base_types._BaseFieldType):

	__slots__ = ["_FrQty", "_ToQty"]
	@property
	def FrQty(self):
		return self._FrQty

	@FrQty.setter
	def FrQty(self, value):
		self._FrQty = value if value is not None else base_types.UninitialisedField(self, 'FrQty', QuantityRangeBoundary1, False)

	@FrQty.deleter
	def FrQty(self):
		del self._FrQty
		self._FrQty = base_types.UninitialisedField(self, 'FrQty', QuantityRangeBoundary1, False)

	@property
	def ToQty(self):
		return self._ToQty

	@ToQty.setter
	def ToQty(self, value):
		self._ToQty = value if value is not None else base_types.UninitialisedField(self, 'ToQty', QuantityRangeBoundary1, False)

	@ToQty.deleter
	def ToQty(self):
		del self._ToQty
		self._ToQty = base_types.UninitialisedField(self, 'ToQty', QuantityRangeBoundary1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrQty', type=QuantityRangeBoundary1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToQty', type=QuantityRangeBoundary1, min=1, max=1, mutex_group=None, array=False),
	))