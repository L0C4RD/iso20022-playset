from . import base_types
from .AcceptorTransactionLogReportRequestV05 import AcceptorTransactionLogReportRequestV05

class CAAA_024_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrTxLgRptReq"]
		@property
		def AccptrTxLgRptReq(self):
			return self._AccptrTxLgRptReq

		@AccptrTxLgRptReq.setter
		def AccptrTxLgRptReq(self, value):
			self._AccptrTxLgRptReq = value if type(value) != auto else self.make_default("AccptrTxLgRptReq")

		@AccptrTxLgRptReq.deleter
		def AccptrTxLgRptReq(self):
			del self._AccptrTxLgRptReq
			self._AccptrTxLgRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrTxLgRptReq', type=AcceptorTransactionLogReportRequestV05, min=1, max=1, mutex_group=None, array=False),
		))

