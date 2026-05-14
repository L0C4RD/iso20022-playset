from . import base_types
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._MarketIdentification89 import MarketIdentification89
from ._PriceRateOrAmount4Choice import PriceRateOrAmount4Choice

class PriceInformation25(base_types._BaseFieldType):

	__slots__ = ["_QtnDt", "_SrcOfPric", "_Val"]
	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if type(value) != base_types.auto else self.make_default("QtnDt")

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = None

	@property
	def SrcOfPric(self):
		return self._SrcOfPric

	@SrcOfPric.setter
	def SrcOfPric(self, value):
		self._SrcOfPric = value if type(value) != base_types.auto else self.make_default("SrcOfPric")

	@SrcOfPric.deleter
	def SrcOfPric(self):
		del self._SrcOfPric
		self._SrcOfPric = None

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
		base_types.FieldEntry(name='QtnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfPric', type=MarketIdentification89, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PriceRateOrAmount4Choice, min=1, max=1, mutex_group=None, array=False),
	))

