# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TotalPortfolioValuationReportV01 import TotalPortfolioValuationReportV01

class SEMT_024_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:semt.024.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_TtlPrtflValtnRpt"]
		@property
		def TtlPrtflValtnRpt(self):
			return self._TtlPrtflValtnRpt

		@TtlPrtflValtnRpt.setter
		def TtlPrtflValtnRpt(self, value):
			self._TtlPrtflValtnRpt = value if type(value) != base_types.auto else self.make_default("TtlPrtflValtnRpt")

		@TtlPrtflValtnRpt.deleter
		def TtlPrtflValtnRpt(self):
			del self._TtlPrtflValtnRpt
			self._TtlPrtflValtnRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TtlPrtflValtnRpt', type=TotalPortfolioValuationReportV01, min=1, max=1, mutex_group=None, array=False),
		))