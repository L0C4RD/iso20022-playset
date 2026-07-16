# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import DateTimePeriod1Choice
from . import ISODate
from . import SystemEventType2Choice
from . import SystemIdentification2Choice

class BusinessDaySearchCriteria2(base_types._BaseFieldType):

	__slots__ = ["_ClsrPrd", "_EvtTp", "_SysCcy", "_SysDt", "_SysId"]
	@property
	def ClsrPrd(self):
		return self._ClsrPrd

	@ClsrPrd.setter
	def ClsrPrd(self, value):
		self._ClsrPrd = value if value is not None else base_types.UninitialisedField(self, 'ClsrPrd', DateTimePeriod1Choice, False)

	@ClsrPrd.deleter
	def ClsrPrd(self):
		del self._ClsrPrd
		self._ClsrPrd = base_types.UninitialisedField(self, 'ClsrPrd', DateTimePeriod1Choice, False)

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', SystemEventType2Choice, False)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', SystemEventType2Choice, False)

	@property
	def SysCcy(self):
		return self._SysCcy

	@SysCcy.setter
	def SysCcy(self, value):
		self._SysCcy = value if value is not None else base_types.UninitialisedField(self, 'SysCcy', ActiveCurrencyCode, True)

	@SysCcy.deleter
	def SysCcy(self):
		del self._SysCcy
		self._SysCcy = base_types.UninitialisedField(self, 'SysCcy', ActiveCurrencyCode, True)

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
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if value is not None else base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, True)

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsrPrd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=SystemEventType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysCcy', type=ActiveCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=0, max=None, mutex_group=None, array=True),
	))