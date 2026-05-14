from . import base_types
from ._FIToFIPaymentReversalV14 import FIToFIPaymentReversalV14

class PACS_007_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FIToFIPmtRvsl"]
		@property
		def FIToFIPmtRvsl(self):
			return self._FIToFIPmtRvsl

		@FIToFIPmtRvsl.setter
		def FIToFIPmtRvsl(self, value):
			self._FIToFIPmtRvsl = value if type(value) != base_types.auto else self.make_default("FIToFIPmtRvsl")

		@FIToFIPmtRvsl.deleter
		def FIToFIPmtRvsl(self):
			del self._FIToFIPmtRvsl
			self._FIToFIPmtRvsl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFIPmtRvsl', type=FIToFIPaymentReversalV14, min=1, max=1, mutex_group=None, array=False),
		))

