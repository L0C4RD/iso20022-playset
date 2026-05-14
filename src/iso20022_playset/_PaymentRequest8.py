# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LoyaltyRequestData3 import LoyaltyRequestData3
from ._PaymentTransaction183 import PaymentTransaction183

class PaymentRequest8(base_types._BaseFieldType):

	__slots__ = ["_LltyData", "_PmtTx"]
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
	def PmtTx(self):
		return self._PmtTx

	@PmtTx.setter
	def PmtTx(self, value):
		self._PmtTx = value if type(value) != base_types.auto else self.make_default("PmtTx")

	@PmtTx.deleter
	def PmtTx(self):
		del self._PmtTx
		self._PmtTx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyData', type=LoyaltyRequestData3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtTx', type=PaymentTransaction183, min=0, max=1, mutex_group=None, array=False),
	))