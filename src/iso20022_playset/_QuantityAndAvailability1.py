from . import base_types
from ._YesNoIndicator import YesNoIndicator
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice

class QuantityAndAvailability1(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_AvlbtyInd"]
	@property
	def AvlbtyInd(self):
		return self._AvlbtyInd

	@AvlbtyInd.setter
	def AvlbtyInd(self, value):
		self._AvlbtyInd = value if type(value) != base_types.auto else self.make_default("AvlbtyInd")

	@AvlbtyInd.deleter
	def AvlbtyInd(self):
		del self._AvlbtyInd
		self._AvlbtyInd = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AvlbtyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
	))

