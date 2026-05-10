import base_types
import Price8
import ISODateTime
import DateTimePeriod1Choice
import ISODate
import PercentageRate
import CalculationType3Choice

class YieldCalculation6(base_types._BaseFieldType):

	__slots__ = ["_ValDt", "_RedPric", "_ValPrd", "_ClctnTp", "_Val", "_ClctnDt"]
	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def RedPric(self):
		return self._RedPric

	@RedPric.setter
	def RedPric(self, value):
		self._RedPric = value if type(value) != auto else self.make_default("RedPric")

	@RedPric.deleter
	def RedPric(self):
		del self._RedPric
		self._RedPric = None

	@property
	def ValPrd(self):
		return self._ValPrd

	@ValPrd.setter
	def ValPrd(self, value):
		self._ValPrd = value if type(value) != auto else self.make_default("ValPrd")

	@ValPrd.deleter
	def ValPrd(self):
		del self._ValPrd
		self._ValPrd = None

	@property
	def ClctnTp(self):
		return self._ClctnTp

	@ClctnTp.setter
	def ClctnTp(self, value):
		self._ClctnTp = value if type(value) != auto else self.make_default("ClctnTp")

	@ClctnTp.deleter
	def ClctnTp(self):
		del self._ClctnTp
		self._ClctnTp = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	@property
	def ClctnDt(self):
		return self._ClctnDt

	@ClctnDt.setter
	def ClctnDt(self, value):
		self._ClctnDt = value if type(value) != auto else self.make_default("ClctnDt")

	@ClctnDt.deleter
	def ClctnDt(self):
		del self._ClctnDt
		self._ClctnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValPrd', type=DateTimePeriod1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnTp', type=CalculationType3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

