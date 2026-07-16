# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LoyaltyAccountRequest3
from . import PaymentAccountRequest1
from . import StoredValueRequest9
from . import TransactionIdentifier1

class BalanceInquiryRequest9(base_types._BaseFieldType):

	__slots__ = ["_LltyAcctReq", "_PmtAcctReq", "_SaleTxId", "_StordValAcctReq"]
	@property
	def LltyAcctReq(self):
		return self._LltyAcctReq

	@LltyAcctReq.setter
	def LltyAcctReq(self, value):
		self._LltyAcctReq = value if value is not None else base_types.UninitialisedField(self, 'LltyAcctReq', LoyaltyAccountRequest3, False)

	@LltyAcctReq.deleter
	def LltyAcctReq(self):
		del self._LltyAcctReq
		self._LltyAcctReq = base_types.UninitialisedField(self, 'LltyAcctReq', LoyaltyAccountRequest3, False)

	@property
	def PmtAcctReq(self):
		return self._PmtAcctReq

	@PmtAcctReq.setter
	def PmtAcctReq(self, value):
		self._PmtAcctReq = value if value is not None else base_types.UninitialisedField(self, 'PmtAcctReq', PaymentAccountRequest1, False)

	@PmtAcctReq.deleter
	def PmtAcctReq(self):
		del self._PmtAcctReq
		self._PmtAcctReq = base_types.UninitialisedField(self, 'PmtAcctReq', PaymentAccountRequest1, False)

	@property
	def SaleTxId(self):
		return self._SaleTxId

	@SaleTxId.setter
	def SaleTxId(self, value):
		self._SaleTxId = value if value is not None else base_types.UninitialisedField(self, 'SaleTxId', TransactionIdentifier1, False)

	@SaleTxId.deleter
	def SaleTxId(self):
		del self._SaleTxId
		self._SaleTxId = base_types.UninitialisedField(self, 'SaleTxId', TransactionIdentifier1, False)

	@property
	def StordValAcctReq(self):
		return self._StordValAcctReq

	@StordValAcctReq.setter
	def StordValAcctReq(self, value):
		self._StordValAcctReq = value if value is not None else base_types.UninitialisedField(self, 'StordValAcctReq', StoredValueRequest9, False)

	@StordValAcctReq.deleter
	def StordValAcctReq(self):
		del self._StordValAcctReq
		self._StordValAcctReq = base_types.UninitialisedField(self, 'StordValAcctReq', StoredValueRequest9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyAcctReq', type=LoyaltyAccountRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtAcctReq', type=PaymentAccountRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleTxId', type=TransactionIdentifier1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StordValAcctReq', type=StoredValueRequest9, min=0, max=1, mutex_group=None, array=False),
	))