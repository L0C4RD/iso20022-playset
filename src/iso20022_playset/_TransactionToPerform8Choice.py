# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LoyaltyRequest8
from . import PaymentRequest8
from . import ReversalRequest8

class TransactionToPerform8Choice(base_types._BaseFieldType):

	__slots__ = ["_LltyReq", "_PmtReq", "_RvslReq"]
	@property
	def LltyReq(self):
		return self._LltyReq

	@LltyReq.setter
	def LltyReq(self, value):
		self._LltyReq = value if value is not None else base_types.UninitialisedField(self, 'LltyReq', LoyaltyRequest8, False)

	@LltyReq.deleter
	def LltyReq(self):
		del self._LltyReq
		self._LltyReq = base_types.UninitialisedField(self, 'LltyReq', LoyaltyRequest8, False)

	@property
	def PmtReq(self):
		return self._PmtReq

	@PmtReq.setter
	def PmtReq(self, value):
		self._PmtReq = value if value is not None else base_types.UninitialisedField(self, 'PmtReq', PaymentRequest8, False)

	@PmtReq.deleter
	def PmtReq(self):
		del self._PmtReq
		self._PmtReq = base_types.UninitialisedField(self, 'PmtReq', PaymentRequest8, False)

	@property
	def RvslReq(self):
		return self._RvslReq

	@RvslReq.setter
	def RvslReq(self, value):
		self._RvslReq = value if value is not None else base_types.UninitialisedField(self, 'RvslReq', ReversalRequest8, False)

	@RvslReq.deleter
	def RvslReq(self):
		del self._RvslReq
		self._RvslReq = base_types.UninitialisedField(self, 'RvslReq', ReversalRequest8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyReq', type=LoyaltyRequest8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtReq', type=PaymentRequest8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RvslReq', type=ReversalRequest8, min=0, max=1, mutex_group=1, array=False),
	))