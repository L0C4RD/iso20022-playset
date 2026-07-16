# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantitySearch2
from . import FinancialInstrumentQuantitySearch2Choice

class QuantitySearch2Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlAndCurFace", "_Qty"]
	@property
	def OrgnlAndCurFace(self):
		return self._OrgnlAndCurFace

	@OrgnlAndCurFace.setter
	def OrgnlAndCurFace(self, value):
		self._OrgnlAndCurFace = value if value is not None else base_types.UninitialisedField(self, 'OrgnlAndCurFace', FinancialInstrumentQuantitySearch2, False)

	@OrgnlAndCurFace.deleter
	def OrgnlAndCurFace(self):
		del self._OrgnlAndCurFace
		self._OrgnlAndCurFace = base_types.UninitialisedField(self, 'OrgnlAndCurFace', FinancialInstrumentQuantitySearch2, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantitySearch2Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', FinancialInstrumentQuantitySearch2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlAndCurFace', type=FinancialInstrumentQuantitySearch2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Qty', type=FinancialInstrumentQuantitySearch2Choice, min=0, max=1, mutex_group=1, array=False),
	))