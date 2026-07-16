# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorTransactionLogReportResponseV06

class CAAA_025_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.025.001.06"
		_docname = "caaa.025.001.06"

		__slots__ = ["_AccptrTxLgRptRspn"]
		@property
		def AccptrTxLgRptRspn(self):
			return self._AccptrTxLgRptRspn

		@AccptrTxLgRptRspn.setter
		def AccptrTxLgRptRspn(self, value):
			self._AccptrTxLgRptRspn = value if value is not None else base_types.UninitialisedField(self, 'AccptrTxLgRptRspn', AcceptorTransactionLogReportResponseV06, False)

		@AccptrTxLgRptRspn.deleter
		def AccptrTxLgRptRspn(self):
			del self._AccptrTxLgRptRspn
			self._AccptrTxLgRptRspn = base_types.UninitialisedField(self, 'AccptrTxLgRptRspn', AcceptorTransactionLogReportResponseV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrTxLgRptRspn', type=AcceptorTransactionLogReportResponseV06, min=1, max=1, mutex_group=None, array=False),
		))