from . import base_types
from .AmendmentRejectionNotificationV03 import AmendmentRejectionNotificationV03

class TSMT_008_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AmdmntRjctnNtfctn"]
		@property
		def AmdmntRjctnNtfctn(self):
			return self._AmdmntRjctnNtfctn

		@AmdmntRjctnNtfctn.setter
		def AmdmntRjctnNtfctn(self, value):
			self._AmdmntRjctnNtfctn = value if type(value) != auto else self.make_default("AmdmntRjctnNtfctn")

		@AmdmntRjctnNtfctn.deleter
		def AmdmntRjctnNtfctn(self):
			del self._AmdmntRjctnNtfctn
			self._AmdmntRjctnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AmdmntRjctnNtfctn', type=AmendmentRejectionNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

