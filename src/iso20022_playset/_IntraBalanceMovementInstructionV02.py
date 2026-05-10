from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._IntraBalance5 import IntraBalance5
from ._Linkages57 import Linkages57
from ._Max35Text import Max35Text
from ._NumberCount1Choice import NumberCount1Choice
from ._SupplementaryData1 import SupplementaryData1
from ._SystemPartyIdentification8 import SystemPartyIdentification8
from ._TransactionAndDocumentIdentification6 import TransactionAndDocumentIdentification6

class IntraBalanceMovementInstructionV02(base_types._BaseFieldType):

	__slots__ = ["_CorpActnEvtId", "_CshAcct", "_CshAcctOwnr", "_CshAcctSvcr", "_Id", "_IntraBal", "_Lnkgs", "_NbCounts", "_SplmtryData"]
	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if type(value) != base_types.auto else self.make_default("CorpActnEvtId")

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if type(value) != base_types.auto else self.make_default("CshAcctOwnr")

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = None

	@property
	def CshAcctSvcr(self):
		return self._CshAcctSvcr

	@CshAcctSvcr.setter
	def CshAcctSvcr(self, value):
		self._CshAcctSvcr = value if type(value) != base_types.auto else self.make_default("CshAcctSvcr")

	@CshAcctSvcr.deleter
	def CshAcctSvcr(self):
		del self._CshAcctSvcr
		self._CshAcctSvcr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def IntraBal(self):
		return self._IntraBal

	@IntraBal.setter
	def IntraBal(self, value):
		self._IntraBal = value if type(value) != base_types.auto else self.make_default("IntraBal")

	@IntraBal.deleter
	def IntraBal(self):
		del self._IntraBal
		self._IntraBal = None

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if type(value) != base_types.auto else self.make_default("Lnkgs")

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = None

	@property
	def NbCounts(self):
		return self._NbCounts

	@NbCounts.setter
	def NbCounts(self, value):
		self._NbCounts = value if type(value) != base_types.auto else self.make_default("NbCounts")

	@NbCounts.deleter
	def NbCounts(self):
		del self._NbCounts
		self._NbCounts = None

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
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=TransactionAndDocumentIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraBal', type=IntraBalance5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages57, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbCounts', type=NumberCount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

