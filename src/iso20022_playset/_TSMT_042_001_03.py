# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TransactionReportRequestV03

class TSMT_042_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.042.001.03"
		_docname = "tsmt.042.001.03"

		__slots__ = ["_TxRptReq"]
		@property
		def TxRptReq(self):
			return self._TxRptReq

		@TxRptReq.setter
		def TxRptReq(self, value):
			self._TxRptReq = value if value is not None else base_types.UninitialisedField(self, 'TxRptReq', TransactionReportRequestV03, False)

		@TxRptReq.deleter
		def TxRptReq(self):
			del self._TxRptReq
			self._TxRptReq = base_types.UninitialisedField(self, 'TxRptReq', TransactionReportRequestV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxRptReq', type=TransactionReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))