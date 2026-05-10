from . import base_types
from .Max35Text import Max35Text

class MeetingEventReference1Choice(base_types._BaseFieldType):

	__slots__ = ["_LkdIssrMtgId", "_LkdMtgId"]
	@property
	def LkdIssrMtgId(self):
		return self._LkdIssrMtgId

	@LkdIssrMtgId.setter
	def LkdIssrMtgId(self, value):
		self._LkdIssrMtgId = value if type(value) != base_types.auto else self.make_default("LkdIssrMtgId")

	@LkdIssrMtgId.deleter
	def LkdIssrMtgId(self):
		del self._LkdIssrMtgId
		self._LkdIssrMtgId = None

	@property
	def LkdMtgId(self):
		return self._LkdMtgId

	@LkdMtgId.setter
	def LkdMtgId(self, value):
		self._LkdMtgId = value if type(value) != base_types.auto else self.make_default("LkdMtgId")

	@LkdMtgId.deleter
	def LkdMtgId(self):
		del self._LkdMtgId
		self._LkdMtgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkdIssrMtgId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LkdMtgId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

