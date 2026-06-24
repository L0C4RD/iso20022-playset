# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TransactionReportRequestV03 import TransactionReportRequestV03

class TSMT_042_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_TxRptReq"]
		@property
		def TxRptReq(self):
			return self._TxRptReq

		@TxRptReq.setter
		def TxRptReq(self, value):
			self._TxRptReq = value if type(value) != base_types.auto else self.make_default("TxRptReq")

		@TxRptReq.deleter
		def TxRptReq(self):
			del self._TxRptReq
			self._TxRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxRptReq', type=TransactionReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))