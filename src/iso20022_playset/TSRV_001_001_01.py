from . import base_types
from .UndertakingIssuanceV01 import UndertakingIssuanceV01

class TSRV_001_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgIssnc"]
		@property
		def UdrtkgIssnc(self):
			return self._UdrtkgIssnc

		@UdrtkgIssnc.setter
		def UdrtkgIssnc(self, value):
			self._UdrtkgIssnc = value if type(value) != base_types.auto else self.make_default("UdrtkgIssnc")

		@UdrtkgIssnc.deleter
		def UdrtkgIssnc(self):
			del self._UdrtkgIssnc
			self._UdrtkgIssnc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgIssnc', type=UndertakingIssuanceV01, min=1, max=1, mutex_group=None, array=False),
		))

