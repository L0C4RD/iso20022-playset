from . import base_types
from ._ActivationHeader3 import ActivationHeader3
from ._SupplementaryData1 import SupplementaryData1
from ._DebtorActivation5 import DebtorActivation5
from ._ElectronicInvoice1 import ElectronicInvoice1

class RequestToPayDebtorActivationRequestV02(base_types._BaseFieldType):

	__slots__ = ["_ElctrncInvcData", "_SplmtryData", "_DbtrActvtn", "_Hdr"]
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

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

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
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != base_types.auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElctrncInvcData', type=ElectronicInvoice1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DbtrActvtn', type=DebtorActivation5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hdr', type=ActivationHeader3, min=1, max=1, mutex_group=None, array=False),
	))

