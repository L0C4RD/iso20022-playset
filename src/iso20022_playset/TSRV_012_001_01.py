from . import base_types
import UndertakingTerminationNotificationV01

class TSRV_012_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgTermntnNtfctn"]
		@property
		def UdrtkgTermntnNtfctn(self):
			return self._UdrtkgTermntnNtfctn

		@UdrtkgTermntnNtfctn.setter
		def UdrtkgTermntnNtfctn(self, value):
			self._UdrtkgTermntnNtfctn = value if type(value) != auto else self.make_default("UdrtkgTermntnNtfctn")

		@UdrtkgTermntnNtfctn.deleter
		def UdrtkgTermntnNtfctn(self):
			del self._UdrtkgTermntnNtfctn
			self._UdrtkgTermntnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgTermntnNtfctn', type=UndertakingTerminationNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))

