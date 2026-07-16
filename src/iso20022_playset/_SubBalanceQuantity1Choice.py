# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantityChoice
from . import GenericIdentification6
from . import QuantityAndAvailability

class SubBalanceQuantity1Choice(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_QtyAndAvlbty", "_QtyAsDSS"]
	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantityChoice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantityChoice, False)

	@property
	def QtyAndAvlbty(self):
		return self._QtyAndAvlbty

	@QtyAndAvlbty.setter
	def QtyAndAvlbty(self, value):
		self._QtyAndAvlbty = value if value is not None else base_types.UninitialisedField(self, 'QtyAndAvlbty', QuantityAndAvailability, False)

	@QtyAndAvlbty.deleter
	def QtyAndAvlbty(self):
		del self._QtyAndAvlbty
		self._QtyAndAvlbty = base_types.UninitialisedField(self, 'QtyAndAvlbty', QuantityAndAvailability, False)

	@property
	def QtyAsDSS(self):
		return self._QtyAsDSS

	@QtyAsDSS.setter
	def QtyAsDSS(self, value):
		self._QtyAsDSS = value if value is not None else base_types.UninitialisedField(self, 'QtyAsDSS', GenericIdentification6, False)

	@QtyAsDSS.deleter
	def QtyAsDSS(self):
		del self._QtyAsDSS
		self._QtyAsDSS = base_types.UninitialisedField(self, 'QtyAsDSS', GenericIdentification6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantityChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyAndAvlbty', type=QuantityAndAvailability, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyAsDSS', type=GenericIdentification6, min=0, max=1, mutex_group=1, array=False),
	))