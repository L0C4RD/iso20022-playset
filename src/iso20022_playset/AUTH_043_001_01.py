from . import base_types
from .FinancialInstrumentReportingReferenceDataIndexReportV01 import FinancialInstrumentReportingReferenceDataIndexReportV01

class AUTH_043_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgRefDataIndxRpt"]
		@property
		def FinInstrmRptgRefDataIndxRpt(self):
			return self._FinInstrmRptgRefDataIndxRpt

		@FinInstrmRptgRefDataIndxRpt.setter
		def FinInstrmRptgRefDataIndxRpt(self, value):
			self._FinInstrmRptgRefDataIndxRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgRefDataIndxRpt")

		@FinInstrmRptgRefDataIndxRpt.deleter
		def FinInstrmRptgRefDataIndxRpt(self):
			del self._FinInstrmRptgRefDataIndxRpt
			self._FinInstrmRptgRefDataIndxRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgRefDataIndxRpt', type=FinancialInstrumentReportingReferenceDataIndexReportV01, min=1, max=1, mutex_group=None, array=False),
		))

