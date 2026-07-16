# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Number

class Absolute1(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_Unit"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', Number, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', Number, False)

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if value is not None else base_types.UninitialisedField(self, 'Unit', Max35Text, False)

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = base_types.UninitialisedField(self, 'Unit', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))