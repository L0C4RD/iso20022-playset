# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import Party50Choice
from . import Purpose2Choice
from . import RemittanceInformation26
from . import RemittanceLocation8

class OriginalItemReference8(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AcctOwnr", "_AcctSvcr", "_Dbtr", "_DbtrAgt", "_IntrmyAgt", "_Purp", "_RltdAcct", "_RltdRmtInf", "_RmtInf"]
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
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', Purpose2Choice, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', Purpose2Choice, False)

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
	def RltdRmtInf(self):
		return self._RltdRmtInf

	@RltdRmtInf.setter
	def RltdRmtInf(self, value):
		self._RltdRmtInf = value if value is not None else base_types.UninitialisedField(self, 'RltdRmtInf', RemittanceLocation8, False)

	@RltdRmtInf.deleter
	def RltdRmtInf(self):
		del self._RltdRmtInf
		self._RltdRmtInf = base_types.UninitialisedField(self, 'RltdRmtInf', RemittanceLocation8, False)

	@property
	def RmtInf(self):
		return self._RmtInf

	@RmtInf.setter
	def RmtInf(self, value):
		self._RmtInf = value if value is not None else base_types.UninitialisedField(self, 'RmtInf', RemittanceInformation26, False)

	@RmtInf.deleter
	def RmtInf(self):
		del self._RmtInf
		self._RmtInf = base_types.UninitialisedField(self, 'RmtInf', RemittanceInformation26, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRmtInf', type=RemittanceLocation8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtInf', type=RemittanceInformation26, min=0, max=1, mutex_group=None, array=False),
	))