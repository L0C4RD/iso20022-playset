# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import NationalityCode
from . import YesNoIndicator

class CitizenshipInformation1(base_types._BaseFieldType):

	__slots__ = ["_EndDt", "_MnrInd", "_Ntlty", "_StartDt"]
	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@property
	def MnrInd(self):
		return self._MnrInd

	@MnrInd.setter
	def MnrInd(self, value):
		self._MnrInd = value if value is not None else base_types.UninitialisedField(self, 'MnrInd', YesNoIndicator, False)

	@MnrInd.deleter
	def MnrInd(self):
		del self._MnrInd
		self._MnrInd = base_types.UninitialisedField(self, 'MnrInd', YesNoIndicator, False)

	@property
	def Ntlty(self):
		return self._Ntlty

	@Ntlty.setter
	def Ntlty(self, value):
		self._Ntlty = value if value is not None else base_types.UninitialisedField(self, 'Ntlty', NationalityCode, False)

	@Ntlty.deleter
	def Ntlty(self):
		del self._Ntlty
		self._Ntlty = base_types.UninitialisedField(self, 'Ntlty', NationalityCode, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntlty', type=NationalityCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))