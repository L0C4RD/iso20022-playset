# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DTI2024Identifier
from . import Quantity48Choice
from . import SecurityIdentification50

class DigitalPaymentSettlement3(base_types._BaseFieldType):

	__slots__ = ["_DgtlLdgrId", "_FinInstrmId", "_Qty"]
	@property
	def DgtlLdgrId(self):
		return self._DgtlLdgrId

	@DgtlLdgrId.setter
	def DgtlLdgrId(self, value):
		self._DgtlLdgrId = value if value is not None else base_types.UninitialisedField(self, 'DgtlLdgrId', DTI2024Identifier, False)

	@DgtlLdgrId.deleter
	def DgtlLdgrId(self):
		del self._DgtlLdgrId
		self._DgtlLdgrId = base_types.UninitialisedField(self, 'DgtlLdgrId', DTI2024Identifier, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification50, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification50, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', Quantity48Choice, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', Quantity48Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlLdgrId', type=DTI2024Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification50, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity48Choice, min=1, max=1, mutex_group=None, array=False),
	))