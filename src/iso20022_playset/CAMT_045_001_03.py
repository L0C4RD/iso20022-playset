import base_types
import FundDetailedConfirmedCashForecastReportCancellationV03

class CAMT_045_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FndDtldConfdCshFcstRptCxl"]
		@property
		def FndDtldConfdCshFcstRptCxl(self):
			return self._FndDtldConfdCshFcstRptCxl

		@FndDtldConfdCshFcstRptCxl.setter
		def FndDtldConfdCshFcstRptCxl(self, value):
			self._FndDtldConfdCshFcstRptCxl = value if type(value) != auto else self.make_default("FndDtldConfdCshFcstRptCxl")

		@FndDtldConfdCshFcstRptCxl.deleter
		def FndDtldConfdCshFcstRptCxl(self):
			del self._FndDtldConfdCshFcstRptCxl
			self._FndDtldConfdCshFcstRptCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndDtldConfdCshFcstRptCxl', type=FundDetailedConfirmedCashForecastReportCancellationV03, min=1, max=1, mutex_group=None, array=False),
		))

