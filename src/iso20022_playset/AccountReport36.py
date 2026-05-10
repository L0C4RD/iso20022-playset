from . import base_types
import AccountForAction1
import ContractDocument1
import AccountContract3
import BranchAndFinancialInstitutionIdentification8
import CustomerAccount5
import OperationMandate7
import Group6
import CashAccount40

class AccountReport36(base_types._BaseFieldType):

	__slots__ = ["_RefAcct", "_Mndt", "_Grp", "_CtrctDts", "_UndrlygMstrAgrmt", "_TrfAcctSvcrId", "_BalTrfAcct", "_Acct"]
	@property
	def RefAcct(self):
		return self._RefAcct

	@RefAcct.setter
	def RefAcct(self, value):
		self._RefAcct = value if type(value) != auto else self.make_default("RefAcct")

	@RefAcct.deleter
	def RefAcct(self):
		del self._RefAcct
		self._RefAcct = None

	@property
	def Mndt(self):
		return self._Mndt

	@Mndt.setter
	def Mndt(self, value):
		self._Mndt = value if type(value) != auto else self.make_default("Mndt")

	@Mndt.deleter
	def Mndt(self):
		del self._Mndt
		self._Mndt = None

	@property
	def Grp(self):
		return self._Grp

	@Grp.setter
	def Grp(self, value):
		self._Grp = value if type(value) != auto else self.make_default("Grp")

	@Grp.deleter
	def Grp(self):
		del self._Grp
		self._Grp = None

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
	def UndrlygMstrAgrmt(self):
		return self._UndrlygMstrAgrmt

	@UndrlygMstrAgrmt.setter
	def UndrlygMstrAgrmt(self, value):
		self._UndrlygMstrAgrmt = value if type(value) != auto else self.make_default("UndrlygMstrAgrmt")

	@UndrlygMstrAgrmt.deleter
	def UndrlygMstrAgrmt(self):
		del self._UndrlygMstrAgrmt
		self._UndrlygMstrAgrmt = None

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
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RefAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mndt', type=OperationMandate7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Grp', type=Group6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctDts', type=AccountContract3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygMstrAgrmt', type=ContractDocument1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfAcctSvcrId', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTrfAcct', type=AccountForAction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=CustomerAccount5, min=1, max=1, mutex_group=None, array=False),
	))

