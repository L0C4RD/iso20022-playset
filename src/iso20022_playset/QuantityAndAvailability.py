from . import base_types
from .YesNoIndicator import YesNoIndicator
from .FinancialInstrumentQuantityChoice import FinancialInstrumentQuantityChoice

class QuantityAndAvailability(base_types._BaseFieldType):

	__slots__ = ["_AvlbtyInd", "_Qty"]
	@property
	def AvlbtyInd(self):
		return self._AvlbtyInd

	@AvlbtyInd.setter
	def AvlbtyInd(self, value):
		self._AvlbtyInd = value if type(value) != auto else self.make_default("AvlbtyInd")

	@AvlbtyInd.deleter
	def AvlbtyInd(self):
		del self._AvlbtyInd
		self._AvlbtyInd = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlbtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantityChoice, min=1, max=1, mutex_group=None, array=False),
	))

