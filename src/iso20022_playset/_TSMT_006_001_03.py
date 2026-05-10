from . import base_types
from .AmendmentAcceptanceNotificationV03 import AmendmentAcceptanceNotificationV03

class TSMT_006_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AmdmntAccptncNtfctn"]
		@property
		def AmdmntAccptncNtfctn(self):
			return self._AmdmntAccptncNtfctn

		@AmdmntAccptncNtfctn.setter
		def AmdmntAccptncNtfctn(self, value):
			self._AmdmntAccptncNtfctn = value if type(value) != base_types.auto else self.make_default("AmdmntAccptncNtfctn")

		@AmdmntAccptncNtfctn.deleter
		def AmdmntAccptncNtfctn(self):
			del self._AmdmntAccptncNtfctn
			self._AmdmntAccptncNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AmdmntAccptncNtfctn', type=AmendmentAcceptanceNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

