from . import base_types
from .FinancialInstitutionCreditTransferV12 import FinancialInstitutionCreditTransferV12

class PACS_009_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FICdtTrf"]
		@property
		def FICdtTrf(self):
			return self._FICdtTrf

		@FICdtTrf.setter
		def FICdtTrf(self, value):
			self._FICdtTrf = value if type(value) != auto else self.make_default("FICdtTrf")

		@FICdtTrf.deleter
		def FICdtTrf(self):
			del self._FICdtTrf
			self._FICdtTrf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FICdtTrf', type=FinancialInstitutionCreditTransferV12, min=1, max=1, mutex_group=None, array=False),
		))

