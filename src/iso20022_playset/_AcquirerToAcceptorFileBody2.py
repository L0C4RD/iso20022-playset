from . import base_types
from ._AcceptorCompletionAdviceResponse13 import AcceptorCompletionAdviceResponse13
from ._AcceptorCancellationAdviceResponse13 import AcceptorCancellationAdviceResponse13
from ._CardPaymentBatchTransferResponse12 import CardPaymentBatchTransferResponse12

class AcquirerToAcceptorFileBody2(base_types._BaseFieldType):

	__slots__ = ["_CxlRspn", "_BtchTrfRspn", "_CmpltnAdvcRspn"]
	@property
	def CxlRspn(self):
		return self._CxlRspn

	@CxlRspn.setter
	def CxlRspn(self, value):
		self._CxlRspn = value if type(value) != base_types.auto else self.make_default("CxlRspn")

	@CxlRspn.deleter
	def CxlRspn(self):
		del self._CxlRspn
		self._CxlRspn = None

	@property
	def BtchTrfRspn(self):
		return self._BtchTrfRspn

	@BtchTrfRspn.setter
	def BtchTrfRspn(self, value):
		self._BtchTrfRspn = value if type(value) != base_types.auto else self.make_default("BtchTrfRspn")

	@BtchTrfRspn.deleter
	def BtchTrfRspn(self):
		del self._BtchTrfRspn
		self._BtchTrfRspn = None

	@property
	def CmpltnAdvcRspn(self):
		return self._CmpltnAdvcRspn

	@CmpltnAdvcRspn.setter
	def CmpltnAdvcRspn(self, value):
		self._CmpltnAdvcRspn = value if type(value) != base_types.auto else self.make_default("CmpltnAdvcRspn")

	@CmpltnAdvcRspn.deleter
	def CmpltnAdvcRspn(self):
		del self._CmpltnAdvcRspn
		self._CmpltnAdvcRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRspn', type=AcceptorCancellationAdviceResponse13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchTrfRspn', type=CardPaymentBatchTransferResponse12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmpltnAdvcRspn', type=AcceptorCompletionAdviceResponse13, min=0, max=1, mutex_group=None, array=False),
	))

