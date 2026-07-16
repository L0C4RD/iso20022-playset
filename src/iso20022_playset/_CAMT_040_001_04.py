# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FundEstimatedCashForecastReportV04

class CAMT_040_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.040.001.04"
		_docname = "camt.040.001.04"

		__slots__ = ["_FndEstmtdCshFcstRpt"]
		@property
		def FndEstmtdCshFcstRpt(self):
			return self._FndEstmtdCshFcstRpt

		@FndEstmtdCshFcstRpt.setter
		def FndEstmtdCshFcstRpt(self, value):
			self._FndEstmtdCshFcstRpt = value if value is not None else base_types.UninitialisedField(self, 'FndEstmtdCshFcstRpt', FundEstimatedCashForecastReportV04, False)

		@FndEstmtdCshFcstRpt.deleter
		def FndEstmtdCshFcstRpt(self):
			del self._FndEstmtdCshFcstRpt
			self._FndEstmtdCshFcstRpt = base_types.UninitialisedField(self, 'FndEstmtdCshFcstRpt', FundEstimatedCashForecastReportV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndEstmtdCshFcstRpt', type=FundEstimatedCashForecastReportV04, min=1, max=1, mutex_group=None, array=False),
		))