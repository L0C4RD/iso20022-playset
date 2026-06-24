# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesFinancingReportingTransactionStatusAdviceV02 import SecuritiesFinancingReportingTransactionStatusAdviceV02

class AUTH_084_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.084.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SctiesFincgRptgTxStsAdvc"]
		@property
		def SctiesFincgRptgTxStsAdvc(self):
			return self._SctiesFincgRptgTxStsAdvc

		@SctiesFincgRptgTxStsAdvc.setter
		def SctiesFincgRptgTxStsAdvc(self, value):
			self._SctiesFincgRptgTxStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgTxStsAdvc")

		@SctiesFincgRptgTxStsAdvc.deleter
		def SctiesFincgRptgTxStsAdvc(self):
			del self._SctiesFincgRptgTxStsAdvc
			self._SctiesFincgRptgTxStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxStsAdvc', type=SecuritiesFinancingReportingTransactionStatusAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))