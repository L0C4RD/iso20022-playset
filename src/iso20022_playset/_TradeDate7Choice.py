from . import base_types
from ._TradingDateCode2Choice import TradingDateCode2Choice
from ._DateAndDateTime1Choice import DateAndDateTime1Choice

class TradeDate7Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_Val"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Val', type=TradingDateCode2Choice, min=0, max=1, mutex_group=1, array=False),
	))

