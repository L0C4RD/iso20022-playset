# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity36Choice
from . import GenericIdentification144
from . import QuantityAndAvailability4

class SubBalanceQuantity9Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_Qty", "_QtyAndAvlbty"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification144, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification144, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity36Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity36Choice, False)

	@property
	def QtyAndAvlbty(self):
		return self._QtyAndAvlbty

	@QtyAndAvlbty.setter
	def QtyAndAvlbty(self, value):
		self._QtyAndAvlbty = value if value is not None else base_types.UninitialisedField(self, 'QtyAndAvlbty', QuantityAndAvailability4, False)

	@QtyAndAvlbty.deleter
	def QtyAndAvlbty(self):
		del self._QtyAndAvlbty
		self._QtyAndAvlbty = base_types.UninitialisedField(self, 'QtyAndAvlbty', QuantityAndAvailability4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification144, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyAndAvlbty', type=QuantityAndAvailability4, min=0, max=1, mutex_group=1, array=False),
	))