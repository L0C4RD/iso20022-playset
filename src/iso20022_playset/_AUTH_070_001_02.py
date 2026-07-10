# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingTransactionMarginDataReportV02 import SecuritiesFinancingReportingTransactionMarginDataReportV02

class AUTH_070_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.070.001.02"
		_docname = "auth.070.001.02"

		__slots__ = ["_SctiesFincgRptgTxMrgnDataRpt"]
		@property
		def SctiesFincgRptgTxMrgnDataRpt(self):
			return self._SctiesFincgRptgTxMrgnDataRpt

		@SctiesFincgRptgTxMrgnDataRpt.setter
		def SctiesFincgRptgTxMrgnDataRpt(self, value):
			self._SctiesFincgRptgTxMrgnDataRpt = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgTxMrgnDataRpt")

		@SctiesFincgRptgTxMrgnDataRpt.deleter
		def SctiesFincgRptgTxMrgnDataRpt(self):
			del self._SctiesFincgRptgTxMrgnDataRpt
			self._SctiesFincgRptgTxMrgnDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxMrgnDataRpt', type=SecuritiesFinancingReportingTransactionMarginDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))