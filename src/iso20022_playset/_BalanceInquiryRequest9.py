from . import base_types
from ._LoyaltyAccountRequest3 import LoyaltyAccountRequest3
from ._PaymentAccountRequest1 import PaymentAccountRequest1
from ._StoredValueRequest9 import StoredValueRequest9
from ._TransactionIdentifier1 import TransactionIdentifier1

class BalanceInquiryRequest9(base_types._BaseFieldType):

	__slots__ = ["_LltyAcctReq", "_PmtAcctReq", "_SaleTxId", "_StordValAcctReq"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyAcctReq', type=LoyaltyAccountRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcctReq', type=PaymentAccountRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StordValAcctReq', type=StoredValueRequest9, min=0, max=1, mutex_group=None, array=False),
	))

