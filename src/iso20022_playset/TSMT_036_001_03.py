from . import base_types
import StatusExtensionRequestNotificationV03

class TSMT_036_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsXtnsnReqNtfctn"]
		@property
		def StsXtnsnReqNtfctn(self):
			return self._StsXtnsnReqNtfctn

		@StsXtnsnReqNtfctn.setter
		def StsXtnsnReqNtfctn(self, value):
			self._StsXtnsnReqNtfctn = value if type(value) != auto else self.make_default("StsXtnsnReqNtfctn")

		@StsXtnsnReqNtfctn.deleter
		def StsXtnsnReqNtfctn(self):
			del self._StsXtnsnReqNtfctn
			self._StsXtnsnReqNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnReqNtfctn', type=StatusExtensionRequestNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

