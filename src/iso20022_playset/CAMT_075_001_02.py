from . import base_types
import IntraBalanceMovementCancellationRequestStatusAdviceV02

class CAMT_075_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntCxlReqStsAdvc"]
		@property
		def IntraBalMvmntCxlReqStsAdvc(self):
			return self._IntraBalMvmntCxlReqStsAdvc

		@IntraBalMvmntCxlReqStsAdvc.setter
		def IntraBalMvmntCxlReqStsAdvc(self, value):
			self._IntraBalMvmntCxlReqStsAdvc = value if type(value) != auto else self.make_default("IntraBalMvmntCxlReqStsAdvc")

		@IntraBalMvmntCxlReqStsAdvc.deleter
		def IntraBalMvmntCxlReqStsAdvc(self):
			del self._IntraBalMvmntCxlReqStsAdvc
			self._IntraBalMvmntCxlReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntCxlReqStsAdvc', type=IntraBalanceMovementCancellationRequestStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))

