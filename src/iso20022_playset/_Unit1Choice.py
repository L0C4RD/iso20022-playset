# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import Max30DecimalNumber

class Unit1Choice(base_types._BaseFieldType):

	__slots__ = ["_DgtlTknUnit", "_UnitsNb"]
	@property
	def DgtlTknUnit(self):
		return self._DgtlTknUnit

	@DgtlTknUnit.setter
	def DgtlTknUnit(self, value):
		self._DgtlTknUnit = value if value is not None else base_types.UninitialisedField(self, 'DgtlTknUnit', Max30DecimalNumber, False)

	@DgtlTknUnit.deleter
	def DgtlTknUnit(self):
		del self._DgtlTknUnit
		self._DgtlTknUnit = base_types.UninitialisedField(self, 'DgtlTknUnit', Max30DecimalNumber, False)

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if value is not None else base_types.UninitialisedField(self, 'UnitsNb', DecimalNumber, False)

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = base_types.UninitialisedField(self, 'UnitsNb', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlTknUnit', type=Max30DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))