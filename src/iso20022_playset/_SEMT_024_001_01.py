# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TotalPortfolioValuationReportV01

class SEMT_024_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:semt.024.001.01"
		_docname = "semt.024.001.01"

		__slots__ = ["_TtlPrtflValtnRpt"]
		@property
		def TtlPrtflValtnRpt(self):
			return self._TtlPrtflValtnRpt

		@TtlPrtflValtnRpt.setter
		def TtlPrtflValtnRpt(self, value):
			self._TtlPrtflValtnRpt = value if value is not None else base_types.UninitialisedField(self, 'TtlPrtflValtnRpt', TotalPortfolioValuationReportV01, False)

		@TtlPrtflValtnRpt.deleter
		def TtlPrtflValtnRpt(self):
			del self._TtlPrtflValtnRpt
			self._TtlPrtflValtnRpt = base_types.UninitialisedField(self, 'TtlPrtflValtnRpt', TotalPortfolioValuationReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TtlPrtflValtnRpt', type=TotalPortfolioValuationReportV01, min=1, max=1, mutex_group=None, array=False),
		))