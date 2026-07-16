# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity36Choice

class PairedOrTurnedQuantity6Choice(base_types._BaseFieldType):

	__slots__ = ["_PairdOffQty", "_TrndQty"]
	@property
	def PairdOffQty(self):
		return self._PairdOffQty

	@PairdOffQty.setter
	def PairdOffQty(self, value):
		self._PairdOffQty = value if value is not None else base_types.UninitialisedField(self, 'PairdOffQty', FinancialInstrumentQuantity36Choice, False)

	@PairdOffQty.deleter
	def PairdOffQty(self):
		del self._PairdOffQty
		self._PairdOffQty = base_types.UninitialisedField(self, 'PairdOffQty', FinancialInstrumentQuantity36Choice, False)

	@property
	def TrndQty(self):
		return self._TrndQty

	@TrndQty.setter
	def TrndQty(self, value):
		self._TrndQty = value if value is not None else base_types.UninitialisedField(self, 'TrndQty', FinancialInstrumentQuantity36Choice, False)

	@TrndQty.deleter
	def TrndQty(self):
		del self._TrndQty
		self._TrndQty = base_types.UninitialisedField(self, 'TrndQty', FinancialInstrumentQuantity36Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PairdOffQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='TrndQty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=1, array=False),
	))