# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialBenchmarkReportV01 import FinancialBenchmarkReportV01

class AUTH_077_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.077.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FinBchmkRpt"]
		@property
		def FinBchmkRpt(self):
			return self._FinBchmkRpt

		@FinBchmkRpt.setter
		def FinBchmkRpt(self, value):
			self._FinBchmkRpt = value if type(value) != base_types.auto else self.make_default("FinBchmkRpt")

		@FinBchmkRpt.deleter
		def FinBchmkRpt(self):
			del self._FinBchmkRpt
			self._FinBchmkRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinBchmkRpt', type=FinancialBenchmarkReportV01, min=1, max=1, mutex_group=None, array=False),
		))