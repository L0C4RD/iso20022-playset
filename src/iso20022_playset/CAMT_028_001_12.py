from . import base_types
from .AdditionalPaymentInformationV12 import AdditionalPaymentInformationV12

class CAMT_028_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AddtlPmtInf"]
		@property
		def AddtlPmtInf(self):
			return self._AddtlPmtInf

		@AddtlPmtInf.setter
		def AddtlPmtInf(self, value):
			self._AddtlPmtInf = value if type(value) != auto else self.make_default("AddtlPmtInf")

		@AddtlPmtInf.deleter
		def AddtlPmtInf(self):
			del self._AddtlPmtInf
			self._AddtlPmtInf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AddtlPmtInf', type=AdditionalPaymentInformationV12, min=1, max=1, mutex_group=None, array=False),
		))

