# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentIdentification35
from . import Max35Text

class ContractRegistrationReference2Choice(base_types._BaseFieldType):

	__slots__ = ["_Ctrct", "_RegdCtrctId"]
	@property
	def Ctrct(self):
		return self._Ctrct

	@Ctrct.setter
	def Ctrct(self, value):
		self._Ctrct = value if value is not None else base_types.UninitialisedField(self, 'Ctrct', DocumentIdentification35, False)

	@Ctrct.deleter
	def Ctrct(self):
		del self._Ctrct
		self._Ctrct = base_types.UninitialisedField(self, 'Ctrct', DocumentIdentification35, False)

	@property
	def RegdCtrctId(self):
		return self._RegdCtrctId

	@RegdCtrctId.setter
	def RegdCtrctId(self, value):
		self._RegdCtrctId = value if value is not None else base_types.UninitialisedField(self, 'RegdCtrctId', Max35Text, False)

	@RegdCtrctId.deleter
	def RegdCtrctId(self):
		del self._RegdCtrctId
		self._RegdCtrctId = base_types.UninitialisedField(self, 'RegdCtrctId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctrct', type=DocumentIdentification35, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RegdCtrctId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))