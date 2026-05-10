import base_types
import FundConfirmedCashForecastReportV04

class CAMT_041_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FndConfdCshFcstRpt"]
		@property
		def FndConfdCshFcstRpt(self):
			return self._FndConfdCshFcstRpt

		@FndConfdCshFcstRpt.setter
		def FndConfdCshFcstRpt(self, value):
			self._FndConfdCshFcstRpt = value if type(value) != auto else self.make_default("FndConfdCshFcstRpt")

		@FndConfdCshFcstRpt.deleter
		def FndConfdCshFcstRpt(self):
			del self._FndConfdCshFcstRpt
			self._FndConfdCshFcstRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FndConfdCshFcstRpt', type=FundConfirmedCashForecastReportV04, min=1, max=1, mutex_group=None, array=False),
		))

