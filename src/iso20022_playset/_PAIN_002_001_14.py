# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CustomerPaymentStatusReportV14 import CustomerPaymentStatusReportV14

class PAIN_002_001_14():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:pain.002.001.14"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_CstmrPmtStsRpt"]
		@property
		def CstmrPmtStsRpt(self):
			return self._CstmrPmtStsRpt

		@CstmrPmtStsRpt.setter
		def CstmrPmtStsRpt(self, value):
			self._CstmrPmtStsRpt = value if type(value) != base_types.auto else self.make_default("CstmrPmtStsRpt")

		@CstmrPmtStsRpt.deleter
		def CstmrPmtStsRpt(self):
			del self._CstmrPmtStsRpt
			self._CstmrPmtStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrPmtStsRpt', type=CustomerPaymentStatusReportV14, min=1, max=1, mutex_group=None, array=False),
		))