from . import base_types
from .IntraBalanceMovementModificationQueryV02 import IntraBalanceMovementModificationQueryV02

class CAMT_080_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntModQry"]
		@property
		def IntraBalMvmntModQry(self):
			return self._IntraBalMvmntModQry

		@IntraBalMvmntModQry.setter
		def IntraBalMvmntModQry(self, value):
			self._IntraBalMvmntModQry = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntModQry")

		@IntraBalMvmntModQry.deleter
		def IntraBalMvmntModQry(self):
			del self._IntraBalMvmntModQry
			self._IntraBalMvmntModQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntModQry', type=IntraBalanceMovementModificationQueryV02, min=1, max=1, mutex_group=None, array=False),
		))

