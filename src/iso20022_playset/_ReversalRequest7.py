from . import base_types
from .CustomerOrder1 import CustomerOrder1
from .LoyaltyRequestData3 import LoyaltyRequestData3
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .PaymentTransaction165 import PaymentTransaction165
from .ReversalReason1Code import ReversalReason1Code

class ReversalRequest7(base_types._BaseFieldType):

	__slots__ = ["_RvsdAmt", "_CstmrOrdr", "_LltyData", "_RvslTx", "_RvslRsn"]
	@property
	def RvsdAmt(self):
		return self._RvsdAmt

	@RvsdAmt.setter
	def RvsdAmt(self, value):
		self._RvsdAmt = value if type(value) != base_types.auto else self.make_default("RvsdAmt")

	@RvsdAmt.deleter
	def RvsdAmt(self):
		del self._RvsdAmt
		self._RvsdAmt = None

	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if type(value) != base_types.auto else self.make_default("CstmrOrdr")

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = None

	@property
	def LltyData(self):
		return self._LltyData

	@LltyData.setter
	def LltyData(self, value):
		self._LltyData = value if type(value) != base_types.auto else self.make_default("LltyData")

	@LltyData.deleter
	def LltyData(self):
		del self._LltyData
		self._LltyData = None

	@property
	def RvslTx(self):
		return self._RvslTx

	@RvslTx.setter
	def RvslTx(self, value):
		self._RvslTx = value if type(value) != base_types.auto else self.make_default("RvslTx")

	@RvslTx.deleter
	def RvslTx(self):
		del self._RvslTx
		self._RvslTx = None

	@property
	def RvslRsn(self):
		return self._RvslRsn

	@RvslRsn.setter
	def RvslRsn(self, value):
		self._RvslRsn = value if type(value) != base_types.auto else self.make_default("RvslRsn")

	@RvslRsn.deleter
	def RvslRsn(self):
		del self._RvslRsn
		self._RvslRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RvsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyData', type=LoyaltyRequestData3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RvslTx', type=PaymentTransaction165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslRsn', type=ReversalReason1Code, min=1, max=1, mutex_group=None, array=False),
	))

