# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionNotificationType2Code
from . import DocumentIdentification8

class NotificationCancellation1(base_types._BaseFieldType):

	__slots__ = ["_LkdAgtCANtfctnAdvcId", "_NtfctnCxlTp"]
	@property
	def LkdAgtCANtfctnAdvcId(self):
		return self._LkdAgtCANtfctnAdvcId

	@LkdAgtCANtfctnAdvcId.setter
	def LkdAgtCANtfctnAdvcId(self, value):
		self._LkdAgtCANtfctnAdvcId = value if value is not None else base_types.UninitialisedField(self, 'LkdAgtCANtfctnAdvcId', DocumentIdentification8, False)

	@LkdAgtCANtfctnAdvcId.deleter
	def LkdAgtCANtfctnAdvcId(self):
		del self._LkdAgtCANtfctnAdvcId
		self._LkdAgtCANtfctnAdvcId = base_types.UninitialisedField(self, 'LkdAgtCANtfctnAdvcId', DocumentIdentification8, False)

	@property
	def NtfctnCxlTp(self):
		return self._NtfctnCxlTp

	@NtfctnCxlTp.setter
	def NtfctnCxlTp(self, value):
		self._NtfctnCxlTp = value if value is not None else base_types.UninitialisedField(self, 'NtfctnCxlTp', CorporateActionNotificationType2Code, False)

	@NtfctnCxlTp.deleter
	def NtfctnCxlTp(self):
		del self._NtfctnCxlTp
		self._NtfctnCxlTp = base_types.UninitialisedField(self, 'NtfctnCxlTp', CorporateActionNotificationType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkdAgtCANtfctnAdvcId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnCxlTp', type=CorporateActionNotificationType2Code, min=1, max=1, mutex_group=None, array=False),
	))