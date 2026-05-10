from . import base_types
from .OriginalAndCurrentQuantities6 import OriginalAndCurrentQuantities6
from .SignedQuantityFormat10 import SignedQuantityFormat10

class Quantity50Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlAndCurFaceAmt", "_SgndQty"]
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
	def SgndQty(self):
		return self._SgndQty

	@SgndQty.setter
	def SgndQty(self, value):
		self._SgndQty = value if type(value) != base_types.auto else self.make_default("SgndQty")

	@SgndQty.deleter
	def SgndQty(self):
		del self._SgndQty
		self._SgndQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlAndCurFaceAmt', type=OriginalAndCurrentQuantities6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgndQty', type=SignedQuantityFormat10, min=0, max=1, mutex_group=1, array=False),
	))

