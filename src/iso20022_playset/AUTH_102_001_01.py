from . import base_types
import FinancialInstrumentReportingCancellationReportV01

class AUTH_102_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgCxlRpt"]
		@property
		def FinInstrmRptgCxlRpt(self):
			return self._FinInstrmRptgCxlRpt

		@FinInstrmRptgCxlRpt.setter
		def FinInstrmRptgCxlRpt(self, value):
			self._FinInstrmRptgCxlRpt = value if type(value) != auto else self.make_default("FinInstrmRptgCxlRpt")

		@FinInstrmRptgCxlRpt.deleter
		def FinInstrmRptgCxlRpt(self):
			del self._FinInstrmRptgCxlRpt
			self._FinInstrmRptgCxlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgCxlRpt', type=FinancialInstrumentReportingCancellationReportV01, min=1, max=1, mutex_group=None, array=False),
		))

