from . import base_types
from .ContractRegistration7 import ContractRegistration7
from .SupplementaryData1 import SupplementaryData1
from .CurrencyControlHeader8 import CurrencyControlHeader8

class ContractRegistrationRequestV04(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_CtrctRegn", "_GrpHdr"]
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

	@property
	def CtrctRegn(self):
		return self._CtrctRegn

	@CtrctRegn.setter
	def CtrctRegn(self, value):
		self._CtrctRegn = value if type(value) != auto else self.make_default("CtrctRegn")

	@CtrctRegn.deleter
	def CtrctRegn(self):
		del self._CtrctRegn
		self._CtrctRegn = None

	@property
	def GrpHdr(self):
		return self._GrpHdr

	@GrpHdr.setter
	def GrpHdr(self, value):
		self._GrpHdr = value if type(value) != auto else self.make_default("GrpHdr")

	@GrpHdr.deleter
	def GrpHdr(self):
		del self._GrpHdr
		self._GrpHdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctRegn', type=ContractRegistration7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader8, min=1, max=1, mutex_group=None, array=False),
	))

