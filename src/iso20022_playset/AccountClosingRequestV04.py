from . import base_types
from .References4 import References4
from .AccountForAction2 import AccountForAction2
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from .AccountForAction1 import AccountForAction1
from .SupplementaryData1 import SupplementaryData1
from .OrganisationIdentification39 import OrganisationIdentification39
from .PartyAndSignature4 import PartyAndSignature4
from .Organisation44 import Organisation44
from .AccountContract4 import AccountContract4

class AccountClosingRequestV04(base_types._BaseFieldType):

	__slots__ = ["_BalTrfAcct", "_Fr", "_CtrctDts", "_TrfAcctSvcrId", "_AcctId", "_DgtlSgntr", "_OrgId", "_SplmtryData", "_AcctSvcrId", "_Refs"]
	@property
	def BalTrfAcct(self):
		return self._BalTrfAcct

	@BalTrfAcct.setter
	def BalTrfAcct(self, value):
		self._BalTrfAcct = value if type(value) != auto else self.make_default("BalTrfAcct")

	@BalTrfAcct.deleter
	def BalTrfAcct(self):
		del self._BalTrfAcct
		self._BalTrfAcct = None

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if type(value) != auto else self.make_default("Fr")

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = None

	@property
	def CtrctDts(self):
		return self._CtrctDts

	@CtrctDts.setter
	def CtrctDts(self, value):
		self._CtrctDts = value if type(value) != auto else self.make_default("CtrctDts")

	@CtrctDts.deleter
	def CtrctDts(self):
		del self._CtrctDts
		self._CtrctDts = None

	@property
	def TrfAcctSvcrId(self):
		return self._TrfAcctSvcrId

	@TrfAcctSvcrId.setter
	def TrfAcctSvcrId(self, value):
		self._TrfAcctSvcrId = value if type(value) != auto else self.make_default("TrfAcctSvcrId")

	@TrfAcctSvcrId.deleter
	def TrfAcctSvcrId(self):
		del self._TrfAcctSvcrId
		self._TrfAcctSvcrId = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def OrgId(self):
		return self._OrgId

	@OrgId.setter
	def OrgId(self, value):
		self._OrgId = value if type(value) != auto else self.make_default("OrgId")

	@OrgId.deleter
	def OrgId(self):
		del self._OrgId
		self._OrgId = None

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
	def AcctSvcrId(self):
		return self._AcctSvcrId

	@AcctSvcrId.setter
	def AcctSvcrId(self, value):
		self._AcctSvcrId = value if type(value) != auto else self.make_default("AcctSvcrId")

	@AcctSvcrId.deleter
	def AcctSvcrId(self):
		del self._AcctSvcrId
		self._AcctSvcrId = None

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if type(value) != auto else self.make_default("Refs")

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalTrfAcct', type=AccountForAction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fr', type=OrganisationIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctDts', type=AccountContract4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfAcctSvcrId', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=AccountForAction2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgId', type=Organisation44, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctSvcrId', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=References4, min=1, max=1, mutex_group=None, array=False),
	))

