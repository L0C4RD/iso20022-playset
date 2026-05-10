from . import base_types
import OriginalAndCurrentQuantities1
import FinancialInstrumentQuantity33Choice
import Quantity1Code

class Quantity52Choice(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_Qty", "_OrgnlAndCurFaceAmt"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

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

	@property
	def OrgnlAndCurFaceAmt(self):
		return self._OrgnlAndCurFaceAmt

	@OrgnlAndCurFaceAmt.setter
	def OrgnlAndCurFaceAmt(self, value):
		self._OrgnlAndCurFaceAmt = value if type(value) != auto else self.make_default("OrgnlAndCurFaceAmt")

	@OrgnlAndCurFaceAmt.deleter
	def OrgnlAndCurFaceAmt(self):
		del self._OrgnlAndCurFaceAmt
		self._OrgnlAndCurFaceAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=Quantity1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlAndCurFaceAmt', type=OriginalAndCurrentQuantities1, min=0, max=1, mutex_group=1, array=False),
	))

