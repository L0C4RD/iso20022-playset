# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountContract3
from . import AccountForAction1
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import ContractDocument1
from . import CustomerAccount5
from . import Group6
from . import OperationMandate7

class AccountReport36(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_BalTrfAcct", "_CtrctDts", "_Grp", "_Mndt", "_RefAcct", "_TrfAcctSvcrId", "_UndrlygMstrAgrmt"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CustomerAccount5, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CustomerAccount5, False)

	@property
	def BalTrfAcct(self):
		return self._BalTrfAcct

	@BalTrfAcct.setter
	def BalTrfAcct(self, value):
		self._BalTrfAcct = value if value is not None else base_types.UninitialisedField(self, 'BalTrfAcct', AccountForAction1, False)

	@BalTrfAcct.deleter
	def BalTrfAcct(self):
		del self._BalTrfAcct
		self._BalTrfAcct = base_types.UninitialisedField(self, 'BalTrfAcct', AccountForAction1, False)

	@property
	def CtrctDts(self):
		return self._CtrctDts

	@CtrctDts.setter
	def CtrctDts(self, value):
		self._CtrctDts = value if value is not None else base_types.UninitialisedField(self, 'CtrctDts', AccountContract3, False)

	@CtrctDts.deleter
	def CtrctDts(self):
		del self._CtrctDts
		self._CtrctDts = base_types.UninitialisedField(self, 'CtrctDts', AccountContract3, False)

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
	def TrfAcctSvcrId(self):
		return self._TrfAcctSvcrId

	@TrfAcctSvcrId.setter
	def TrfAcctSvcrId(self, value):
		self._TrfAcctSvcrId = value if value is not None else base_types.UninitialisedField(self, 'TrfAcctSvcrId', BranchAndFinancialInstitutionIdentification8, False)

	@TrfAcctSvcrId.deleter
	def TrfAcctSvcrId(self):
		del self._TrfAcctSvcrId
		self._TrfAcctSvcrId = base_types.UninitialisedField(self, 'TrfAcctSvcrId', BranchAndFinancialInstitutionIdentification8, False)

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
		base_types.FieldEntry(name='Acct', type=CustomerAccount5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTrfAcct', type=AccountForAction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctDts', type=AccountContract3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grp', type=Group6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Mndt', type=OperationMandate7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RefAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfAcctSvcrId', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygMstrAgrmt', type=ContractDocument1, min=0, max=1, mutex_group=None, array=False),
	))