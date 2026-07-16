# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FundDetailedEstimatedCashForecastReportV04

class CAMT_042_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.042.001.04"
		_docname = "camt.042.001.04"

		__slots__ = ["_FndDtldEstmtdCshFcstRpt"]
		@property
		def FndDtldEstmtdCshFcstRpt(self):
			return self._FndDtldEstmtdCshFcstRpt

		@FndDtldEstmtdCshFcstRpt.setter
		def FndDtldEstmtdCshFcstRpt(self, value):
			self._FndDtldEstmtdCshFcstRpt = value if value is not None else base_types.UninitialisedField(self, 'FndDtldEstmtdCshFcstRpt', FundDetailedEstimatedCashForecastReportV04, False)

		@FndDtldEstmtdCshFcstRpt.deleter
		def FndDtldEstmtdCshFcstRpt(self):
			del self._FndDtldEstmtdCshFcstRpt
			self._FndDtldEstmtdCshFcstRpt = base_types.UninitialisedField(self, 'FndDtldEstmtdCshFcstRpt', FundDetailedEstimatedCashForecastReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndDtldEstmtdCshFcstRpt', type=FundDetailedEstimatedCashForecastReportV04, min=1, max=1, mutex_group=None, array=False),
		))