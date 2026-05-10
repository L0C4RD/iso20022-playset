import base_types
import FinancialInstrumentReportingInstrumentClassificationReportV01

class AUTH_050_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgInstrmClssfctnRpt"]
		@property
		def FinInstrmRptgInstrmClssfctnRpt(self):
			return self._FinInstrmRptgInstrmClssfctnRpt

		@FinInstrmRptgInstrmClssfctnRpt.setter
		def FinInstrmRptgInstrmClssfctnRpt(self, value):
			self._FinInstrmRptgInstrmClssfctnRpt = value if type(value) != auto else self.make_default("FinInstrmRptgInstrmClssfctnRpt")

		@FinInstrmRptgInstrmClssfctnRpt.deleter
		def FinInstrmRptgInstrmClssfctnRpt(self):
			del self._FinInstrmRptgInstrmClssfctnRpt
			self._FinInstrmRptgInstrmClssfctnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgInstrmClssfctnRpt', type=FinancialInstrumentReportingInstrumentClassificationReportV01, min=1, max=1, mutex_group=None, array=False),
		))

