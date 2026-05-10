from . import base_types
from .SecuritiesFinancingReportingReusedCollateralDataTransactionStateReportV02 import SecuritiesFinancingReportingReusedCollateralDataTransactionStateReportV02

class AUTH_086_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgRptgReusdCollDataTxStatRpt"]
		@property
		def SctiesFincgRptgReusdCollDataTxStatRpt(self):
			return self._SctiesFincgRptgReusdCollDataTxStatRpt

		@SctiesFincgRptgReusdCollDataTxStatRpt.setter
		def SctiesFincgRptgReusdCollDataTxStatRpt(self, value):
			self._SctiesFincgRptgReusdCollDataTxStatRpt = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgReusdCollDataTxStatRpt")

		@SctiesFincgRptgReusdCollDataTxStatRpt.deleter
		def SctiesFincgRptgReusdCollDataTxStatRpt(self):
			del self._SctiesFincgRptgReusdCollDataTxStatRpt
			self._SctiesFincgRptgReusdCollDataTxStatRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgReusdCollDataTxStatRpt', type=SecuritiesFinancingReportingReusedCollateralDataTransactionStateReportV02, min=1, max=1, mutex_group=None, array=False),
		))

