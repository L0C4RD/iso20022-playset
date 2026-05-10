from . import base_types
from .SecuritiesTransactionPrice17Choice import SecuritiesTransactionPrice17Choice
from .ISODate import ISODate

class Schedule1(base_types._BaseFieldType):

	__slots__ = ["_UadjstdFctvDt", "_UadjstdEndDt", "_Pric"]
	@property
	def UadjstdFctvDt(self):
		return self._UadjstdFctvDt

	@UadjstdFctvDt.setter
	def UadjstdFctvDt(self, value):
		self._UadjstdFctvDt = value if type(value) != base_types.auto else self.make_default("UadjstdFctvDt")

	@UadjstdFctvDt.deleter
	def UadjstdFctvDt(self):
		del self._UadjstdFctvDt
		self._UadjstdFctvDt = None

	@property
	def UadjstdEndDt(self):
		return self._UadjstdEndDt

	@UadjstdEndDt.setter
	def UadjstdEndDt(self, value):
		self._UadjstdEndDt = value if type(value) != base_types.auto else self.make_default("UadjstdEndDt")

	@UadjstdEndDt.deleter
	def UadjstdEndDt(self):
		del self._UadjstdEndDt
		self._UadjstdEndDt = None

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
		base_types.FieldEntry(name='UadjstdFctvDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UadjstdEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pric', type=SecuritiesTransactionPrice17Choice, min=1, max=1, mutex_group=None, array=False),
	))

