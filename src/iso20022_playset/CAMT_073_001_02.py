from . import base_types
import IntraBalanceMovementModificationRequestStatusAdviceV02

class CAMT_073_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntModReqStsAdvc"]
		@property
		def IntraBalMvmntModReqStsAdvc(self):
			return self._IntraBalMvmntModReqStsAdvc

		@IntraBalMvmntModReqStsAdvc.setter
		def IntraBalMvmntModReqStsAdvc(self, value):
			self._IntraBalMvmntModReqStsAdvc = value if type(value) != auto else self.make_default("IntraBalMvmntModReqStsAdvc")

		@IntraBalMvmntModReqStsAdvc.deleter
		def IntraBalMvmntModReqStsAdvc(self):
			del self._IntraBalMvmntModReqStsAdvc
			self._IntraBalMvmntModReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntModReqStsAdvc', type=IntraBalanceMovementModificationRequestStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))

