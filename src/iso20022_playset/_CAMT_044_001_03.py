from . import base_types
from ._FundConfirmedCashForecastReportCancellationV03 import FundConfirmedCashForecastReportCancellationV03

class CAMT_044_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FndConfdCshFcstRptCxl"]
		@property
		def FndConfdCshFcstRptCxl(self):
			return self._FndConfdCshFcstRptCxl

		@FndConfdCshFcstRptCxl.setter
		def FndConfdCshFcstRptCxl(self, value):
			self._FndConfdCshFcstRptCxl = value if type(value) != base_types.auto else self.make_default("FndConfdCshFcstRptCxl")

		@FndConfdCshFcstRptCxl.deleter
		def FndConfdCshFcstRptCxl(self):
			del self._FndConfdCshFcstRptCxl
			self._FndConfdCshFcstRptCxl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndConfdCshFcstRptCxl', type=FundConfirmedCashForecastReportCancellationV03, min=1, max=1, mutex_group=None, array=False),
		))

