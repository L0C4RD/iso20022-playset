# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class ReservationReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_StartDtTmInd", "_StsInd"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='StartDtTmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))