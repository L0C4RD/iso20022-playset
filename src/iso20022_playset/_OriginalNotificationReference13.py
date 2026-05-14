# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._ISODate import ISODate
from ._OriginalItemAndStatus8 import OriginalItemAndStatus8
from ._Party50Choice import Party50Choice

class OriginalNotificationReference13(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AcctOwnr", "_AcctSvcr", "_Dbtr", "_DbtrAgt", "_IntrmyAgt", "_OrgnlItmAndSts", "_RltdAcct", "_TtlAmt", "_XpctdValDt"]
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

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def AcctSvcr(self):
		return self._AcctSvcr

	@AcctSvcr.setter
	def AcctSvcr(self, value):
		self._AcctSvcr = value if type(value) != base_types.auto else self.make_default("AcctSvcr")

	@AcctSvcr.deleter
	def AcctSvcr(self):
		del self._AcctSvcr
		self._AcctSvcr = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != base_types.auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != base_types.auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

	@property
	def IntrmyAgt(self):
		return self._IntrmyAgt

	@IntrmyAgt.setter
	def IntrmyAgt(self, value):
		self._IntrmyAgt = value if type(value) != base_types.auto else self.make_default("IntrmyAgt")

	@IntrmyAgt.deleter
	def IntrmyAgt(self):
		del self._IntrmyAgt
		self._IntrmyAgt = None

	@property
	def OrgnlItmAndSts(self):
		return self._OrgnlItmAndSts

	@OrgnlItmAndSts.setter
	def OrgnlItmAndSts(self, value):
		self._OrgnlItmAndSts = value if type(value) != base_types.auto else self.make_default("OrgnlItmAndSts")

	@OrgnlItmAndSts.deleter
	def OrgnlItmAndSts(self):
		del self._OrgnlItmAndSts
		self._OrgnlItmAndSts = None

	@property
	def RltdAcct(self):
		return self._RltdAcct

	@RltdAcct.setter
	def RltdAcct(self, value):
		self._RltdAcct = value if type(value) != base_types.auto else self.make_default("RltdAcct")

	@RltdAcct.deleter
	def RltdAcct(self):
		del self._RltdAcct
		self._RltdAcct = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def XpctdValDt(self):
		return self._XpctdValDt

	@XpctdValDt.setter
	def XpctdValDt(self, value):
		self._XpctdValDt = value if type(value) != base_types.auto else self.make_default("XpctdValDt")

	@XpctdValDt.deleter
	def XpctdValDt(self):
		del self._XpctdValDt
		self._XpctdValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlItmAndSts', type=OriginalItemAndStatus8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))