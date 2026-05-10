from . import base_types
from ._FinancialInstrumentAggregateBalance1Choice import FinancialInstrumentAggregateBalance1Choice
from ._ISODate import ISODate
from ._Price6 import Price6

class FinancialInstrumentAggregateBalance1(base_types._BaseFieldType):

	__slots__ = ["_Hldgs", "_ItmDt", "_Pric"]
	@property
	def Hldgs(self):
		return self._Hldgs

	@Hldgs.setter
	def Hldgs(self, value):
		self._Hldgs = value if type(value) != base_types.auto else self.make_default("Hldgs")

	@Hldgs.deleter
	def Hldgs(self):
		del self._Hldgs
		self._Hldgs = None

	@property
	def ItmDt(self):
		return self._ItmDt

	@ItmDt.setter
	def ItmDt(self, value):
		self._ItmDt = value if type(value) != base_types.auto else self.make_default("ItmDt")

	@ItmDt.deleter
	def ItmDt(self):
		del self._ItmDt
		self._ItmDt = None

	@property
	def Pric(self):
		return self._Pric

	@Pric.setter
	def Pric(self, value):
		self._Pric = value if type(value) != base_types.auto else self.make_default("Pric")

	@Pric.deleter
	def Pric(self):
		del self._Pric
		self._Pric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hldgs', type=FinancialInstrumentAggregateBalance1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=Price6, min=0, max=None, mutex_group=None, array=True),
	))

