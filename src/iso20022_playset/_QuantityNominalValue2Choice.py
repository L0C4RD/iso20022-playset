# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection53
from . import DecimalNumber

class QuantityNominalValue2Choice(base_types._BaseFieldType):

	__slots__ = ["_NmnlVal", "_Qty"]
	@property
	def NmnlVal(self):
		return self._NmnlVal

	@NmnlVal.setter
	def NmnlVal(self, value):
		self._NmnlVal = value if value is not None else base_types.UninitialisedField(self, 'NmnlVal', AmountAndDirection53, False)

	@NmnlVal.deleter
	def NmnlVal(self):
		del self._NmnlVal
		self._NmnlVal = base_types.UninitialisedField(self, 'NmnlVal', AmountAndDirection53, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', DecimalNumber, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NmnlVal', type=AmountAndDirection53, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
	))