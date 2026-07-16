# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class LimitReturnCriteria2(base_types._BaseFieldType):

	__slots__ = ["_StartDtTmInd", "_StsInd", "_UsdAmtInd", "_UsdPctgInd"]
	@property
	def StartDtTmInd(self):
		return self._StartDtTmInd

	@StartDtTmInd.setter
	def StartDtTmInd(self, value):
		self._StartDtTmInd = value if value is not None else base_types.UninitialisedField(self, 'StartDtTmInd', RequestedIndicator, False)

	@StartDtTmInd.deleter
	def StartDtTmInd(self):
		del self._StartDtTmInd
		self._StartDtTmInd = base_types.UninitialisedField(self, 'StartDtTmInd', RequestedIndicator, False)

	@property
	def StsInd(self):
		return self._StsInd

	@StsInd.setter
	def StsInd(self, value):
		self._StsInd = value if value is not None else base_types.UninitialisedField(self, 'StsInd', RequestedIndicator, False)

	@StsInd.deleter
	def StsInd(self):
		del self._StsInd
		self._StsInd = base_types.UninitialisedField(self, 'StsInd', RequestedIndicator, False)

	@property
	def UsdAmtInd(self):
		return self._UsdAmtInd

	@UsdAmtInd.setter
	def UsdAmtInd(self, value):
		self._UsdAmtInd = value if value is not None else base_types.UninitialisedField(self, 'UsdAmtInd', RequestedIndicator, False)

	@UsdAmtInd.deleter
	def UsdAmtInd(self):
		del self._UsdAmtInd
		self._UsdAmtInd = base_types.UninitialisedField(self, 'UsdAmtInd', RequestedIndicator, False)

	@property
	def UsdPctgInd(self):
		return self._UsdPctgInd

	@UsdPctgInd.setter
	def UsdPctgInd(self, value):
		self._UsdPctgInd = value if value is not None else base_types.UninitialisedField(self, 'UsdPctgInd', RequestedIndicator, False)

	@UsdPctgInd.deleter
	def UsdPctgInd(self):
		del self._UsdPctgInd
		self._UsdPctgInd = base_types.UninitialisedField(self, 'UsdPctgInd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='StartDtTmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsdAmtInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsdPctgInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))