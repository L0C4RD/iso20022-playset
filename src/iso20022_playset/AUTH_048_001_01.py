from . import base_types
from .FinancialInstrumentReportingCurrencyCodeReportV01 import FinancialInstrumentReportingCurrencyCodeReportV01

class AUTH_048_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgCcyCdRpt"]
		@property
		def FinInstrmRptgCcyCdRpt(self):
			return self._FinInstrmRptgCcyCdRpt

		@FinInstrmRptgCcyCdRpt.setter
		def FinInstrmRptgCcyCdRpt(self, value):
			self._FinInstrmRptgCcyCdRpt = value if type(value) != auto else self.make_default("FinInstrmRptgCcyCdRpt")

		@FinInstrmRptgCcyCdRpt.deleter
		def FinInstrmRptgCcyCdRpt(self):
			del self._FinInstrmRptgCcyCdRpt
			self._FinInstrmRptgCcyCdRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgCcyCdRpt', type=FinancialInstrumentReportingCurrencyCodeReportV01, min=1, max=1, mutex_group=None, array=False),
		))

