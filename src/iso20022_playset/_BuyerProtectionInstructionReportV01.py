from . import base_types
from ._CorporateActionDetails1 import CorporateActionDetails1
from ._FinancialInstitutionIdentification28 import FinancialInstitutionIdentification28
from ._Pagination1 import Pagination1
from ._Statement87 import Statement87
from ._SupplementaryData1 import SupplementaryData1

class BuyerProtectionInstructionReportV01(base_types._BaseFieldType):

	__slots__ = ["_CorpActnDtls", "_FIId", "_Pgntn", "_SplmtryData", "_StmtGnlDtls"]
	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if type(value) != base_types.auto else self.make_default("CorpActnDtls")

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = None

	@property
	def FIId(self):
		return self._FIId

	@FIId.setter
	def FIId(self, value):
		self._FIId = value if type(value) != base_types.auto else self.make_default("FIId")

	@FIId.deleter
	def FIId(self):
		del self._FIId
		self._FIId = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

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
	def StmtGnlDtls(self):
		return self._StmtGnlDtls

	@StmtGnlDtls.setter
	def StmtGnlDtls(self, value):
		self._StmtGnlDtls = value if type(value) != base_types.auto else self.make_default("StmtGnlDtls")

	@StmtGnlDtls.deleter
	def StmtGnlDtls(self):
		del self._StmtGnlDtls
		self._StmtGnlDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateActionDetails1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FIId', type=FinancialInstitutionIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtGnlDtls', type=Statement87, min=1, max=1, mutex_group=None, array=False),
	))

