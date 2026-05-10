from . import base_types
from .DebtorActivationAmendment5 import DebtorActivationAmendment5
from .SupplementaryData1 import SupplementaryData1
from .ActivationHeader3 import ActivationHeader3

class RequestToPayDebtorActivationAmendmentRequestV02(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_AmdmntData", "_SplmtryData"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def AmdmntData(self):
		return self._AmdmntData

	@AmdmntData.setter
	def AmdmntData(self, value):
		self._AmdmntData = value if type(value) != auto else self.make_default("AmdmntData")

	@AmdmntData.deleter
	def AmdmntData(self):
		del self._AmdmntData
		self._AmdmntData = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=ActivationHeader3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntData', type=DebtorActivationAmendment5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

