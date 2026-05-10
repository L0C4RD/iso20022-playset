from . import base_types
from .RedemptionBulkOrderV04 import RedemptionBulkOrderV04

class SETR_001_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RedBlkOrdr"]
		@property
		def RedBlkOrdr(self):
			return self._RedBlkOrdr

		@RedBlkOrdr.setter
		def RedBlkOrdr(self, value):
			self._RedBlkOrdr = value if type(value) != auto else self.make_default("RedBlkOrdr")

		@RedBlkOrdr.deleter
		def RedBlkOrdr(self):
			del self._RedBlkOrdr
			self._RedBlkOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedBlkOrdr', type=RedemptionBulkOrderV04, min=1, max=1, mutex_group=None, array=False),
		))

