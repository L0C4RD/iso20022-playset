from . import base_types
import FinancialBenchmarkReportV01

class AUTH_077_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinBchmkRpt"]
		@property
		def FinBchmkRpt(self):
			return self._FinBchmkRpt

		@FinBchmkRpt.setter
		def FinBchmkRpt(self, value):
			self._FinBchmkRpt = value if type(value) != auto else self.make_default("FinBchmkRpt")

		@FinBchmkRpt.deleter
		def FinBchmkRpt(self):
			del self._FinBchmkRpt
			self._FinBchmkRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinBchmkRpt', type=FinancialBenchmarkReportV01, min=1, max=1, mutex_group=None, array=False),
		))

