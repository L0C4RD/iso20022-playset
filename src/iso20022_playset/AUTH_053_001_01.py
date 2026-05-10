import base_types
import FinancialInstrumentReportingTradingVolumeCapResultReportV01

class AUTH_053_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgTradgVolCapRsltRpt"]
		@property
		def FinInstrmRptgTradgVolCapRsltRpt(self):
			return self._FinInstrmRptgTradgVolCapRsltRpt

		@FinInstrmRptgTradgVolCapRsltRpt.setter
		def FinInstrmRptgTradgVolCapRsltRpt(self, value):
			self._FinInstrmRptgTradgVolCapRsltRpt = value if type(value) != auto else self.make_default("FinInstrmRptgTradgVolCapRsltRpt")

		@FinInstrmRptgTradgVolCapRsltRpt.deleter
		def FinInstrmRptgTradgVolCapRsltRpt(self):
			del self._FinInstrmRptgTradgVolCapRsltRpt
			self._FinInstrmRptgTradgVolCapRsltRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgTradgVolCapRsltRpt', type=FinancialInstrumentReportingTradingVolumeCapResultReportV01, min=1, max=1, mutex_group=None, array=False),
		))

