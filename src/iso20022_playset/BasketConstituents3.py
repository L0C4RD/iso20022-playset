import base_types
import UnitOfMeasure8Choice
import InstrumentIdentification6Choice
import LongFraction19DecimalNumber

class BasketConstituents3(base_types._BaseFieldType):

	__slots__ = ["_Qty", "_InstrmId", "_UnitOfMeasr"]
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
	def InstrmId(self):
		return self._InstrmId

	@InstrmId.setter
	def InstrmId(self, value):
		self._InstrmId = value if type(value) != auto else self.make_default("InstrmId")

	@InstrmId.deleter
	def InstrmId(self):
		del self._InstrmId
		self._InstrmId = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Qty', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmId', type=InstrumentIdentification6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure8Choice, min=0, max=1, mutex_group=None, array=False),
	))

