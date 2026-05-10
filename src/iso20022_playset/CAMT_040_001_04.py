from . import base_types
from .FundEstimatedCashForecastReportV04 import FundEstimatedCashForecastReportV04

class CAMT_040_001_04():

	class Document(base_types._BaseFieldType):

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

