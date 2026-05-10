from . import base_types
from .IntraBalanceMovementModificationRequestV02 import IntraBalanceMovementModificationRequestV02

class CAMT_072_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntModReq"]
		@property
		def IntraBalMvmntModReq(self):
			return self._IntraBalMvmntModReq

		@IntraBalMvmntModReq.setter
		def IntraBalMvmntModReq(self, value):
			self._IntraBalMvmntModReq = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntModReq")

		@IntraBalMvmntModReq.deleter
		def IntraBalMvmntModReq(self):
			del self._IntraBalMvmntModReq
			self._IntraBalMvmntModReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntModReq', type=IntraBalanceMovementModificationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

