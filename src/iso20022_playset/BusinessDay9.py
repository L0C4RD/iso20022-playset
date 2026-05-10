import base_types
import SystemStatus3
import SystemAvailabilityAndEvents3
import DateAndDateTime2Choice

class BusinessDay9(base_types._BaseFieldType):

	__slots__ = ["_SysSts", "_SysDt", "_SysInfPerCcy"]
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
	def SysInfPerCcy(self):
		return self._SysInfPerCcy

	@SysInfPerCcy.setter
	def SysInfPerCcy(self, value):
		self._SysInfPerCcy = value if type(value) != auto else self.make_default("SysInfPerCcy")

	@SysInfPerCcy.deleter
	def SysInfPerCcy(self):
		del self._SysInfPerCcy
		self._SysInfPerCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SysSts', type=SystemStatus3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysInfPerCcy', type=SystemAvailabilityAndEvents3, min=0, max=None, mutex_group=None, array=True),
	))

