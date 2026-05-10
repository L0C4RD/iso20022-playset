from . import base_types
import LongFraction19DecimalNumber
import UnitOfMeasure8Choice
import SecuritiesTransactionPrice17Choice
import Schedule1

class PriceData2(base_types._BaseFieldType):

	__slots__ = ["_PricMltplr", "_UnitOfMeasr", "_SchdlPrd", "_Pric"]
	@property
	def PricMltplr(self):
		return self._PricMltplr

	@PricMltplr.setter
	def PricMltplr(self, value):
		self._PricMltplr = value if type(value) != auto else self.make_default("PricMltplr")

	@PricMltplr.deleter
	def PricMltplr(self):
		del self._PricMltplr
		self._PricMltplr = None

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

	@property
	def SchdlPrd(self):
		return self._SchdlPrd

	@SchdlPrd.setter
	def SchdlPrd(self, value):
		self._SchdlPrd = value if type(value) != auto else self.make_default("SchdlPrd")

	@SchdlPrd.deleter
	def SchdlPrd(self):
		del self._SchdlPrd
		self._SchdlPrd = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricMltplr', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchdlPrd', type=Schedule1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice17Choice, min=0, max=1, mutex_group=None, array=False),
	))

