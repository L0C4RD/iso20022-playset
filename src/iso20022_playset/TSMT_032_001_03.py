import base_types
import StatusExtensionNotificationV03

class TSMT_032_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsXtnsnNtfctn"]
		@property
		def StsXtnsnNtfctn(self):
			return self._StsXtnsnNtfctn

		@StsXtnsnNtfctn.setter
		def StsXtnsnNtfctn(self, value):
			self._StsXtnsnNtfctn = value if type(value) != auto else self.make_default("StsXtnsnNtfctn")

		@StsXtnsnNtfctn.deleter
		def StsXtnsnNtfctn(self):
			del self._StsXtnsnNtfctn
			self._StsXtnsnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnNtfctn', type=StatusExtensionNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

