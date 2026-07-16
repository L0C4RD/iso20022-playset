# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InstrumentIdentification6Choice
from . import LongFraction19DecimalNumber
from . import UnitOfMeasure8Choice

class BasketConstituents3(base_types._BaseFieldType):

	__slots__ = ["_InstrmId", "_Qty", "_UnitOfMeasr"]
	@property
	def InstrmId(self):
		return self._InstrmId

	@InstrmId.setter
	def InstrmId(self, value):
		self._InstrmId = value if value is not None else base_types.UninitialisedField(self, 'InstrmId', InstrumentIdentification6Choice, False)

	@InstrmId.deleter
	def InstrmId(self):
		del self._InstrmId
		self._InstrmId = base_types.UninitialisedField(self, 'InstrmId', InstrumentIdentification6Choice, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', LongFraction19DecimalNumber, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', LongFraction19DecimalNumber, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure8Choice, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure8Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrmId', type=InstrumentIdentification6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure8Choice, min=0, max=1, mutex_group=None, array=False),
	))