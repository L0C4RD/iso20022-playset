import base_types
import SystemPartyIdentification8
import BranchAndFinancialInstitutionIdentification8
import IntraBalanceStatusAndReason2
import CashAccount40
import IntraBalanceMovement7

class IntraBalanceMovements4(base_types._BaseFieldType):

	__slots__ = ["_CshAcctSvcr", "_CshAcctOwnr", "_CshAcct", "_StsAndRsn", "_Mvmnt"]
	@property
	def CshAcctSvcr(self):
		return self._CshAcctSvcr

	@CshAcctSvcr.setter
	def CshAcctSvcr(self, value):
		self._CshAcctSvcr = value if type(value) != auto else self.make_default("CshAcctSvcr")

	@CshAcctSvcr.deleter
	def CshAcctSvcr(self):
		del self._CshAcctSvcr
		self._CshAcctSvcr = None

	@property
	def CshAcctOwnr(self):
		return self._CshAcctOwnr

	@CshAcctOwnr.setter
	def CshAcctOwnr(self, value):
		self._CshAcctOwnr = value if type(value) != auto else self.make_default("CshAcctOwnr")

	@CshAcctOwnr.deleter
	def CshAcctOwnr(self):
		del self._CshAcctOwnr
		self._CshAcctOwnr = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def StsAndRsn(self):
		return self._StsAndRsn

	@StsAndRsn.setter
	def StsAndRsn(self, value):
		self._StsAndRsn = value if type(value) != auto else self.make_default("StsAndRsn")

	@StsAndRsn.deleter
	def StsAndRsn(self):
		del self._StsAndRsn
		self._StsAndRsn = None

	@property
	def Mvmnt(self):
		return self._Mvmnt

	@Mvmnt.setter
	def Mvmnt(self, value):
		self._Mvmnt = value if type(value) != auto else self.make_default("Mvmnt")

	@Mvmnt.deleter
	def Mvmnt(self):
		del self._Mvmnt
		self._Mvmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshAcctSvcr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcctOwnr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsAndRsn', type=IntraBalanceStatusAndReason2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mvmnt', type=IntraBalanceMovement7, min=1, max=None, mutex_group=None, array=True),
	))

