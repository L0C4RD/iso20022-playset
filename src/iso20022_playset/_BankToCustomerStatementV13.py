from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .AccountStatement14 import AccountStatement14
from .GroupHeader116 import GroupHeader116

class BankToCustomerStatementV13(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_Stmt", "_GrpHdr"]
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
	def Stmt(self):
		return self._Stmt

	@Stmt.setter
	def Stmt(self, value):
		self._Stmt = value if type(value) != base_types.auto else self.make_default("Stmt")

	@Stmt.deleter
	def Stmt(self):
		del self._Stmt
		self._Stmt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Stmt', type=AccountStatement14, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GrpHdr', type=GroupHeader116, min=1, max=1, mutex_group=None, array=False),
	))

