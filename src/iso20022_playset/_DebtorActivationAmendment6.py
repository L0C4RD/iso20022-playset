from . import base_types
from ._ElectronicInvoice1 import ElectronicInvoice1
from ._DebtorActivation6 import DebtorActivation6

class DebtorActivationAmendment6(base_types._BaseFieldType):

	__slots__ = ["_ElctrncInvcData", "_DbtrActvtn"]
	@property
	def DbtrActvtn(self):
		return self._DbtrActvtn

	@DbtrActvtn.setter
	def DbtrActvtn(self, value):
		self._DbtrActvtn = value if type(value) != base_types.auto else self.make_default("DbtrActvtn")

	@DbtrActvtn.deleter
	def DbtrActvtn(self):
		del self._DbtrActvtn
		self._DbtrActvtn = None

	@property
	def ElctrncInvcData(self):
		return self._ElctrncInvcData

	@ElctrncInvcData.setter
	def ElctrncInvcData(self, value):
		self._ElctrncInvcData = value if type(value) != base_types.auto else self.make_default("ElctrncInvcData")

	@ElctrncInvcData.deleter
	def ElctrncInvcData(self):
		del self._ElctrncInvcData
		self._ElctrncInvcData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DbtrActvtn', type=DebtorActivation6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncInvcData', type=ElectronicInvoice1, min=0, max=1, mutex_group=None, array=False),
	))

