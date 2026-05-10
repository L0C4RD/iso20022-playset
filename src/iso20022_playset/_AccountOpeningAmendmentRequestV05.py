from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .OperationMandate7 import OperationMandate7
from .Group6 import Group6
from .AccountContract2 import AccountContract2
from .CustomerAccount4 import CustomerAccount4
from .Organisation42 import Organisation42
from .ContractDocument1 import ContractDocument1
from .References4 import References4
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .PartyAndSignature4 import PartyAndSignature4
from .CashAccount40 import CashAccount40
from .OrganisationIdentification39 import OrganisationIdentification39

class AccountOpeningAmendmentRequestV05(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_SplmtryData", "_Fr", "_Mndt", "_CtrctDts", "_Grp", "_AcctSvcrId", "_Org", "_RefAcct", "_UndrlygMstrAgrmt", "_Refs", "_Acct"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != base_types.auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

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
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if type(value) != base_types.auto else self.make_default("Fr")

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = None

	@property
	def Mndt(self):
		return self._Mndt

	@Mndt.setter
	def Mndt(self, value):
		self._Mndt = value if type(value) != base_types.auto else self.make_default("Mndt")

	@Mndt.deleter
	def Mndt(self):
		del self._Mndt
		self._Mndt = None

	@property
	def CtrctDts(self):
		return self._CtrctDts

	@CtrctDts.setter
	def CtrctDts(self, value):
		self._CtrctDts = value if type(value) != base_types.auto else self.make_default("CtrctDts")

	@CtrctDts.deleter
	def CtrctDts(self):
		del self._CtrctDts
		self._CtrctDts = None

	@property
	def Grp(self):
		return self._Grp

	@Grp.setter
	def Grp(self, value):
		self._Grp = value if type(value) != base_types.auto else self.make_default("Grp")

	@Grp.deleter
	def Grp(self):
		del self._Grp
		self._Grp = None

	@property
	def AcctSvcrId(self):
		return self._AcctSvcrId

	@AcctSvcrId.setter
	def AcctSvcrId(self, value):
		self._AcctSvcrId = value if type(value) != base_types.auto else self.make_default("AcctSvcrId")

	@AcctSvcrId.deleter
	def AcctSvcrId(self):
		del self._AcctSvcrId
		self._AcctSvcrId = None

	@property
	def Org(self):
		return self._Org

	@Org.setter
	def Org(self, value):
		self._Org = value if type(value) != base_types.auto else self.make_default("Org")

	@Org.deleter
	def Org(self):
		del self._Org
		self._Org = None

	@property
	def RefAcct(self):
		return self._RefAcct

	@RefAcct.setter
	def RefAcct(self, value):
		self._RefAcct = value if type(value) != base_types.auto else self.make_default("RefAcct")

	@RefAcct.deleter
	def RefAcct(self):
		del self._RefAcct
		self._RefAcct = None

	@property
	def UndrlygMstrAgrmt(self):
		return self._UndrlygMstrAgrmt

	@UndrlygMstrAgrmt.setter
	def UndrlygMstrAgrmt(self, value):
		self._UndrlygMstrAgrmt = value if type(value) != base_types.auto else self.make_default("UndrlygMstrAgrmt")

	@UndrlygMstrAgrmt.deleter
	def UndrlygMstrAgrmt(self):
		del self._UndrlygMstrAgrmt
		self._UndrlygMstrAgrmt = None

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != base_types.auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Fr', type=OrganisationIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mndt', type=OperationMandate7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctDts', type=AccountContract2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grp', type=Group6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcrId', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Org', type=Organisation42, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygMstrAgrmt', type=ContractDocument1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=References4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=CustomerAccount4, min=1, max=1, mutex_group=None, array=False),
	))

