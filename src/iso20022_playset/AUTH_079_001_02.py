import base_types
import SecuritiesFinancingReportingTransactionStateReportV02

class AUTH_079_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgRptgTxStatRpt"]
		@property
		def SctiesFincgRptgTxStatRpt(self):
			return self._SctiesFincgRptgTxStatRpt

		@SctiesFincgRptgTxStatRpt.setter
		def SctiesFincgRptgTxStatRpt(self, value):
			self._SctiesFincgRptgTxStatRpt = value if type(value) != auto else self.make_default("SctiesFincgRptgTxStatRpt")

		@SctiesFincgRptgTxStatRpt.deleter
		def SctiesFincgRptgTxStatRpt(self):
			del self._SctiesFincgRptgTxStatRpt
			self._SctiesFincgRptgTxStatRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxStatRpt', type=SecuritiesFinancingReportingTransactionStateReportV02, min=1, max=1, mutex_group=None, array=False),
		))

