import base_types
import ISODate
import SystemStatus3Choice

class CalendarData1(base_types._BaseFieldType):

	__slots__ = ["_SysDt", "_SysSts"]
	@property
	def SysDt(self):
		return self._SysDt

	@SysDt.setter
	def SysDt(self, value):
		self._SysDt = value if type(value) != auto else self.make_default("SysDt")

	@SysDt.deleter
	def SysDt(self):
		del self._SysDt
		self._SysDt = None

	@property
	def SysSts(self):
		return self._SysSts

	@SysSts.setter
	def SysSts(self, value):
		self._SysSts = value if type(value) != auto else self.make_default("SysSts")

	@SysSts.deleter
	def SysSts(self):
		del self._SysSts
		self._SysSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SysDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysSts', type=SystemStatus3Choice, min=1, max=1, mutex_group=None, array=False),
	))

