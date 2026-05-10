from . import base_types
from .FundDetailedConfirmedCashForecastReportV04 import FundDetailedConfirmedCashForecastReportV04

class CAMT_043_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FndDtldConfdCshFcstRpt"]
		@property
		def FndDtldConfdCshFcstRpt(self):
			return self._FndDtldConfdCshFcstRpt

		@FndDtldConfdCshFcstRpt.setter
		def FndDtldConfdCshFcstRpt(self, value):
			self._FndDtldConfdCshFcstRpt = value if type(value) != auto else self.make_default("FndDtldConfdCshFcstRpt")

		@FndDtldConfdCshFcstRpt.deleter
		def FndDtldConfdCshFcstRpt(self):
			del self._FndDtldConfdCshFcstRpt
			self._FndDtldConfdCshFcstRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndDtldConfdCshFcstRpt', type=FundDetailedConfirmedCashForecastReportV04, min=1, max=1, mutex_group=None, array=False),
		))

