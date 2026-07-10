# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingReusedCollateralDataTransactionStateReportV02 import SecuritiesFinancingReportingReusedCollateralDataTransactionStateReportV02

class AUTH_086_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.086.001.02"
		_docname = "auth.086.001.02"

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