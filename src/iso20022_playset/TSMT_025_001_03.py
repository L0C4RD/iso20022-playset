import base_types
import StatusChangeNotificationV03

class TSMT_025_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsChngNtfctn"]
		@property
		def StsChngNtfctn(self):
			return self._StsChngNtfctn

		@StsChngNtfctn.setter
		def StsChngNtfctn(self, value):
			self._StsChngNtfctn = value if type(value) != auto else self.make_default("StsChngNtfctn")

		@StsChngNtfctn.deleter
		def StsChngNtfctn(self):
			del self._StsChngNtfctn
			self._StsChngNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsChngNtfctn', type=StatusChangeNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

