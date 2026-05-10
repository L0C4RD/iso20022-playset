from . import base_types
from ._LongFraction19DecimalNumber import LongFraction19DecimalNumber
from ._UnitOfMeasure8Choice import UnitOfMeasure8Choice
from ._InstrumentIdentification6Choice import InstrumentIdentification6Choice

class BasketConstituents3(base_types._BaseFieldType):

	__slots__ = ["_UnitOfMeasr", "_InstrmId", "_Qty"]
	@property
	def InstrmId(self):
		return self._InstrmId

	@InstrmId.setter
	def InstrmId(self, value):
		self._InstrmId = value if type(value) != base_types.auto else self.make_default("InstrmId")

	@InstrmId.deleter
	def InstrmId(self):
		del self._InstrmId
		self._InstrmId = None

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

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != base_types.auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrmId', type=InstrumentIdentification6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure8Choice, min=0, max=1, mutex_group=None, array=False),
	))

