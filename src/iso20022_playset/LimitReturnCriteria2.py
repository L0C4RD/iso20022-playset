from . import base_types
from .RequestedIndicator import RequestedIndicator

class LimitReturnCriteria2(base_types._BaseFieldType):

	__slots__ = ["_StsInd", "_StartDtTmInd", "_UsdAmtInd", "_UsdPctgInd"]
	@property
	def StsInd(self):
		return self._StsInd

	@StsInd.setter
	def StsInd(self, value):
		self._StsInd = value if type(value) != auto else self.make_default("StsInd")

	@StsInd.deleter
	def StsInd(self):
		del self._StsInd
		self._StsInd = None

	@property
	def StartDtTmInd(self):
		return self._StartDtTmInd

	@StartDtTmInd.setter
	def StartDtTmInd(self, value):
		self._StartDtTmInd = value if type(value) != auto else self.make_default("StartDtTmInd")

	@StartDtTmInd.deleter
	def StartDtTmInd(self):
		del self._StartDtTmInd
		self._StartDtTmInd = None

	@property
	def UsdAmtInd(self):
		return self._UsdAmtInd

	@UsdAmtInd.setter
	def UsdAmtInd(self, value):
		self._UsdAmtInd = value if type(value) != auto else self.make_default("UsdAmtInd")

	@UsdAmtInd.deleter
	def UsdAmtInd(self):
		del self._UsdAmtInd
		self._UsdAmtInd = None

	@property
	def UsdPctgInd(self):
		return self._UsdPctgInd

	@UsdPctgInd.setter
	def UsdPctgInd(self, value):
		self._UsdPctgInd = value if type(value) != auto else self.make_default("UsdPctgInd")

	@UsdPctgInd.deleter
	def UsdPctgInd(self):
		del self._UsdPctgInd
		self._UsdPctgInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDtTmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsdAmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsdPctgInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

