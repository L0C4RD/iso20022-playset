# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class BusinessDayReturnCriteria2(base_types._BaseFieldType):

	__slots__ = ["_ClsrPrdInd", "_EvtInd", "_EvtTpInd", "_SsnPrdInd", "_SysCcyInd", "_SysDtInd", "_SysStsInd"]
	@property
	def ClsrPrdInd(self):
		return self._ClsrPrdInd

	@ClsrPrdInd.setter
	def ClsrPrdInd(self, value):
		self._ClsrPrdInd = value if value is not None else base_types.UninitialisedField(self, 'ClsrPrdInd', RequestedIndicator, False)

	@ClsrPrdInd.deleter
	def ClsrPrdInd(self):
		del self._ClsrPrdInd
		self._ClsrPrdInd = base_types.UninitialisedField(self, 'ClsrPrdInd', RequestedIndicator, False)

	@property
	def EvtInd(self):
		return self._EvtInd

	@EvtInd.setter
	def EvtInd(self, value):
		self._EvtInd = value if value is not None else base_types.UninitialisedField(self, 'EvtInd', RequestedIndicator, False)

	@EvtInd.deleter
	def EvtInd(self):
		del self._EvtInd
		self._EvtInd = base_types.UninitialisedField(self, 'EvtInd', RequestedIndicator, False)

	@property
	def EvtTpInd(self):
		return self._EvtTpInd

	@EvtTpInd.setter
	def EvtTpInd(self, value):
		self._EvtTpInd = value if value is not None else base_types.UninitialisedField(self, 'EvtTpInd', RequestedIndicator, False)

	@EvtTpInd.deleter
	def EvtTpInd(self):
		del self._EvtTpInd
		self._EvtTpInd = base_types.UninitialisedField(self, 'EvtTpInd', RequestedIndicator, False)

	@property
	def SsnPrdInd(self):
		return self._SsnPrdInd

	@SsnPrdInd.setter
	def SsnPrdInd(self, value):
		self._SsnPrdInd = value if value is not None else base_types.UninitialisedField(self, 'SsnPrdInd', RequestedIndicator, False)

	@SsnPrdInd.deleter
	def SsnPrdInd(self):
		del self._SsnPrdInd
		self._SsnPrdInd = base_types.UninitialisedField(self, 'SsnPrdInd', RequestedIndicator, False)

	@property
	def SysCcyInd(self):
		return self._SysCcyInd

	@SysCcyInd.setter
	def SysCcyInd(self, value):
		self._SysCcyInd = value if value is not None else base_types.UninitialisedField(self, 'SysCcyInd', RequestedIndicator, False)

	@SysCcyInd.deleter
	def SysCcyInd(self):
		del self._SysCcyInd
		self._SysCcyInd = base_types.UninitialisedField(self, 'SysCcyInd', RequestedIndicator, False)

	@property
	def SysDtInd(self):
		return self._SysDtInd

	@SysDtInd.setter
	def SysDtInd(self, value):
		self._SysDtInd = value if value is not None else base_types.UninitialisedField(self, 'SysDtInd', RequestedIndicator, False)

	@SysDtInd.deleter
	def SysDtInd(self):
		del self._SysDtInd
		self._SysDtInd = base_types.UninitialisedField(self, 'SysDtInd', RequestedIndicator, False)

	@property
	def SysStsInd(self):
		return self._SysStsInd

	@SysStsInd.setter
	def SysStsInd(self, value):
		self._SysStsInd = value if value is not None else base_types.UninitialisedField(self, 'SysStsInd', RequestedIndicator, False)

	@SysStsInd.deleter
	def SysStsInd(self):
		del self._SysStsInd
		self._SysStsInd = base_types.UninitialisedField(self, 'SysStsInd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsrPrdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SsnPrdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysCcyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysDtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysStsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))