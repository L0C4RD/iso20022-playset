import base_types
import SecuritiesFinancingReportingTransactionReusedCollateralDataReportV02

class AUTH_071_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgRptgTxReusdCollDataRpt"]
		@property
		def SctiesFincgRptgTxReusdCollDataRpt(self):
			return self._SctiesFincgRptgTxReusdCollDataRpt

		@SctiesFincgRptgTxReusdCollDataRpt.setter
		def SctiesFincgRptgTxReusdCollDataRpt(self, value):
			self._SctiesFincgRptgTxReusdCollDataRpt = value if type(value) != auto else self.make_default("SctiesFincgRptgTxReusdCollDataRpt")

		@SctiesFincgRptgTxReusdCollDataRpt.deleter
		def SctiesFincgRptgTxReusdCollDataRpt(self):
			del self._SctiesFincgRptgTxReusdCollDataRpt
			self._SctiesFincgRptgTxReusdCollDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxReusdCollDataRpt', type=SecuritiesFinancingReportingTransactionReusedCollateralDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))

