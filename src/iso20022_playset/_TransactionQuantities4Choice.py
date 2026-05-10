from . import base_types
from .FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from .ProprietaryQuantity1 import ProprietaryQuantity1
from .OriginalAndCurrentQuantities1 import OriginalAndCurrentQuantities1

class TransactionQuantities4Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_OrgnlAndCurFaceAmt", "_Qty"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

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
		base_types.FieldEntry(name='Prtry', type=ProprietaryQuantity1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlAndCurFaceAmt', type=OriginalAndCurrentQuantities1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=1, array=False),
	))

