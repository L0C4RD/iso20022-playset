from . import base_types
from ._MeetingNotificationV13 import MeetingNotificationV13

class SEEV_001_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MtgNtfctn"]
		@property
		def MtgNtfctn(self):
			return self._MtgNtfctn

		@MtgNtfctn.setter
		def MtgNtfctn(self, value):
			self._MtgNtfctn = value if type(value) != base_types.auto else self.make_default("MtgNtfctn")

		@MtgNtfctn.deleter
		def MtgNtfctn(self):
			del self._MtgNtfctn
			self._MtgNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgNtfctn', type=MeetingNotificationV13, min=1, max=1, mutex_group=None, array=False),
		))

