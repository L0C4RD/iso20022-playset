import base_types
import AcceptorTransactionLogReportResponseV05

class CAAA_025_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrTxLgRptRspn"]
		@property
		def AccptrTxLgRptRspn(self):
			return self._AccptrTxLgRptRspn

		@AccptrTxLgRptRspn.setter
		def AccptrTxLgRptRspn(self, value):
			self._AccptrTxLgRptRspn = value if type(value) != auto else self.make_default("AccptrTxLgRptRspn")

		@AccptrTxLgRptRspn.deleter
		def AccptrTxLgRptRspn(self):
			del self._AccptrTxLgRptRspn
			self._AccptrTxLgRptRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrTxLgRptRspn', type=AcceptorTransactionLogReportResponseV05, min=1, max=1, mutex_group=None, array=False),
		))

