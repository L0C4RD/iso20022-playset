# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialBenchmarkReportV01

class AUTH_077_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.077.001.01"
		_docname = "auth.077.001.01"

		__slots__ = ["_FinBchmkRpt"]
		@property
		def FinBchmkRpt(self):
			return self._FinBchmkRpt

		@FinBchmkRpt.setter
		def FinBchmkRpt(self, value):
			self._FinBchmkRpt = value if value is not None else base_types.UninitialisedField(self, 'FinBchmkRpt', FinancialBenchmarkReportV01, False)

		@FinBchmkRpt.deleter
		def FinBchmkRpt(self):
			del self._FinBchmkRpt
			self._FinBchmkRpt = base_types.UninitialisedField(self, 'FinBchmkRpt', FinancialBenchmarkReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinBchmkRpt', type=FinancialBenchmarkReportV01, min=1, max=1, mutex_group=None, array=False),
		))