from . import base_types
from .IntraBalanceMovementStatusAdviceV02 import IntraBalanceMovementStatusAdviceV02

class CAMT_067_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntStsAdvc"]
		@property
		def IntraBalMvmntStsAdvc(self):
			return self._IntraBalMvmntStsAdvc

		@IntraBalMvmntStsAdvc.setter
		def IntraBalMvmntStsAdvc(self, value):
			self._IntraBalMvmntStsAdvc = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntStsAdvc")

		@IntraBalMvmntStsAdvc.deleter
		def IntraBalMvmntStsAdvc(self):
			del self._IntraBalMvmntStsAdvc
			self._IntraBalMvmntStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntStsAdvc', type=IntraBalanceMovementStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))

