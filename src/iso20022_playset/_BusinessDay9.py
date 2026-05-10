from . import base_types
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._SystemAvailabilityAndEvents3 import SystemAvailabilityAndEvents3
from ._SystemStatus3 import SystemStatus3

class BusinessDay9(base_types._BaseFieldType):

	__slots__ = ["_SysDt", "_SysInfPerCcy", "_SysSts"]
	@property
	def SysDt(self):
		return self._SysDt

	@SysDt.setter
	def SysDt(self, value):
		self._SysDt = value if type(value) != base_types.auto else self.make_default("SysDt")

	@SysDt.deleter
	def SysDt(self):
		del self._SysDt
		self._SysDt = None

	@property
	def SysInfPerCcy(self):
		return self._SysInfPerCcy

	@SysInfPerCcy.setter
	def SysInfPerCcy(self, value):
		self._SysInfPerCcy = value if type(value) != base_types.auto else self.make_default("SysInfPerCcy")

	@SysInfPerCcy.deleter
	def SysInfPerCcy(self):
		del self._SysInfPerCcy
		self._SysInfPerCcy = None

	@property
	def SysSts(self):
		return self._SysSts

	@SysSts.setter
	def SysSts(self, value):
		self._SysSts = value if type(value) != base_types.auto else self.make_default("SysSts")

	@SysSts.deleter
	def SysSts(self):
		del self._SysSts
		self._SysSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SysDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysInfPerCcy', type=SystemAvailabilityAndEvents3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysSts', type=SystemStatus3, min=0, max=1, mutex_group=None, array=False),
	))

