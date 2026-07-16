# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FundConfirmedCashForecastReportCancellationV03

class CAMT_044_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.044.001.03"
		_docname = "camt.044.001.03"

		__slots__ = ["_FndConfdCshFcstRptCxl"]
		@property
		def FndConfdCshFcstRptCxl(self):
			return self._FndConfdCshFcstRptCxl

		@FndConfdCshFcstRptCxl.setter
		def FndConfdCshFcstRptCxl(self, value):
			self._FndConfdCshFcstRptCxl = value if value is not None else base_types.UninitialisedField(self, 'FndConfdCshFcstRptCxl', FundConfirmedCashForecastReportCancellationV03, False)

		@FndConfdCshFcstRptCxl.deleter
		def FndConfdCshFcstRptCxl(self):
			del self._FndConfdCshFcstRptCxl
			self._FndConfdCshFcstRptCxl = base_types.UninitialisedField(self, 'FndConfdCshFcstRptCxl', FundConfirmedCashForecastReportCancellationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndConfdCshFcstRptCxl', type=FundConfirmedCashForecastReportCancellationV03, min=1, max=1, mutex_group=None, array=False),
		))