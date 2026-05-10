from . import base_types
from ._PercentageRate import PercentageRate
from ._BillingRateIdentification1Choice import BillingRateIdentification1Choice
from ._Number import Number

class BillingRate1(base_types._BaseFieldType):

	__slots__ = ["_Val", "_DaysInYr", "_Id", "_DaysInPrd"]
	@property
	def DaysInPrd(self):
		return self._DaysInPrd

	@DaysInPrd.setter
	def DaysInPrd(self, value):
		self._DaysInPrd = value if type(value) != base_types.auto else self.make_default("DaysInPrd")

	@DaysInPrd.deleter
	def DaysInPrd(self):
		del self._DaysInPrd
		self._DaysInPrd = None

	@property
	def DaysInYr(self):
		return self._DaysInYr

	@DaysInYr.setter
	def DaysInYr(self, value):
		self._DaysInYr = value if type(value) != base_types.auto else self.make_default("DaysInYr")

	@DaysInYr.deleter
	def DaysInYr(self):
		del self._DaysInYr
		self._DaysInYr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

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
		base_types.FieldEntry(name='DaysInPrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DaysInYr', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=BillingRateIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))

