# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity33Choice
from . import YesNoIndicator

class QuantityAndAvailability3(base_types._BaseFieldType):

	__slots__ = ["_AvlbtyInd", "_Qty"]
	@property
	def AvlbtyInd(self):
		return self._AvlbtyInd

	@AvlbtyInd.setter
	def AvlbtyInd(self, value):
		self._AvlbtyInd = value if value is not None else base_types.UninitialisedField(self, 'AvlbtyInd', YesNoIndicator, False)

	@AvlbtyInd.deleter
	def AvlbtyInd(self):
		del self._AvlbtyInd
		self._AvlbtyInd = base_types.UninitialisedField(self, 'AvlbtyInd', YesNoIndicator, False)

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
		base_types.FieldEntry(name='AvlbtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
	))