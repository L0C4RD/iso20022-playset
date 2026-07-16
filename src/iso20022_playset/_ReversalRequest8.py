# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerOrder1
from . import ImpliedCurrencyAndAmount
from . import LoyaltyRequestData3
from . import PaymentTransaction183
from . import ReversalReason1Code

class ReversalRequest8(base_types._BaseFieldType):

	__slots__ = ["_CstmrOrdr", "_LltyData", "_RvsdAmt", "_RvslRsn", "_RvslTx"]
	@property
	def CstmrOrdr(self):
		return self._CstmrOrdr

	@CstmrOrdr.setter
	def CstmrOrdr(self, value):
		self._CstmrOrdr = value if value is not None else base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, False)

	@CstmrOrdr.deleter
	def CstmrOrdr(self):
		del self._CstmrOrdr
		self._CstmrOrdr = base_types.UninitialisedField(self, 'CstmrOrdr', CustomerOrder1, False)

	@property
	def LltyData(self):
		return self._LltyData

	@LltyData.setter
	def LltyData(self, value):
		self._LltyData = value if value is not None else base_types.UninitialisedField(self, 'LltyData', LoyaltyRequestData3, True)

	@LltyData.deleter
	def LltyData(self):
		del self._LltyData
		self._LltyData = base_types.UninitialisedField(self, 'LltyData', LoyaltyRequestData3, True)

	@property
	def RvsdAmt(self):
		return self._RvsdAmt

	@RvsdAmt.setter
	def RvsdAmt(self, value):
		self._RvsdAmt = value if value is not None else base_types.UninitialisedField(self, 'RvsdAmt', ImpliedCurrencyAndAmount, False)

	@RvsdAmt.deleter
	def RvsdAmt(self):
		del self._RvsdAmt
		self._RvsdAmt = base_types.UninitialisedField(self, 'RvsdAmt', ImpliedCurrencyAndAmount, False)

	@property
	def RvslRsn(self):
		return self._RvslRsn

	@RvslRsn.setter
	def RvslRsn(self, value):
		self._RvslRsn = value if value is not None else base_types.UninitialisedField(self, 'RvslRsn', ReversalReason1Code, False)

	@RvslRsn.deleter
	def RvslRsn(self):
		del self._RvslRsn
		self._RvslRsn = base_types.UninitialisedField(self, 'RvslRsn', ReversalReason1Code, False)

	@property
	def RvslTx(self):
		return self._RvslTx

	@RvslTx.setter
	def RvslTx(self, value):
		self._RvslTx = value if value is not None else base_types.UninitialisedField(self, 'RvslTx', PaymentTransaction183, False)

	@RvslTx.deleter
	def RvslTx(self):
		del self._RvslTx
		self._RvslTx = base_types.UninitialisedField(self, 'RvslTx', PaymentTransaction183, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrOrdr', type=CustomerOrder1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyData', type=LoyaltyRequestData3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RvsdAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslRsn', type=ReversalReason1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslTx', type=PaymentTransaction183, min=0, max=1, mutex_group=None, array=False),
	))