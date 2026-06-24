# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingTransactionReportV02 import SecuritiesFinancingReportingTransactionReportV02

class AUTH_052_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.052.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_SctiesFincgRptgTxRpt"]
		@property
		def SctiesFincgRptgTxRpt(self):
			return self._SctiesFincgRptgTxRpt

		@SctiesFincgRptgTxRpt.setter
		def SctiesFincgRptgTxRpt(self, value):
			self._SctiesFincgRptgTxRpt = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgTxRpt")

		@SctiesFincgRptgTxRpt.deleter
		def SctiesFincgRptgTxRpt(self):
			del self._SctiesFincgRptgTxRpt
			self._SctiesFincgRptgTxRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxRpt', type=SecuritiesFinancingReportingTransactionReportV02, min=1, max=1, mutex_group=None, array=False),
		))