# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NationalityCode
from . import YesNoIndicator

class CitizenshipInformation2(base_types._BaseFieldType):

	__slots__ = ["_MnrInd", "_Ntlty"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MnrInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntlty', type=NationalityCode, min=1, max=1, mutex_group=None, array=False),
	))