from . import base_types
from .CustomerCreditTransferInitiationV12 import CustomerCreditTransferInitiationV12

class PAIN_001_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CstmrCdtTrfInitn"]
		@property
		def CstmrCdtTrfInitn(self):
			return self._CstmrCdtTrfInitn

		@CstmrCdtTrfInitn.setter
		def CstmrCdtTrfInitn(self, value):
			self._CstmrCdtTrfInitn = value if type(value) != auto else self.make_default("CstmrCdtTrfInitn")

		@CstmrCdtTrfInitn.deleter
		def CstmrCdtTrfInitn(self):
			del self._CstmrCdtTrfInitn
			self._CstmrCdtTrfInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrCdtTrfInitn', type=CustomerCreditTransferInitiationV12, min=1, max=1, mutex_group=None, array=False),
		))

