# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DecimalNumber import DecimalNumber

class FromToQuantityRange2(base_types._BaseFieldType):

	__slots__ = ["_FrQty", "_ToQty"]
	@property
	def FrQty(self):
		return self._FrQty

	@FrQty.setter
	def FrQty(self, value):
		self._FrQty = value if type(value) != base_types.auto else self.make_default("FrQty")

	@FrQty.deleter
	def FrQty(self):
		del self._FrQty
		self._FrQty = None

	@property
	def ToQty(self):
		return self._ToQty

	@ToQty.setter
	def ToQty(self, value):
		self._ToQty = value if type(value) != base_types.auto else self.make_default("ToQty")

	@ToQty.deleter
	def ToQty(self):
		del self._ToQty
		self._ToQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrQty', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToQty', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))