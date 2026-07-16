# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import FromToQuantityRange1
from . import QuantityRangeBoundary1

class QuantityRange1Choice(base_types._BaseFieldType):

	__slots__ = ["_EQQty", "_FrQty", "_FrToQty", "_NEQQty", "_ToQty"]
	@property
	def EQQty(self):
		return self._EQQty

	@EQQty.setter
	def EQQty(self, value):
		self._EQQty = value if value is not None else base_types.UninitialisedField(self, 'EQQty', DecimalNumber, False)

	@EQQty.deleter
	def EQQty(self):
		del self._EQQty
		self._EQQty = base_types.UninitialisedField(self, 'EQQty', DecimalNumber, False)

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
	def FrToQty(self):
		return self._FrToQty

	@FrToQty.setter
	def FrToQty(self, value):
		self._FrToQty = value if value is not None else base_types.UninitialisedField(self, 'FrToQty', FromToQuantityRange1, False)

	@FrToQty.deleter
	def FrToQty(self):
		del self._FrToQty
		self._FrToQty = base_types.UninitialisedField(self, 'FrToQty', FromToQuantityRange1, False)

	@property
	def NEQQty(self):
		return self._NEQQty

	@NEQQty.setter
	def NEQQty(self, value):
		self._NEQQty = value if value is not None else base_types.UninitialisedField(self, 'NEQQty', DecimalNumber, False)

	@NEQQty.deleter
	def NEQQty(self):
		del self._NEQQty
		self._NEQQty = base_types.UninitialisedField(self, 'NEQQty', DecimalNumber, False)

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
		base_types.FieldEntry(name='EQQty', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrQty', type=QuantityRangeBoundary1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrToQty', type=FromToQuantityRange1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NEQQty', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToQty', type=QuantityRangeBoundary1, min=0, max=1, mutex_group=1, array=False),
	))