import base_types
import SubscriptionBulkOrderV04

class SETR_007_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SbcptBlkOrdr"]
		@property
		def SbcptBlkOrdr(self):
			return self._SbcptBlkOrdr

		@SbcptBlkOrdr.setter
		def SbcptBlkOrdr(self, value):
			self._SbcptBlkOrdr = value if type(value) != auto else self.make_default("SbcptBlkOrdr")

		@SbcptBlkOrdr.deleter
		def SbcptBlkOrdr(self):
			del self._SbcptBlkOrdr
			self._SbcptBlkOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdr', type=SubscriptionBulkOrderV04, min=1, max=1, mutex_group=None, array=False),
		))

