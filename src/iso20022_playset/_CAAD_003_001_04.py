from . import base_types
from ._BatchTransferInitiationV04 import BatchTransferInitiationV04

class CAAD_003_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_BtchTrfInitn"]
		@property
		def BtchTrfInitn(self):
			return self._BtchTrfInitn

		@BtchTrfInitn.setter
		def BtchTrfInitn(self, value):
			self._BtchTrfInitn = value if type(value) != base_types.auto else self.make_default("BtchTrfInitn")

		@BtchTrfInitn.deleter
		def BtchTrfInitn(self):
			del self._BtchTrfInitn
			self._BtchTrfInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BtchTrfInitn', type=BatchTransferInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))

