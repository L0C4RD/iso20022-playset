import base_types
import BranchAndFinancialInstitutionIdentification8
import SystemIdentification2Choice
import AccountIdentification4Choice
import LimitType1Choice

class LimitIdentification8(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_Tp", "_SysId", "_BilLmtCtrPtyId"]
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
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if type(value) != auto else self.make_default("SysId")

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = None

	@property
	def BilLmtCtrPtyId(self):
		return self._BilLmtCtrPtyId

	@BilLmtCtrPtyId.setter
	def BilLmtCtrPtyId(self, value):
		self._BilLmtCtrPtyId = value if type(value) != auto else self.make_default("BilLmtCtrPtyId")

	@BilLmtCtrPtyId.deleter
	def BilLmtCtrPtyId(self):
		del self._BilLmtCtrPtyId
		self._BilLmtCtrPtyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=LimitType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilLmtCtrPtyId', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
	))

