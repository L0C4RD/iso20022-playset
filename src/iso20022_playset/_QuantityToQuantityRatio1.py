# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber

class QuantityToQuantityRatio1(base_types._BaseFieldType):

	__slots__ = ["_Qty1", "_Qty2"]
	@property
	def Qty1(self):
		return self._Qty1

	@Qty1.setter
	def Qty1(self, value):
		self._Qty1 = value if value is not None else base_types.UninitialisedField(self, 'Qty1', DecimalNumber, False)

	@Qty1.deleter
	def Qty1(self):
		del self._Qty1
		self._Qty1 = base_types.UninitialisedField(self, 'Qty1', DecimalNumber, False)

	@property
	def Qty2(self):
		return self._Qty2

	@Qty2.setter
	def Qty2(self, value):
		self._Qty2 = value if value is not None else base_types.UninitialisedField(self, 'Qty2', DecimalNumber, False)

	@Qty2.deleter
	def Qty2(self):
		del self._Qty2
		self._Qty2 = base_types.UninitialisedField(self, 'Qty2', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty1', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty2', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
	))