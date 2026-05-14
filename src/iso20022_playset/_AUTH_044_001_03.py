from . import base_types
from ._FinancialInstrumentReportingEquityTradingActivityResultV03 import FinancialInstrumentReportingEquityTradingActivityResultV03

class AUTH_044_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgEqtyTradgActvtyRslt"]
		@property
		def FinInstrmRptgEqtyTradgActvtyRslt(self):
			return self._FinInstrmRptgEqtyTradgActvtyRslt

		@FinInstrmRptgEqtyTradgActvtyRslt.setter
		def FinInstrmRptgEqtyTradgActvtyRslt(self, value):
			self._FinInstrmRptgEqtyTradgActvtyRslt = value if type(value) != base_types.auto else self.make_default("FinInstrmRptgEqtyTradgActvtyRslt")

		@FinInstrmRptgEqtyTradgActvtyRslt.deleter
		def FinInstrmRptgEqtyTradgActvtyRslt(self):
			del self._FinInstrmRptgEqtyTradgActvtyRslt
			self._FinInstrmRptgEqtyTradgActvtyRslt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgEqtyTradgActvtyRslt', type=FinancialInstrumentReportingEquityTradingActivityResultV03, min=1, max=1, mutex_group=None, array=False),
		))

