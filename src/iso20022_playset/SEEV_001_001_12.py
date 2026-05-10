from . import base_types
import MeetingNotificationV12

class SEEV_001_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MtgNtfctn"]
		@property
		def MtgNtfctn(self):
			return self._MtgNtfctn

		@MtgNtfctn.setter
		def MtgNtfctn(self, value):
			self._MtgNtfctn = value if type(value) != auto else self.make_default("MtgNtfctn")

		@MtgNtfctn.deleter
		def MtgNtfctn(self):
			del self._MtgNtfctn
			self._MtgNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MtgNtfctn', type=MeetingNotificationV12, min=1, max=1, mutex_group=None, array=False),
		))

