from . import base_types
from ._FinancialInstrumentQuantity36Choice import FinancialInstrumentQuantity36Choice
from ._OriginalAndCurrentQuantities4 import OriginalAndCurrentQuantities4

class Quantity54Choice(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_OrgnlAndCurFace"]
	@property
	def OrgnlAndCurFace(self):
		return self._OrgnlAndCurFace

	@OrgnlAndCurFace.setter
	def OrgnlAndCurFace(self, value):
		self._OrgnlAndCurFace = value if type(value) != base_types.auto else self.make_default("OrgnlAndCurFace")

	@OrgnlAndCurFace.deleter
	def OrgnlAndCurFace(self):
		del self._OrgnlAndCurFace
		self._OrgnlAndCurFace = None

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
		base_types.FieldEntry(name='OrgnlAndCurFace', type=OriginalAndCurrentQuantities4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=1, array=False),
	))

