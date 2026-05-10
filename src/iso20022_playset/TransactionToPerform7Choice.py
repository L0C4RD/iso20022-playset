import base_types
import PaymentRequest7
import LoyaltyRequest7
import ReversalRequest7

class TransactionToPerform7Choice(base_types._BaseFieldType):

	__slots__ = ["_RvslReq", "_PmtReq", "_LltyReq"]
	@property
	def RvslReq(self):
		return self._RvslReq

	@RvslReq.setter
	def RvslReq(self, value):
		self._RvslReq = value if type(value) != auto else self.make_default("RvslReq")

	@RvslReq.deleter
	def RvslReq(self):
		del self._RvslReq
		self._RvslReq = None

	@property
	def PmtReq(self):
		return self._PmtReq

	@PmtReq.setter
	def PmtReq(self, value):
		self._PmtReq = value if type(value) != auto else self.make_default("PmtReq")

	@PmtReq.deleter
	def PmtReq(self):
		del self._PmtReq
		self._PmtReq = None

	@property
	def LltyReq(self):
		return self._LltyReq

	@LltyReq.setter
	def LltyReq(self, value):
		self._LltyReq = value if type(value) != auto else self.make_default("LltyReq")

	@LltyReq.deleter
	def LltyReq(self):
		del self._LltyReq
		self._LltyReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RvslReq', type=ReversalRequest7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtReq', type=PaymentRequest7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LltyReq', type=LoyaltyRequest7, min=0, max=1, mutex_group=1, array=False),
	))

