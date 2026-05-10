from . import base_types
import FinancialInstrumentReportingEquityTradingActivityReportV01

class AUTH_040_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgEqtyTradgActvtyRpt"]
		@property
		def FinInstrmRptgEqtyTradgActvtyRpt(self):
			return self._FinInstrmRptgEqtyTradgActvtyRpt

		@FinInstrmRptgEqtyTradgActvtyRpt.setter
		def FinInstrmRptgEqtyTradgActvtyRpt(self, value):
			self._FinInstrmRptgEqtyTradgActvtyRpt = value if type(value) != auto else self.make_default("FinInstrmRptgEqtyTradgActvtyRpt")

		@FinInstrmRptgEqtyTradgActvtyRpt.deleter
		def FinInstrmRptgEqtyTradgActvtyRpt(self):
			del self._FinInstrmRptgEqtyTradgActvtyRpt
			self._FinInstrmRptgEqtyTradgActvtyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgEqtyTradgActvtyRpt', type=FinancialInstrumentReportingEquityTradingActivityReportV01, min=1, max=1, mutex_group=None, array=False),
		))

