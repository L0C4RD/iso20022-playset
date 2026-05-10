from . import base_types
import InformationRequestStatusChangeNotificationV01

class AUTH_003_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InfReqStsChngNtfctn"]
		@property
		def InfReqStsChngNtfctn(self):
			return self._InfReqStsChngNtfctn

		@InfReqStsChngNtfctn.setter
		def InfReqStsChngNtfctn(self, value):
			self._InfReqStsChngNtfctn = value if type(value) != auto else self.make_default("InfReqStsChngNtfctn")

		@InfReqStsChngNtfctn.deleter
		def InfReqStsChngNtfctn(self):
			del self._InfReqStsChngNtfctn
			self._InfReqStsChngNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InfReqStsChngNtfctn', type=InformationRequestStatusChangeNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))

