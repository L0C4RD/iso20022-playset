from . import base_types
from .FinancialInstrumentQuantity36Choice import FinancialInstrumentQuantity36Choice
from .OriginalAndCurrentQuantities4 import OriginalAndCurrentQuantities4
from .Quantity1Code import Quantity1Code

class Quantity55Choice(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_OrgnlAndCurFaceAmt", "_Qty"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def OrgnlAndCurFaceAmt(self):
		return self._OrgnlAndCurFaceAmt

	@OrgnlAndCurFaceAmt.setter
	def OrgnlAndCurFaceAmt(self, value):
		self._OrgnlAndCurFaceAmt = value if type(value) != base_types.auto else self.make_default("OrgnlAndCurFaceAmt")

	@OrgnlAndCurFaceAmt.deleter
	def OrgnlAndCurFaceAmt(self):
		del self._OrgnlAndCurFaceAmt
		self._OrgnlAndCurFaceAmt = None

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
		base_types.FieldEntry(name='Cd', type=Quantity1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlAndCurFaceAmt', type=OriginalAndCurrentQuantities4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity36Choice, min=0, max=1, mutex_group=1, array=False),
	))

