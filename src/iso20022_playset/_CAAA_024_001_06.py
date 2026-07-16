# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorTransactionLogReportRequestV06

class CAAA_024_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.024.001.06"
		_docname = "caaa.024.001.06"

		__slots__ = ["_AccptrTxLgRptReq"]
		@property
		def AccptrTxLgRptReq(self):
			return self._AccptrTxLgRptReq

		@AccptrTxLgRptReq.setter
		def AccptrTxLgRptReq(self, value):
			self._AccptrTxLgRptReq = value if value is not None else base_types.UninitialisedField(self, 'AccptrTxLgRptReq', AcceptorTransactionLogReportRequestV06, False)

		@AccptrTxLgRptReq.deleter
		def AccptrTxLgRptReq(self):
			del self._AccptrTxLgRptReq
			self._AccptrTxLgRptReq = base_types.UninitialisedField(self, 'AccptrTxLgRptReq', AcceptorTransactionLogReportRequestV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrTxLgRptReq', type=AcceptorTransactionLogReportRequestV06, min=1, max=1, mutex_group=None, array=False),
		))