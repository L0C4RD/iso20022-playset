from . import base_types
from ._UndertakingAmendmentResponseNotificationV01 import UndertakingAmendmentResponseNotificationV01

class TSRV_009_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgAmdmntRspnNtfctn"]
		@property
		def UdrtkgAmdmntRspnNtfctn(self):
			return self._UdrtkgAmdmntRspnNtfctn

		@UdrtkgAmdmntRspnNtfctn.setter
		def UdrtkgAmdmntRspnNtfctn(self, value):
			self._UdrtkgAmdmntRspnNtfctn = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntRspnNtfctn")

		@UdrtkgAmdmntRspnNtfctn.deleter
		def UdrtkgAmdmntRspnNtfctn(self):
			del self._UdrtkgAmdmntRspnNtfctn
			self._UdrtkgAmdmntRspnNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmntRspnNtfctn', type=UndertakingAmendmentResponseNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))

