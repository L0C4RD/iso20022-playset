# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._DateTimePeriod1Choice import DateTimePeriod1Choice
from ._ISODate import ISODate
from ._SystemEventType2Choice import SystemEventType2Choice
from ._SystemIdentification2Choice import SystemIdentification2Choice

class BusinessDaySearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_ClsrPrd", "_EvtTp", "_SysCcy", "_SysDt", "_SysId"]
	@property
	def ClsrPrd(self):
		return self._ClsrPrd

	@ClsrPrd.setter
	def ClsrPrd(self, value):
		self._ClsrPrd = value if type(value) != base_types.auto else self.make_default("ClsrPrd")

	@ClsrPrd.deleter
	def ClsrPrd(self):
		del self._ClsrPrd
		self._ClsrPrd = None

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if type(value) != base_types.auto else self.make_default("EvtTp")

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = None

	@property
	def SysCcy(self):
		return self._SysCcy

	@SysCcy.setter
	def SysCcy(self, value):
		self._SysCcy = value if type(value) != base_types.auto else self.make_default("SysCcy")

	@SysCcy.deleter
	def SysCcy(self):
		del self._SysCcy
		self._SysCcy = None

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
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if type(value) != base_types.auto else self.make_default("SysId")

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsrPrd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=SystemEventType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysCcy', type=ActiveCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=0, max=None, mutex_group=None, array=True),
	))