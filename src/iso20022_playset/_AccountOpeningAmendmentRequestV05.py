# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountContract2
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import ContractDocument1
from . import CustomerAccount4
from . import Group6
from . import OperationMandate7
from . import Organisation42
from . import OrganisationIdentification39
from . import PartyAndSignature4
from . import References4
from . import SupplementaryData1

class AccountOpeningAmendmentRequestV05(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AcctSvcrId", "_CtrctDts", "_DgtlSgntr", "_Fr", "_Grp", "_Mndt", "_Org", "_RefAcct", "_Refs", "_SplmtryData", "_UndrlygMstrAgrmt"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CustomerAccount4, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CustomerAccount4, False)

	@property
	def AcctSvcrId(self):
		return self._AcctSvcrId

	@AcctSvcrId.setter
	def AcctSvcrId(self, value):
		self._AcctSvcrId = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrId', BranchAndFinancialInstitutionIdentification8, False)

	@AcctSvcrId.deleter
	def AcctSvcrId(self):
		del self._AcctSvcrId
		self._AcctSvcrId = base_types.UninitialisedField(self, 'AcctSvcrId', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def CtrctDts(self):
		return self._CtrctDts

	@CtrctDts.setter
	def CtrctDts(self, value):
		self._CtrctDts = value if value is not None else base_types.UninitialisedField(self, 'CtrctDts', AccountContract2, False)

	@CtrctDts.deleter
	def CtrctDts(self):
		del self._CtrctDts
		self._CtrctDts = base_types.UninitialisedField(self, 'CtrctDts', AccountContract2, False)

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature4, True)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature4, True)

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if value is not None else base_types.UninitialisedField(self, 'Fr', OrganisationIdentification39, False)

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = base_types.UninitialisedField(self, 'Fr', OrganisationIdentification39, False)

	@property
	def Grp(self):
		return self._Grp

	@Grp.setter
	def Grp(self, value):
		self._Grp = value if value is not None else base_types.UninitialisedField(self, 'Grp', Group6, True)

	@Grp.deleter
	def Grp(self):
		del self._Grp
		self._Grp = base_types.UninitialisedField(self, 'Grp', Group6, True)

	@property
	def Mndt(self):
		return self._Mndt

	@Mndt.setter
	def Mndt(self, value):
		self._Mndt = value if value is not None else base_types.UninitialisedField(self, 'Mndt', OperationMandate7, True)

	@Mndt.deleter
	def Mndt(self):
		del self._Mndt
		self._Mndt = base_types.UninitialisedField(self, 'Mndt', OperationMandate7, True)

	@property
	def Org(self):
		return self._Org

	@Org.setter
	def Org(self, value):
		self._Org = value if value is not None else base_types.UninitialisedField(self, 'Org', Organisation42, False)

	@Org.deleter
	def Org(self):
		del self._Org
		self._Org = base_types.UninitialisedField(self, 'Org', Organisation42, False)

	@property
	def RefAcct(self):
		return self._RefAcct

	@RefAcct.setter
	def RefAcct(self, value):
		self._RefAcct = value if value is not None else base_types.UninitialisedField(self, 'RefAcct', CashAccount40, False)

	@RefAcct.deleter
	def RefAcct(self):
		del self._RefAcct
		self._RefAcct = base_types.UninitialisedField(self, 'RefAcct', CashAccount40, False)

	@property
	def Refs(self):
		return self._Refs

	@Refs.setter
	def Refs(self, value):
		self._Refs = value if value is not None else base_types.UninitialisedField(self, 'Refs', References4, False)

	@Refs.deleter
	def Refs(self):
		del self._Refs
		self._Refs = base_types.UninitialisedField(self, 'Refs', References4, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def UndrlygMstrAgrmt(self):
		return self._UndrlygMstrAgrmt

	@UndrlygMstrAgrmt.setter
	def UndrlygMstrAgrmt(self, value):
		self._UndrlygMstrAgrmt = value if value is not None else base_types.UninitialisedField(self, 'UndrlygMstrAgrmt', ContractDocument1, False)

	@UndrlygMstrAgrmt.deleter
	def UndrlygMstrAgrmt(self):
		del self._UndrlygMstrAgrmt
		self._UndrlygMstrAgrmt = base_types.UninitialisedField(self, 'UndrlygMstrAgrmt', ContractDocument1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CustomerAccount4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrId', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctDts', type=AccountContract2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Fr', type=OrganisationIdentification39, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grp', type=Group6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mndt', type=OperationMandate7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Org', type=Organisation42, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Refs', type=References4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygMstrAgrmt', type=ContractDocument1, min=0, max=1, mutex_group=None, array=False),
	))