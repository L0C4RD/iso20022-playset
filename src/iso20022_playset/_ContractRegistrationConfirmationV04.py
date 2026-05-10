from . import base_types
from ._CurrencyControlHeader7 import CurrencyControlHeader7
from ._RegisteredContract20 import RegisteredContract20
from ._SupplementaryData1 import SupplementaryData1

class ContractRegistrationConfirmationV04(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_RegdCtrct", "_SplmtryData"]
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
	def RegdCtrct(self):
		return self._RegdCtrct

	@RegdCtrct.setter
	def RegdCtrct(self, value):
		self._RegdCtrct = value if type(value) != base_types.auto else self.make_default("RegdCtrct")

	@RegdCtrct.deleter
	def RegdCtrct(self):
		del self._RegdCtrct
		self._RegdCtrct = None

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
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdCtrct', type=RegisteredContract20, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

