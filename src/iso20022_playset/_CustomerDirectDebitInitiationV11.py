from . import base_types
from ._GroupHeader118 import GroupHeader118
from ._PaymentInstruction45 import PaymentInstruction45
from ._SupplementaryData1 import SupplementaryData1

class CustomerDirectDebitInitiationV11(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_PmtInf", "_SplmtryData"]
	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != base_types.auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	@property
	def PmtInf(self):
		return self._PmtInf

	@PmtInf.setter
	def PmtInf(self, value):
		self._PmtInf = value if type(value) != base_types.auto else self.make_default("PmtInf")

	@PmtInf.deleter
	def PmtInf(self):
		del self._PmtInf
		self._PmtInf = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader118, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInf', type=PaymentInstruction45, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

