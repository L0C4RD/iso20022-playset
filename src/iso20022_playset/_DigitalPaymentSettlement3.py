from . import base_types
from ._DTI2024Identifier import DTI2024Identifier
from ._Quantity48Choice import Quantity48Choice
from ._SecurityIdentification50 import SecurityIdentification50

class DigitalPaymentSettlement3(base_types._BaseFieldType):

	__slots__ = ["_DgtlLdgrId", "_FinInstrmId", "_Qty"]
	@property
	def DgtlLdgrId(self):
		return self._DgtlLdgrId

	@DgtlLdgrId.setter
	def DgtlLdgrId(self, value):
		self._DgtlLdgrId = value if type(value) != base_types.auto else self.make_default("DgtlLdgrId")

	@DgtlLdgrId.deleter
	def DgtlLdgrId(self):
		del self._DgtlLdgrId
		self._DgtlLdgrId = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != base_types.auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlLdgrId', type=DTI2024Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification50, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity48Choice, min=1, max=1, mutex_group=None, array=False),
	))

