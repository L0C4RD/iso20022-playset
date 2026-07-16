# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LoyaltyRequest7
from . import PaymentRequest7
from . import ReversalRequest7

class TransactionToPerform7Choice(base_types._BaseFieldType):

	__slots__ = ["_LltyReq", "_PmtReq", "_RvslReq"]
	@property
	def LltyReq(self):
		return self._LltyReq

	@LltyReq.setter
	def LltyReq(self, value):
		self._LltyReq = value if value is not None else base_types.UninitialisedField(self, 'LltyReq', LoyaltyRequest7, False)

	@LltyReq.deleter
	def LltyReq(self):
		del self._LltyReq
		self._LltyReq = base_types.UninitialisedField(self, 'LltyReq', LoyaltyRequest7, False)

	@property
	def PmtReq(self):
		return self._PmtReq

	@PmtReq.setter
	def PmtReq(self, value):
		self._PmtReq = value if value is not None else base_types.UninitialisedField(self, 'PmtReq', PaymentRequest7, False)

	@PmtReq.deleter
	def PmtReq(self):
		del self._PmtReq
		self._PmtReq = base_types.UninitialisedField(self, 'PmtReq', PaymentRequest7, False)

	@property
	def RvslReq(self):
		return self._RvslReq

	@RvslReq.setter
	def RvslReq(self, value):
		self._RvslReq = value if value is not None else base_types.UninitialisedField(self, 'RvslReq', ReversalRequest7, False)

	@RvslReq.deleter
	def RvslReq(self):
		del self._RvslReq
		self._RvslReq = base_types.UninitialisedField(self, 'RvslReq', ReversalRequest7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyReq', type=LoyaltyRequest7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtReq', type=PaymentRequest7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RvslReq', type=ReversalRequest7, min=0, max=1, mutex_group=1, array=False),
	))