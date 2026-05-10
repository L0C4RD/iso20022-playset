import base_types
import FinancialInstrumentReportingStatusAdviceV01

class AUTH_031_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgStsAdvc"]
		@property
		def FinInstrmRptgStsAdvc(self):
			return self._FinInstrmRptgStsAdvc

		@FinInstrmRptgStsAdvc.setter
		def FinInstrmRptgStsAdvc(self, value):
			self._FinInstrmRptgStsAdvc = value if type(value) != auto else self.make_default("FinInstrmRptgStsAdvc")

		@FinInstrmRptgStsAdvc.deleter
		def FinInstrmRptgStsAdvc(self):
			del self._FinInstrmRptgStsAdvc
			self._FinInstrmRptgStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgStsAdvc', type=FinancialInstrumentReportingStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

