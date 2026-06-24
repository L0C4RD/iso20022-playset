# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FundDetailedConfirmedCashForecastReportV04 import FundDetailedConfirmedCashForecastReportV04

class CAMT_043_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.043.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_FndDtldConfdCshFcstRpt"]
		@property
		def FndDtldConfdCshFcstRpt(self):
			return self._FndDtldConfdCshFcstRpt

		@FndDtldConfdCshFcstRpt.setter
		def FndDtldConfdCshFcstRpt(self, value):
			self._FndDtldConfdCshFcstRpt = value if type(value) != base_types.auto else self.make_default("FndDtldConfdCshFcstRpt")

		@FndDtldConfdCshFcstRpt.deleter
		def FndDtldConfdCshFcstRpt(self):
			del self._FndDtldConfdCshFcstRpt
			self._FndDtldConfdCshFcstRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndDtldConfdCshFcstRpt', type=FundDetailedConfirmedCashForecastReportV04, min=1, max=1, mutex_group=None, array=False),
		))