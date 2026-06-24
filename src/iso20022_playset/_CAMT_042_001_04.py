# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FundDetailedEstimatedCashForecastReportV04 import FundDetailedEstimatedCashForecastReportV04

class CAMT_042_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.042.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_FndDtldEstmtdCshFcstRpt"]
		@property
		def FndDtldEstmtdCshFcstRpt(self):
			return self._FndDtldEstmtdCshFcstRpt

		@FndDtldEstmtdCshFcstRpt.setter
		def FndDtldEstmtdCshFcstRpt(self, value):
			self._FndDtldEstmtdCshFcstRpt = value if type(value) != base_types.auto else self.make_default("FndDtldEstmtdCshFcstRpt")

		@FndDtldEstmtdCshFcstRpt.deleter
		def FndDtldEstmtdCshFcstRpt(self):
			del self._FndDtldEstmtdCshFcstRpt
			self._FndDtldEstmtdCshFcstRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndDtldEstmtdCshFcstRpt', type=FundDetailedEstimatedCashForecastReportV04, min=1, max=1, mutex_group=None, array=False),
		))