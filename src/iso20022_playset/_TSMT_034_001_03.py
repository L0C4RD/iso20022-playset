from . import base_types
from ._StatusExtensionRejectionNotificationV03 import StatusExtensionRejectionNotificationV03

class TSMT_034_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsXtnsnRjctnNtfctn"]
		@property
		def StsXtnsnRjctnNtfctn(self):
			return self._StsXtnsnRjctnNtfctn

		@StsXtnsnRjctnNtfctn.setter
		def StsXtnsnRjctnNtfctn(self, value):
			self._StsXtnsnRjctnNtfctn = value if type(value) != base_types.auto else self.make_default("StsXtnsnRjctnNtfctn")

		@StsXtnsnRjctnNtfctn.deleter
		def StsXtnsnRjctnNtfctn(self):
			del self._StsXtnsnRjctnNtfctn
			self._StsXtnsnRjctnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnRjctnNtfctn', type=StatusExtensionRejectionNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))

