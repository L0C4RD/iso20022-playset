# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorTransactionLogReportResponseV06 import AcceptorTransactionLogReportResponseV06

class CAAA_025_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrTxLgRptRspn"]
		@property
		def AccptrTxLgRptRspn(self):
			return self._AccptrTxLgRptRspn

		@AccptrTxLgRptRspn.setter
		def AccptrTxLgRptRspn(self, value):
			self._AccptrTxLgRptRspn = value if type(value) != base_types.auto else self.make_default("AccptrTxLgRptRspn")

		@AccptrTxLgRptRspn.deleter
		def AccptrTxLgRptRspn(self):
			del self._AccptrTxLgRptRspn
			self._AccptrTxLgRptRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrTxLgRptRspn', type=AcceptorTransactionLogReportResponseV06, min=1, max=1, mutex_group=None, array=False),
		))