from . import base_types
from .PercentageRate import PercentageRate
from .ISODate import ISODate

class RateAdjustment1(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_AdjstmntDt"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def AdjstmntDt(self):
		return self._AdjstmntDt

	@AdjstmntDt.setter
	def AdjstmntDt(self, value):
		self._AdjstmntDt = value if type(value) != base_types.auto else self.make_default("AdjstmntDt")

	@AdjstmntDt.deleter
	def AdjstmntDt(self):
		del self._AdjstmntDt
		self._AdjstmntDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdjstmntDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

