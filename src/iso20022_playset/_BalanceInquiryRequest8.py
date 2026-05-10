from . import base_types
from .TransactionIdentifier1 import TransactionIdentifier1
from .PaymentAccountRequest1 import PaymentAccountRequest1
from .LoyaltyAccountRequest3 import LoyaltyAccountRequest3
from .StoredValueRequest8 import StoredValueRequest8

class BalanceInquiryRequest8(base_types._BaseFieldType):

	__slots__ = ["_SaleTxId", "_StordValAcctReq", "_LltyAcctReq", "_PmtAcctReq"]
	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if type(value) != base_types.auto else self.make_default("SaleTxId")

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = None

	@property
	def StordValAcctReq(self):
		return self._StordValAcctReq

	@StordValAcctReq.setter
	def StordValAcctReq(self, value):
		self._StordValAcctReq = value if type(value) != base_types.auto else self.make_default("StordValAcctReq")

	@StordValAcctReq.deleter
	def StordValAcctReq(self):
		del self._StordValAcctReq
		self._StordValAcctReq = None

	@property
	def LltyAcctReq(self):
		return self._LltyAcctReq

	@LltyAcctReq.setter
	def LltyAcctReq(self, value):
		self._LltyAcctReq = value if type(value) != base_types.auto else self.make_default("LltyAcctReq")

	@LltyAcctReq.deleter
	def LltyAcctReq(self):
		del self._LltyAcctReq
		self._LltyAcctReq = None

	@property
	def PmtAcctReq(self):
		return self._PmtAcctReq

	@PmtAcctReq.setter
	def PmtAcctReq(self, value):
		self._PmtAcctReq = value if type(value) != base_types.auto else self.make_default("PmtAcctReq")

	@PmtAcctReq.deleter
	def PmtAcctReq(self):
		del self._PmtAcctReq
		self._PmtAcctReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StordValAcctReq', type=StoredValueRequest8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyAcctReq', type=LoyaltyAccountRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcctReq', type=PaymentAccountRequest1, min=0, max=1, mutex_group=None, array=False),
	))

