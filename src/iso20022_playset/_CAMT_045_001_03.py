# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FundDetailedConfirmedCashForecastReportCancellationV03

class CAMT_045_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.045.001.03"
		_docname = "camt.045.001.03"

		__slots__ = ["_FndDtldConfdCshFcstRptCxl"]
		@property
		def FndDtldConfdCshFcstRptCxl(self):
			return self._FndDtldConfdCshFcstRptCxl

		@FndDtldConfdCshFcstRptCxl.setter
		def FndDtldConfdCshFcstRptCxl(self, value):
			self._FndDtldConfdCshFcstRptCxl = value if value is not None else base_types.UninitialisedField(self, 'FndDtldConfdCshFcstRptCxl', FundDetailedConfirmedCashForecastReportCancellationV03, False)

		@FndDtldConfdCshFcstRptCxl.deleter
		def FndDtldConfdCshFcstRptCxl(self):
			del self._FndDtldConfdCshFcstRptCxl
			self._FndDtldConfdCshFcstRptCxl = base_types.UninitialisedField(self, 'FndDtldConfdCshFcstRptCxl', FundDetailedConfirmedCashForecastReportCancellationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndDtldConfdCshFcstRptCxl', type=FundDetailedConfirmedCashForecastReportCancellationV03, min=1, max=1, mutex_group=None, array=False),
		))