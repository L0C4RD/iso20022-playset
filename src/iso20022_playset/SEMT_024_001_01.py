import base_types
import TotalPortfolioValuationReportV01

class SEMT_024_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TtlPrtflValtnRpt"]
		@property
		def TtlPrtflValtnRpt(self):
			return self._TtlPrtflValtnRpt

		@TtlPrtflValtnRpt.setter
		def TtlPrtflValtnRpt(self, value):
			self._TtlPrtflValtnRpt = value if type(value) != auto else self.make_default("TtlPrtflValtnRpt")

		@TtlPrtflValtnRpt.deleter
		def TtlPrtflValtnRpt(self):
			del self._TtlPrtflValtnRpt
			self._TtlPrtflValtnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TtlPrtflValtnRpt', type=TotalPortfolioValuationReportV01, min=1, max=1, mutex_group=None, array=False),
		))

