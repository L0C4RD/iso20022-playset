from . import base_types
from ._CustomerPaymentCancellationRequestV13 import CustomerPaymentCancellationRequestV13

class CAMT_055_001_13():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CstmrPmtCxlReq"]
		@property
		def CstmrPmtCxlReq(self):
			return self._CstmrPmtCxlReq

		@CstmrPmtCxlReq.setter
		def CstmrPmtCxlReq(self, value):
			self._CstmrPmtCxlReq = value if type(value) != base_types.auto else self.make_default("CstmrPmtCxlReq")

		@CstmrPmtCxlReq.deleter
		def CstmrPmtCxlReq(self):
			del self._CstmrPmtCxlReq
			self._CstmrPmtCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrPmtCxlReq', type=CustomerPaymentCancellationRequestV13, min=1, max=1, mutex_group=None, array=False),
		))

