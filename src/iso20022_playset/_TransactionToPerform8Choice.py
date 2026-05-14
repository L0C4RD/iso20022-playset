# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LoyaltyRequest8 import LoyaltyRequest8
from ._PaymentRequest8 import PaymentRequest8
from ._ReversalRequest8 import ReversalRequest8

class TransactionToPerform8Choice(base_types._BaseFieldType):

	__slots__ = ["_LltyReq", "_PmtReq", "_RvslReq"]
	@property
	def LltyReq(self):
		return self._LltyReq

	@LltyReq.setter
	def LltyReq(self, value):
		self._LltyReq = value if type(value) != base_types.auto else self.make_default("LltyReq")

	@LltyReq.deleter
	def LltyReq(self):
		del self._LltyReq
		self._LltyReq = None

	@property
	def PmtReq(self):
		return self._PmtReq

	@PmtReq.setter
	def PmtReq(self, value):
		self._PmtReq = value if type(value) != base_types.auto else self.make_default("PmtReq")

	@PmtReq.deleter
	def PmtReq(self):
		del self._PmtReq
		self._PmtReq = None

	@property
	def RvslReq(self):
		return self._RvslReq

	@RvslReq.setter
	def RvslReq(self, value):
		self._RvslReq = value if type(value) != base_types.auto else self.make_default("RvslReq")

	@RvslReq.deleter
	def RvslReq(self):
		del self._RvslReq
		self._RvslReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyReq', type=LoyaltyRequest8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtReq', type=PaymentRequest8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RvslReq', type=ReversalRequest8, min=0, max=1, mutex_group=1, array=False),
	))