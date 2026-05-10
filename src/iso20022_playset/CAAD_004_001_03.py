import base_types
import BatchTransferResponseV03

class CAAD_004_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BtchTrfRspn"]
		@property
		def BtchTrfRspn(self):
			return self._BtchTrfRspn

		@BtchTrfRspn.setter
		def BtchTrfRspn(self, value):
			self._BtchTrfRspn = value if type(value) != auto else self.make_default("BtchTrfRspn")

		@BtchTrfRspn.deleter
		def BtchTrfRspn(self):
			del self._BtchTrfRspn
			self._BtchTrfRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchTrfRspn', type=BatchTransferResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

