import base_types
import StatusChangeRequestNotificationV03

class TSMT_028_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsChngReqNtfctn"]
		@property
		def StsChngReqNtfctn(self):
			return self._StsChngReqNtfctn

		@StsChngReqNtfctn.setter
		def StsChngReqNtfctn(self, value):
			self._StsChngReqNtfctn = value if type(value) != auto else self.make_default("StsChngReqNtfctn")

		@StsChngReqNtfctn.deleter
		def StsChngReqNtfctn(self):
			del self._StsChngReqNtfctn
			self._StsChngReqNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReqNtfctn', type=StatusChangeRequestNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

