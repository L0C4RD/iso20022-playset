from . import base_types
from ._UndertakingAmendmentRequestV01 import UndertakingAmendmentRequestV01

class TSRV_004_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgAmdmntReq"]
		@property
		def UdrtkgAmdmntReq(self):
			return self._UdrtkgAmdmntReq

		@UdrtkgAmdmntReq.setter
		def UdrtkgAmdmntReq(self, value):
			self._UdrtkgAmdmntReq = value if type(value) != base_types.auto else self.make_default("UdrtkgAmdmntReq")

		@UdrtkgAmdmntReq.deleter
		def UdrtkgAmdmntReq(self):
			del self._UdrtkgAmdmntReq
			self._UdrtkgAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmntReq', type=UndertakingAmendmentRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

