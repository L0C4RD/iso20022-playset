# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity33Choice
from . import ProprietaryQuantity8

class Quantity48Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryQty", "_Qty"]
	@property
	def PrtryQty(self):
		return self._PrtryQty

	@PrtryQty.setter
	def PrtryQty(self, value):
		self._PrtryQty = value if value is not None else base_types.UninitialisedField(self, 'PrtryQty', ProprietaryQuantity8, False)

	@PrtryQty.deleter
	def PrtryQty(self):
		del self._PrtryQty
		self._PrtryQty = base_types.UninitialisedField(self, 'PrtryQty', ProprietaryQuantity8, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity33Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantity33Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryQty', type=ProprietaryQuantity8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=1, array=False),
	))