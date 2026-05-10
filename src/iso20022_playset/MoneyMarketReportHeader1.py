from . import base_types
from .DateTimePeriod1 import DateTimePeriod1
from .LEIIdentifier import LEIIdentifier

class MoneyMarketReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_RefPrd", "_RptgAgt"]
	@property
	def RefPrd(self):
		return self._RefPrd

	@RefPrd.setter
	def RefPrd(self, value):
		self._RefPrd = value if type(value) != base_types.auto else self.make_default("RefPrd")

	@RefPrd.deleter
	def RefPrd(self):
		del self._RefPrd
		self._RefPrd = None

	@property
	def RptgAgt(self):
		return self._RptgAgt

	@RptgAgt.setter
	def RptgAgt(self, value):
		self._RptgAgt = value if type(value) != base_types.auto else self.make_default("RptgAgt")

	@RptgAgt.deleter
	def RptgAgt(self):
		del self._RptgAgt
		self._RptgAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RefPrd', type=DateTimePeriod1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgAgt', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
	))

