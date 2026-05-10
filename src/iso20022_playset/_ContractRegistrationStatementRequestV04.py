from . import base_types
from ._ContractRegistrationStatementRequest3 import ContractRegistrationStatementRequest3
from ._CurrencyControlHeader8 import CurrencyControlHeader8
from ._SupplementaryData1 import SupplementaryData1

class ContractRegistrationStatementRequestV04(base_types._BaseFieldType):

	__slots__ = ["_GrpHdr", "_SplmtryData", "_StmtReq"]
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
	def StmtReq(self):
		return self._StmtReq

	@StmtReq.setter
	def StmtReq(self, value):
		self._StmtReq = value if type(value) != base_types.auto else self.make_default("StmtReq")

	@StmtReq.deleter
	def StmtReq(self):
		del self._StmtReq
		self._StmtReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpHdr', type=CurrencyControlHeader8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtReq', type=ContractRegistrationStatementRequest3, min=1, max=None, mutex_group=None, array=True),
	))

