# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LongFraction19DecimalNumber
from . import Max52Text

class Quantity47Choice(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Qty"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max52Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max52Text, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', LongFraction19DecimalNumber, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', LongFraction19DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max52Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))