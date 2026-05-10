from . import base_types
from .UndertakingAmendmentV01 import UndertakingAmendmentV01

class TSRV_005_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_UdrtkgAmdmnt"]
		@property
		def UdrtkgAmdmnt(self):
			return self._UdrtkgAmdmnt

		@UdrtkgAmdmnt.setter
		def UdrtkgAmdmnt(self, value):
			self._UdrtkgAmdmnt = value if type(value) != auto else self.make_default("UdrtkgAmdmnt")

		@UdrtkgAmdmnt.deleter
		def UdrtkgAmdmnt(self):
			del self._UdrtkgAmdmnt
			self._UdrtkgAmdmnt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgAmdmnt', type=UndertakingAmendmentV01, min=1, max=1, mutex_group=None, array=False),
		))

