import base_types
import IntraBalanceMovementCancellationRequestV02

class CAMT_074_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntCxlReq"]
		@property
		def IntraBalMvmntCxlReq(self):
			return self._IntraBalMvmntCxlReq

		@IntraBalMvmntCxlReq.setter
		def IntraBalMvmntCxlReq(self, value):
			self._IntraBalMvmntCxlReq = value if type(value) != auto else self.make_default("IntraBalMvmntCxlReq")

		@IntraBalMvmntCxlReq.deleter
		def IntraBalMvmntCxlReq(self):
			del self._IntraBalMvmntCxlReq
			self._IntraBalMvmntCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntCxlReq', type=IntraBalanceMovementCancellationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

