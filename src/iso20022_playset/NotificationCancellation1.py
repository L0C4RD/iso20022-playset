from . import base_types
from .CorporateActionNotificationType2Code import CorporateActionNotificationType2Code
from .DocumentIdentification8 import DocumentIdentification8

class NotificationCancellation1(base_types._BaseFieldType):

	__slots__ = ["_LkdAgtCANtfctnAdvcId", "_NtfctnCxlTp"]
	@property
	def LkdAgtCANtfctnAdvcId(self):
		return self._LkdAgtCANtfctnAdvcId

	@LkdAgtCANtfctnAdvcId.setter
	def LkdAgtCANtfctnAdvcId(self, value):
		self._LkdAgtCANtfctnAdvcId = value if type(value) != base_types.auto else self.make_default("LkdAgtCANtfctnAdvcId")

	@LkdAgtCANtfctnAdvcId.deleter
	def LkdAgtCANtfctnAdvcId(self):
		del self._LkdAgtCANtfctnAdvcId
		self._LkdAgtCANtfctnAdvcId = None

	@property
	def NtfctnCxlTp(self):
		return self._NtfctnCxlTp

	@NtfctnCxlTp.setter
	def NtfctnCxlTp(self, value):
		self._NtfctnCxlTp = value if type(value) != base_types.auto else self.make_default("NtfctnCxlTp")

	@NtfctnCxlTp.deleter
	def NtfctnCxlTp(self):
		del self._NtfctnCxlTp
		self._NtfctnCxlTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkdAgtCANtfctnAdvcId', type=DocumentIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnCxlTp', type=CorporateActionNotificationType2Code, min=1, max=1, mutex_group=None, array=False),
	))

