# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from ._OriginalAndCurrentQuantities1 import OriginalAndCurrentQuantities1

class Quantity6Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlAndCurFace", "_Qty"]
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
		base_types.FieldEntry(name='OrgnlAndCurFace', type=OriginalAndCurrentQuantities1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=1, array=False),
	))