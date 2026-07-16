# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LoyaltyRequestData3
from . import PaymentTransaction165

class PaymentRequest7(base_types._BaseFieldType):

	__slots__ = ["_LltyData", "_PmtTx"]
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
	def PmtTx(self):
		return self._PmtTx

	@PmtTx.setter
	def PmtTx(self, value):
		self._PmtTx = value if value is not None else base_types.UninitialisedField(self, 'PmtTx', PaymentTransaction165, False)

	@PmtTx.deleter
	def PmtTx(self):
		del self._PmtTx
		self._PmtTx = base_types.UninitialisedField(self, 'PmtTx', PaymentTransaction165, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LltyData', type=LoyaltyRequestData3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtTx', type=PaymentTransaction165, min=0, max=1, mutex_group=None, array=False),
	))