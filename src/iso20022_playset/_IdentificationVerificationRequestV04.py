from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .IdentificationVerification5 import IdentificationVerification5
from .IdentificationAssignment4 import IdentificationAssignment4

class IdentificationVerificationRequestV04(base_types._BaseFieldType):

	__slots__ = ["_Assgnmt", "_SplmtryData", "_Vrfctn"]
	@property
	def Assgnmt(self):
		return self._Assgnmt

	@Assgnmt.setter
	def Assgnmt(self, value):
		self._Assgnmt = value if type(value) != base_types.auto else self.make_default("Assgnmt")

	@Assgnmt.deleter
	def Assgnmt(self):
		del self._Assgnmt
		self._Assgnmt = None

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
	def Vrfctn(self):
		return self._Vrfctn

	@Vrfctn.setter
	def Vrfctn(self, value):
		self._Vrfctn = value if type(value) != base_types.auto else self.make_default("Vrfctn")

	@Vrfctn.deleter
	def Vrfctn(self):
		del self._Vrfctn
		self._Vrfctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgnmt', type=IdentificationAssignment4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrfctn', type=IdentificationVerification5, min=1, max=None, mutex_group=None, array=True),
	))

