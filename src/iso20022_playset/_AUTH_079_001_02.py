# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingTransactionStateReportV02 import SecuritiesFinancingReportingTransactionStateReportV02

class AUTH_079_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.079.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctiesFincgRptgTxStatRpt"]
		@property
		def SctiesFincgRptgTxStatRpt(self):
			return self._SctiesFincgRptgTxStatRpt

		@SctiesFincgRptgTxStatRpt.setter
		def SctiesFincgRptgTxStatRpt(self, value):
			self._SctiesFincgRptgTxStatRpt = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgTxStatRpt")

		@SctiesFincgRptgTxStatRpt.deleter
		def SctiesFincgRptgTxStatRpt(self):
			del self._SctiesFincgRptgTxStatRpt
			self._SctiesFincgRptgTxStatRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxStatRpt', type=SecuritiesFinancingReportingTransactionStateReportV02, min=1, max=1, mutex_group=None, array=False),
		))