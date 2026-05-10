from . import base_types
from .IntraBalanceMovementQueryV02 import IntraBalanceMovementQueryV02

class CAMT_078_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntQry"]
		@property
		def IntraBalMvmntQry(self):
			return self._IntraBalMvmntQry

		@IntraBalMvmntQry.setter
		def IntraBalMvmntQry(self, value):
			self._IntraBalMvmntQry = value if type(value) != auto else self.make_default("IntraBalMvmntQry")

		@IntraBalMvmntQry.deleter
		def IntraBalMvmntQry(self):
			del self._IntraBalMvmntQry
			self._IntraBalMvmntQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntQry', type=IntraBalanceMovementQueryV02, min=1, max=1, mutex_group=None, array=False),
		))

