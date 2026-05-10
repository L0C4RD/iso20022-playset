import base_types
import StatusChangeRequestRejectionNotificationV03

class TSMT_030_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsChngReqRjctnNtfctn"]
		@property
		def StsChngReqRjctnNtfctn(self):
			return self._StsChngReqRjctnNtfctn

		@StsChngReqRjctnNtfctn.setter
		def StsChngReqRjctnNtfctn(self, value):
			self._StsChngReqRjctnNtfctn = value if type(value) != auto else self.make_default("StsChngReqRjctnNtfctn")

		@StsChngReqRjctnNtfctn.deleter
		def StsChngReqRjctnNtfctn(self):
			del self._StsChngReqRjctnNtfctn
			self._StsChngReqRjctnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngReqRjctnNtfctn', type=StatusChangeRequestRejectionNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

