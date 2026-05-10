from . import base_types
from ._FinancialInstrumentReportingTradingVolumeCapDataReportV01 import FinancialInstrumentReportingTradingVolumeCapDataReportV01

class AUTH_035_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgTradgVolCapDataRpt"]
		@property
		def FinInstrmRptgTradgVolCapDataRpt(self):
			return self._FinInstrmRptgTradgVolCapDataRpt

		@FinInstrmRptgTradgVolCapDataRpt.setter
		def FinInstrmRptgTradgVolCapDataRpt(self, value):
			self._FinInstrmRptgTradgVolCapDataRpt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgTradgVolCapDataRpt")

		@FinInstrmRptgTradgVolCapDataRpt.deleter
		def FinInstrmRptgTradgVolCapDataRpt(self):
			del self._FinInstrmRptgTradgVolCapDataRpt
			self._FinInstrmRptgTradgVolCapDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgTradgVolCapDataRpt', type=FinancialInstrumentReportingTradingVolumeCapDataReportV01, min=1, max=1, mutex_group=None, array=False),
		))

