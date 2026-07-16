# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import SystemStatus3Choice

class CalendarData1(base_types._BaseFieldType):

	__slots__ = ["_SysDt", "_SysSts"]
	@property
	def SysDt(self):
		return self._SysDt

	@SysDt.setter
	def SysDt(self, value):
		self._SysDt = value if value is not None else base_types.UninitialisedField(self, 'SysDt', ISODate, False)

	@SysDt.deleter
	def SysDt(self):
		del self._SysDt
		self._SysDt = base_types.UninitialisedField(self, 'SysDt', ISODate, False)

	@property
	def SysSts(self):
		return self._SysSts

	@SysSts.setter
	def SysSts(self, value):
		self._SysSts = value if value is not None else base_types.UninitialisedField(self, 'SysSts', SystemStatus3Choice, False)

	@SysSts.deleter
	def SysSts(self):
		del self._SysSts
		self._SysSts = base_types.UninitialisedField(self, 'SysSts', SystemStatus3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SysDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysSts', type=SystemStatus3Choice, min=1, max=1, mutex_group=None, array=False),
	))