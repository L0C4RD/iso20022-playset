import base_types
import TimeOutNotificationV03

class TSMT_040_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TmOutNtfctn"]
		@property
		def TmOutNtfctn(self):
			return self._TmOutNtfctn

		@TmOutNtfctn.setter
		def TmOutNtfctn(self, value):
			self._TmOutNtfctn = value if type(value) != auto else self.make_default("TmOutNtfctn")

		@TmOutNtfctn.deleter
		def TmOutNtfctn(self):
			del self._TmOutNtfctn
			self._TmOutNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TmOutNtfctn', type=TimeOutNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

