from . import base_types
from ._RequestedIndicator import RequestedIndicator

class BusinessDayReturnCriteria2(base_types._BaseFieldType):

	__slots__ = ["_ClsrPrdInd", "_EvtInd", "_EvtTpInd", "_SsnPrdInd", "_SysCcyInd", "_SysDtInd", "_SysStsInd"]
	@property
	def ClsrPrdInd(self):
		return self._ClsrPrdInd

	@ClsrPrdInd.setter
	def ClsrPrdInd(self, value):
		self._ClsrPrdInd = value if type(value) != base_types.auto else self.make_default("ClsrPrdInd")

	@ClsrPrdInd.deleter
	def ClsrPrdInd(self):
		del self._ClsrPrdInd
		self._ClsrPrdInd = None

	@property
	def EvtInd(self):
		return self._EvtInd

	@EvtInd.setter
	def EvtInd(self, value):
		self._EvtInd = value if type(value) != base_types.auto else self.make_default("EvtInd")

	@EvtInd.deleter
	def EvtInd(self):
		del self._EvtInd
		self._EvtInd = None

	@property
	def EvtTpInd(self):
		return self._EvtTpInd

	@EvtTpInd.setter
	def EvtTpInd(self, value):
		self._EvtTpInd = value if type(value) != base_types.auto else self.make_default("EvtTpInd")

	@EvtTpInd.deleter
	def EvtTpInd(self):
		del self._EvtTpInd
		self._EvtTpInd = None

	@property
	def SsnPrdInd(self):
		return self._SsnPrdInd

	@SsnPrdInd.setter
	def SsnPrdInd(self, value):
		self._SsnPrdInd = value if type(value) != base_types.auto else self.make_default("SsnPrdInd")

	@SsnPrdInd.deleter
	def SsnPrdInd(self):
		del self._SsnPrdInd
		self._SsnPrdInd = None

	@property
	def SysCcyInd(self):
		return self._SysCcyInd

	@SysCcyInd.setter
	def SysCcyInd(self, value):
		self._SysCcyInd = value if type(value) != base_types.auto else self.make_default("SysCcyInd")

	@SysCcyInd.deleter
	def SysCcyInd(self):
		del self._SysCcyInd
		self._SysCcyInd = None

	@property
	def SysDtInd(self):
		return self._SysDtInd

	@SysDtInd.setter
	def SysDtInd(self, value):
		self._SysDtInd = value if type(value) != base_types.auto else self.make_default("SysDtInd")

	@SysDtInd.deleter
	def SysDtInd(self):
		del self._SysDtInd
		self._SysDtInd = None

	@property
	def SysStsInd(self):
		return self._SysStsInd

	@SysStsInd.setter
	def SysStsInd(self, value):
		self._SysStsInd = value if type(value) != base_types.auto else self.make_default("SysStsInd")

	@SysStsInd.deleter
	def SysStsInd(self):
		del self._SysStsInd
		self._SysStsInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsrPrdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SsnPrdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysCcyInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysDtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysStsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

