from . import base_types
from ._UndertakingNonExtensionRequestV01 import UndertakingNonExtensionRequestV01

class TSRV_010_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgNonXtnsnReq"]
		@property
		def UdrtkgNonXtnsnReq(self):
			return self._UdrtkgNonXtnsnReq

		@UdrtkgNonXtnsnReq.setter
		def UdrtkgNonXtnsnReq(self, value):
			self._UdrtkgNonXtnsnReq = value if type(value) != base_types.auto else self.make_default("UdrtkgNonXtnsnReq")

		@UdrtkgNonXtnsnReq.deleter
		def UdrtkgNonXtnsnReq(self):
			del self._UdrtkgNonXtnsnReq
			self._UdrtkgNonXtnsnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgNonXtnsnReq', type=UndertakingNonExtensionRequestV01, min=1, max=1, mutex_group=None, array=False),
		))

