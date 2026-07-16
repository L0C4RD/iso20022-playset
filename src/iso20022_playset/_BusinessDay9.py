# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import SystemAvailabilityAndEvents3
from . import SystemStatus3

class BusinessDay9(base_types._BaseFieldType):

	__slots__ = ["_SysDt", "_SysInfPerCcy", "_SysSts"]
	@property
	def SysDt(self):
		return self._SysDt

	@SysDt.setter
	def SysDt(self, value):
		self._SysDt = value if value is not None else base_types.UninitialisedField(self, 'SysDt', DateAndDateTime2Choice, False)

	@SysDt.deleter
	def SysDt(self):
		del self._SysDt
		self._SysDt = base_types.UninitialisedField(self, 'SysDt', DateAndDateTime2Choice, False)

	@property
	def SysInfPerCcy(self):
		return self._SysInfPerCcy

	@SysInfPerCcy.setter
	def SysInfPerCcy(self, value):
		self._SysInfPerCcy = value if value is not None else base_types.UninitialisedField(self, 'SysInfPerCcy', SystemAvailabilityAndEvents3, True)

	@SysInfPerCcy.deleter
	def SysInfPerCcy(self):
		del self._SysInfPerCcy
		self._SysInfPerCcy = base_types.UninitialisedField(self, 'SysInfPerCcy', SystemAvailabilityAndEvents3, True)

	@property
	def SysSts(self):
		return self._SysSts

	@SysSts.setter
	def SysSts(self, value):
		self._SysSts = value if value is not None else base_types.UninitialisedField(self, 'SysSts', SystemStatus3, False)

	@SysSts.deleter
	def SysSts(self):
		del self._SysSts
		self._SysSts = base_types.UninitialisedField(self, 'SysSts', SystemStatus3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SysDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysInfPerCcy', type=SystemAvailabilityAndEvents3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysSts', type=SystemStatus3, min=0, max=1, mutex_group=None, array=False),
	))