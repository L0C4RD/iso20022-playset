# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DecimalNumber import DecimalNumber
from ._FromToQuantityRange1 import FromToQuantityRange1
from ._QuantityRangeBoundary1 import QuantityRangeBoundary1

class QuantityRange1Choice(base_types._BaseFieldType):

	__slots__ = ["_EQQty", "_FrQty", "_FrToQty", "_NEQQty", "_ToQty"]
	@property
	def EQQty(self):
		return self._EQQty

	@EQQty.setter
	def EQQty(self, value):
		self._EQQty = value if type(value) != base_types.auto else self.make_default("EQQty")

	@EQQty.deleter
	def EQQty(self):
		del self._EQQty
		self._EQQty = None

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
	def FrToQty(self):
		return self._FrToQty

	@FrToQty.setter
	def FrToQty(self, value):
		self._FrToQty = value if type(value) != base_types.auto else self.make_default("FrToQty")

	@FrToQty.deleter
	def FrToQty(self):
		del self._FrToQty
		self._FrToQty = None

	@property
	def NEQQty(self):
		return self._NEQQty

	@NEQQty.setter
	def NEQQty(self, value):
		self._NEQQty = value if type(value) != base_types.auto else self.make_default("NEQQty")

	@NEQQty.deleter
	def NEQQty(self):
		del self._NEQQty
		self._NEQQty = None

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
		base_types.FieldEntry(name='EQQty', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrQty', type=QuantityRangeBoundary1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrToQty', type=FromToQuantityRange1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NEQQty', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToQty', type=QuantityRangeBoundary1, min=0, max=1, mutex_group=1, array=False),
	))