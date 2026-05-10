from . import base_types
from .IntraBalanceMovementCancellationQueryV02 import IntraBalanceMovementCancellationQueryV02

class CAMT_082_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntCxlQry"]
		@property
		def IntraBalMvmntCxlQry(self):
			return self._IntraBalMvmntCxlQry

		@IntraBalMvmntCxlQry.setter
		def IntraBalMvmntCxlQry(self, value):
			self._IntraBalMvmntCxlQry = value if type(value) != auto else self.make_default("IntraBalMvmntCxlQry")

		@IntraBalMvmntCxlQry.deleter
		def IntraBalMvmntCxlQry(self):
			del self._IntraBalMvmntCxlQry
			self._IntraBalMvmntCxlQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntCxlQry', type=IntraBalanceMovementCancellationQueryV02, min=1, max=1, mutex_group=None, array=False),
		))

