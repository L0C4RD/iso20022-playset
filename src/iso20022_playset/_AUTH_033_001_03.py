from . import base_types
from .FinancialInstrumentReportingNonEquityTransparencyDataReportV03 import FinancialInstrumentReportingNonEquityTransparencyDataReportV03

class AUTH_033_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgNonEqtyTrnsprncyDataRpt"]
		@property
		def FinInstrmRptgNonEqtyTrnsprncyDataRpt(self):
			return self._FinInstrmRptgNonEqtyTrnsprncyDataRpt

		@FinInstrmRptgNonEqtyTrnsprncyDataRpt.setter
		def FinInstrmRptgNonEqtyTrnsprncyDataRpt(self, value):
			self._FinInstrmRptgNonEqtyTrnsprncyDataRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgNonEqtyTrnsprncyDataRpt")

		@FinInstrmRptgNonEqtyTrnsprncyDataRpt.deleter
		def FinInstrmRptgNonEqtyTrnsprncyDataRpt(self):
			del self._FinInstrmRptgNonEqtyTrnsprncyDataRpt
			self._FinInstrmRptgNonEqtyTrnsprncyDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgNonEqtyTrnsprncyDataRpt', type=FinancialInstrumentReportingNonEquityTransparencyDataReportV03, min=1, max=1, mutex_group=None, array=False),
		))

