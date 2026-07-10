# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingTransactionReusedCollateralDataReportV02 import SecuritiesFinancingReportingTransactionReusedCollateralDataReportV02

class AUTH_071_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.071.001.02"
		_docname = "auth.071.001.02"

		__slots__ = ["_SctiesFincgRptgTxReusdCollDataRpt"]
		@property
		def SctiesFincgRptgTxReusdCollDataRpt(self):
			return self._SctiesFincgRptgTxReusdCollDataRpt

		@SctiesFincgRptgTxReusdCollDataRpt.setter
		def SctiesFincgRptgTxReusdCollDataRpt(self, value):
			self._SctiesFincgRptgTxReusdCollDataRpt = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgTxReusdCollDataRpt")

		@SctiesFincgRptgTxReusdCollDataRpt.deleter
		def SctiesFincgRptgTxReusdCollDataRpt(self):
			del self._SctiesFincgRptgTxReusdCollDataRpt
			self._SctiesFincgRptgTxReusdCollDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxReusdCollDataRpt', type=SecuritiesFinancingReportingTransactionReusedCollateralDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))