from . import base_types
from ._FinancialInstrumentReportingNonEquityTradingActivityReportV01 import FinancialInstrumentReportingNonEquityTradingActivityReportV01

class AUTH_041_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgNonEqtyTradgActvtyRpt"]
		@property
		def FinInstrmRptgNonEqtyTradgActvtyRpt(self):
			return self._FinInstrmRptgNonEqtyTradgActvtyRpt

		@FinInstrmRptgNonEqtyTradgActvtyRpt.setter
		def FinInstrmRptgNonEqtyTradgActvtyRpt(self, value):
			self._FinInstrmRptgNonEqtyTradgActvtyRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgNonEqtyTradgActvtyRpt")

		@FinInstrmRptgNonEqtyTradgActvtyRpt.deleter
		def FinInstrmRptgNonEqtyTradgActvtyRpt(self):
			del self._FinInstrmRptgNonEqtyTradgActvtyRpt
			self._FinInstrmRptgNonEqtyTradgActvtyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgNonEqtyTradgActvtyRpt', type=FinancialInstrumentReportingNonEquityTradingActivityReportV01, min=1, max=1, mutex_group=None, array=False),
		))

