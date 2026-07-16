# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import ISODate
from . import Max35Text
from . import NotificationItem10
from . import Party50Choice

class AccountNotification26(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AcctOwnr", "_AcctSvcr", "_Dbtr", "_DbtrAgt", "_Id", "_IntrmyAgt", "_Itm", "_RltdAcct", "_TtlAmt", "_XpctdValDt"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', Party50Choice, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', Party50Choice, False)

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = base_types.UninitialisedField(self, 'AcctSvcr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', Party50Choice, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', Party50Choice, False)

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = base_types.UninitialisedField(self, 'DbtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def IntrmyAgt(self):
		return self._IntrmyAgt

	@IntrmyAgt.setter
	def IntrmyAgt(self, value):
		self._IntrmyAgt = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt', BranchAndFinancialInstitutionIdentification8, False)

	@IntrmyAgt.deleter
	def IntrmyAgt(self):
		del self._IntrmyAgt
		self._IntrmyAgt = base_types.UninitialisedField(self, 'IntrmyAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def Itm(self):
		return self._Itm

	@Itm.setter
	def Itm(self, value):
		self._Itm = value if value is not None else base_types.UninitialisedField(self, 'Itm', NotificationItem10, True)

	@Itm.deleter
	def Itm(self):
		del self._Itm
		self._Itm = base_types.UninitialisedField(self, 'Itm', NotificationItem10, True)

	@property
	def RltdAcct(self):
		return self._RltdAcct

	@RltdAcct.setter
	def RltdAcct(self, value):
		self._RltdAcct = value if value is not None else base_types.UninitialisedField(self, 'RltdAcct', CashAccount40, False)

	@RltdAcct.deleter
	def RltdAcct(self):
		del self._RltdAcct
		self._RltdAcct = base_types.UninitialisedField(self, 'RltdAcct', CashAccount40, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def XpctdValDt(self):
		return self._XpctdValDt

	@XpctdValDt.setter
	def XpctdValDt(self, value):
		self._XpctdValDt = value if value is not None else base_types.UninitialisedField(self, 'XpctdValDt', ISODate, False)

	@XpctdValDt.deleter
	def XpctdValDt(self):
		del self._XpctdValDt
		self._XpctdValDt = base_types.UninitialisedField(self, 'XpctdValDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Itm', type=NotificationItem10, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))