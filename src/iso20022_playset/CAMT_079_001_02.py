from . import base_types
import IntraBalanceMovementQueryResponseV02

class CAMT_079_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntQryRspn"]
		@property
		def IntraBalMvmntQryRspn(self):
			return self._IntraBalMvmntQryRspn

		@IntraBalMvmntQryRspn.setter
		def IntraBalMvmntQryRspn(self, value):
			self._IntraBalMvmntQryRspn = value if type(value) != auto else self.make_default("IntraBalMvmntQryRspn")

		@IntraBalMvmntQryRspn.deleter
		def IntraBalMvmntQryRspn(self):
			del self._IntraBalMvmntQryRspn
			self._IntraBalMvmntQryRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntQryRspn', type=IntraBalanceMovementQueryResponseV02, min=1, max=1, mutex_group=None, array=False),
		))

