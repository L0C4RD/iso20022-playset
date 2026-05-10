from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .DateAndDateTime2Choice import DateAndDateTime2Choice

class Visibilty1(base_types._BaseFieldType):

	__slots__ = ["_LtdVsblty", "_StartDt", "_EndDt"]
	@property
	def LtdVsblty(self):
		return self._LtdVsblty

	@LtdVsblty.setter
	def LtdVsblty(self, value):
		self._LtdVsblty = value if type(value) != base_types.auto else self.make_default("LtdVsblty")

	@LtdVsblty.deleter
	def LtdVsblty(self):
		del self._LtdVsblty
		self._LtdVsblty = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != base_types.auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if type(value) != base_types.auto else self.make_default("EndDt")

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LtdVsblty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

