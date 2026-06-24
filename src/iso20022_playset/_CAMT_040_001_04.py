# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FundEstimatedCashForecastReportV04 import FundEstimatedCashForecastReportV04

class CAMT_040_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:camt.040.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_FndEstmtdCshFcstRpt"]
		@property
		def FndEstmtdCshFcstRpt(self):
			return self._FndEstmtdCshFcstRpt

		@FndEstmtdCshFcstRpt.setter
		def FndEstmtdCshFcstRpt(self, value):
			self._FndEstmtdCshFcstRpt = value if type(value) != base_types.auto else self.make_default("FndEstmtdCshFcstRpt")

		@FndEstmtdCshFcstRpt.deleter
		def FndEstmtdCshFcstRpt(self):
			del self._FndEstmtdCshFcstRpt
			self._FndEstmtdCshFcstRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndEstmtdCshFcstRpt', type=FundEstimatedCashForecastReportV04, min=1, max=1, mutex_group=None, array=False),
		))