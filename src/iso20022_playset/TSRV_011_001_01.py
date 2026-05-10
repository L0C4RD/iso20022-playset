from . import base_types
from .UndertakingNonExtensionNotificationV01 import UndertakingNonExtensionNotificationV01

class TSRV_011_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgNonXtnsnNtfctn"]
		@property
		def UdrtkgNonXtnsnNtfctn(self):
			return self._UdrtkgNonXtnsnNtfctn

		@UdrtkgNonXtnsnNtfctn.setter
		def UdrtkgNonXtnsnNtfctn(self, value):
			self._UdrtkgNonXtnsnNtfctn = value if type(value) != auto else self.make_default("UdrtkgNonXtnsnNtfctn")

		@UdrtkgNonXtnsnNtfctn.deleter
		def UdrtkgNonXtnsnNtfctn(self):
			del self._UdrtkgNonXtnsnNtfctn
			self._UdrtkgNonXtnsnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgNonXtnsnNtfctn', type=UndertakingNonExtensionNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))

