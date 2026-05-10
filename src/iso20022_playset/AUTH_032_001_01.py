import base_types
import FinancialInstrumentReportingEquityTransparencyDataReportV01

class AUTH_032_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgEqtyTrnsprncyDataRpt"]
		@property
		def FinInstrmRptgEqtyTrnsprncyDataRpt(self):
			return self._FinInstrmRptgEqtyTrnsprncyDataRpt

		@FinInstrmRptgEqtyTrnsprncyDataRpt.setter
		def FinInstrmRptgEqtyTrnsprncyDataRpt(self, value):
			self._FinInstrmRptgEqtyTrnsprncyDataRpt = value if type(value) != auto else self.make_default("FinInstrmRptgEqtyTrnsprncyDataRpt")

		@FinInstrmRptgEqtyTrnsprncyDataRpt.deleter
		def FinInstrmRptgEqtyTrnsprncyDataRpt(self):
			del self._FinInstrmRptgEqtyTrnsprncyDataRpt
			self._FinInstrmRptgEqtyTrnsprncyDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgEqtyTrnsprncyDataRpt', type=FinancialInstrumentReportingEquityTransparencyDataReportV01, min=1, max=1, mutex_group=None, array=False),
		))

