import base_types
import DemandRefusalNotificationV01

class TSRV_016_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DmndRfslNtfctn"]
		@property
		def DmndRfslNtfctn(self):
			return self._DmndRfslNtfctn

		@DmndRfslNtfctn.setter
		def DmndRfslNtfctn(self, value):
			self._DmndRfslNtfctn = value if type(value) != auto else self.make_default("DmndRfslNtfctn")

		@DmndRfslNtfctn.deleter
		def DmndRfslNtfctn(self):
			del self._DmndRfslNtfctn
			self._DmndRfslNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DmndRfslNtfctn', type=DemandRefusalNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))

