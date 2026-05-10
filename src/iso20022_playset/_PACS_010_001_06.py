from . import base_types
from ._FinancialInstitutionDirectDebitV06 import FinancialInstitutionDirectDebitV06

class PACS_010_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FIDrctDbt"]
		@property
		def FIDrctDbt(self):
			return self._FIDrctDbt

		@FIDrctDbt.setter
		def FIDrctDbt(self, value):
			self._FIDrctDbt = value if type(value) != base_types.auto else self.make_default("FIDrctDbt")

		@FIDrctDbt.deleter
		def FIDrctDbt(self):
			del self._FIDrctDbt
			self._FIDrctDbt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIDrctDbt', type=FinancialInstitutionDirectDebitV06, min=1, max=1, mutex_group=None, array=False),
		))

