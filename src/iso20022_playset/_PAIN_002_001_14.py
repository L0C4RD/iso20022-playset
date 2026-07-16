# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerPaymentStatusReportV14

class PAIN_002_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pain.002.001.14"
		_docname = "pain.002.001.14"

		__slots__ = ["_CstmrPmtStsRpt"]
		@property
		def CstmrPmtStsRpt(self):
			return self._CstmrPmtStsRpt

		@CstmrPmtStsRpt.setter
		def CstmrPmtStsRpt(self, value):
			self._CstmrPmtStsRpt = value if value is not None else base_types.UninitialisedField(self, 'CstmrPmtStsRpt', CustomerPaymentStatusReportV14, False)

		@CstmrPmtStsRpt.deleter
		def CstmrPmtStsRpt(self):
			del self._CstmrPmtStsRpt
			self._CstmrPmtStsRpt = base_types.UninitialisedField(self, 'CstmrPmtStsRpt', CustomerPaymentStatusReportV14, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrPmtStsRpt', type=CustomerPaymentStatusReportV14, min=1, max=1, mutex_group=None, array=False),
		))