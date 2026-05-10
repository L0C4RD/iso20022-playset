from . import base_types
import FinancialInstrumentReportingMarketIdentificationCodeReportV02

class AUTH_049_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgMktIdCdRpt"]
		@property
		def FinInstrmRptgMktIdCdRpt(self):
			return self._FinInstrmRptgMktIdCdRpt

		@FinInstrmRptgMktIdCdRpt.setter
		def FinInstrmRptgMktIdCdRpt(self, value):
			self._FinInstrmRptgMktIdCdRpt = value if type(value) != auto else self.make_default("FinInstrmRptgMktIdCdRpt")

		@FinInstrmRptgMktIdCdRpt.deleter
		def FinInstrmRptgMktIdCdRpt(self):
			del self._FinInstrmRptgMktIdCdRpt
			self._FinInstrmRptgMktIdCdRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgMktIdCdRpt', type=FinancialInstrumentReportingMarketIdentificationCodeReportV02, min=1, max=1, mutex_group=None, array=False),
		))

