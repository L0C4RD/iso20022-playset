# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionNotificationType1Code
from . import CorporateActionProcessingStatus5Choice
from . import Max35Text

class CorporateActionNotification9(base_types._BaseFieldType):

	__slots__ = ["_NtfctnId", "_NtfctnTp", "_PrcgSts"]
	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if value is not None else base_types.UninitialisedField(self, 'NtfctnId', Max35Text, False)

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = base_types.UninitialisedField(self, 'NtfctnId', Max35Text, False)

	@property
	def NtfctnTp(self):
		return self._NtfctnTp

	@NtfctnTp.setter
	def NtfctnTp(self, value):
		self._NtfctnTp = value if value is not None else base_types.UninitialisedField(self, 'NtfctnTp', CorporateActionNotificationType1Code, False)

	@NtfctnTp.deleter
	def NtfctnTp(self):
		del self._NtfctnTp
		self._NtfctnTp = base_types.UninitialisedField(self, 'NtfctnTp', CorporateActionNotificationType1Code, False)

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', CorporateActionProcessingStatus5Choice, False)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', CorporateActionProcessingStatus5Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtfctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnTp', type=CorporateActionNotificationType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=CorporateActionProcessingStatus5Choice, min=1, max=1, mutex_group=None, array=False),
	))