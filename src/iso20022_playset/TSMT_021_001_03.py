from . import base_types
from .MisMatchAcceptanceNotificationV03 import MisMatchAcceptanceNotificationV03

class TSMT_021_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MisMtchAccptncNtfctn"]
		@property
		def MisMtchAccptncNtfctn(self):
			return self._MisMtchAccptncNtfctn

		@MisMtchAccptncNtfctn.setter
		def MisMtchAccptncNtfctn(self, value):
			self._MisMtchAccptncNtfctn = value if type(value) != auto else self.make_default("MisMtchAccptncNtfctn")

		@MisMtchAccptncNtfctn.deleter
		def MisMtchAccptncNtfctn(self):
			del self._MisMtchAccptncNtfctn
			self._MisMtchAccptncNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MisMtchAccptncNtfctn', type=MisMatchAcceptanceNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

