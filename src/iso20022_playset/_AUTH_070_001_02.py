# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingTransactionMarginDataReportV02 import SecuritiesFinancingReportingTransactionMarginDataReportV02

class AUTH_070_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.070.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

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