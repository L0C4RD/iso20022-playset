# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OriginalAndCurrentQuantities6
from . import SignedQuantityFormat10

class Quantity50Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlAndCurFaceAmt", "_SgndQty"]
	@property
	def OrgnlAndCurFaceAmt(self):
		return self._OrgnlAndCurFaceAmt

	@OrgnlAndCurFaceAmt.setter
	def OrgnlAndCurFaceAmt(self, value):
		self._OrgnlAndCurFaceAmt = value if value is not None else base_types.UninitialisedField(self, 'OrgnlAndCurFaceAmt', OriginalAndCurrentQuantities6, False)

	@OrgnlAndCurFaceAmt.deleter
	def OrgnlAndCurFaceAmt(self):
		del self._OrgnlAndCurFaceAmt
		self._OrgnlAndCurFaceAmt = base_types.UninitialisedField(self, 'OrgnlAndCurFaceAmt', OriginalAndCurrentQuantities6, False)

	@property
	def SgndQty(self):
		return self._SgndQty

	@SgndQty.setter
	def SgndQty(self, value):
		self._SgndQty = value if value is not None else base_types.UninitialisedField(self, 'SgndQty', SignedQuantityFormat10, False)

	@SgndQty.deleter
	def SgndQty(self):
		del self._SgndQty
		self._SgndQty = base_types.UninitialisedField(self, 'SgndQty', SignedQuantityFormat10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlAndCurFaceAmt', type=OriginalAndCurrentQuantities6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgndQty', type=SignedQuantityFormat10, min=0, max=1, mutex_group=1, array=False),
	))