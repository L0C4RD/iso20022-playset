# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber

class FinancialInstrumentQuantity1(base_types._BaseFieldType):

	__slots__ = ["_Unit"]
	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', DecimalNumber, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Unit', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))