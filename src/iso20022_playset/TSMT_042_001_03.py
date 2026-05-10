from . import base_types
import TransactionReportRequestV03

class TSMT_042_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_TxRptReq"]
		@property
		def TxRptReq(self):
			return self._TxRptReq

		@TxRptReq.setter
		def TxRptReq(self, value):
			self._TxRptReq = value if type(value) != auto else self.make_default("TxRptReq")

		@TxRptReq.deleter
		def TxRptReq(self):
			del self._TxRptReq
			self._TxRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TxRptReq', type=TransactionReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))

