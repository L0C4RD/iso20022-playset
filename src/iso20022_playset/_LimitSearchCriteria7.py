from . import base_types
from ._AccountIdentification4Choice import AccountIdentification4Choice
from ._ActiveAmountRange3Choice import ActiveAmountRange3Choice
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._DateAndPeriod2Choice import DateAndPeriod2Choice
from ._LimitType1Choice import LimitType1Choice
from ._PercentageRange1Choice import PercentageRange1Choice
from ._SystemIdentification2Choice import SystemIdentification2Choice

class LimitSearchCriteria7(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_BilLmtCtrPtyId", "_CurLmtTp", "_DfltLmtTp", "_LmtAmt", "_LmtCcy", "_LmtVldAsOfDt", "_SysId", "_UsdAmt", "_UsdPctg"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

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
	def BilLmtCtrPtyId(self):
		return self._BilLmtCtrPtyId

	@BilLmtCtrPtyId.setter
	def BilLmtCtrPtyId(self, value):
		self._BilLmtCtrPtyId = value if type(value) != base_types.auto else self.make_default("BilLmtCtrPtyId")

	@BilLmtCtrPtyId.deleter
	def BilLmtCtrPtyId(self):
		del self._BilLmtCtrPtyId
		self._BilLmtCtrPtyId = None

	@property
	def CurLmtTp(self):
		return self._CurLmtTp

	@CurLmtTp.setter
	def CurLmtTp(self, value):
		self._CurLmtTp = value if type(value) != base_types.auto else self.make_default("CurLmtTp")

	@CurLmtTp.deleter
	def CurLmtTp(self):
		del self._CurLmtTp
		self._CurLmtTp = None

	@property
	def DfltLmtTp(self):
		return self._DfltLmtTp

	@DfltLmtTp.setter
	def DfltLmtTp(self, value):
		self._DfltLmtTp = value if type(value) != base_types.auto else self.make_default("DfltLmtTp")

	@DfltLmtTp.deleter
	def DfltLmtTp(self):
		del self._DfltLmtTp
		self._DfltLmtTp = None

	@property
	def LmtAmt(self):
		return self._LmtAmt

	@LmtAmt.setter
	def LmtAmt(self, value):
		self._LmtAmt = value if type(value) != base_types.auto else self.make_default("LmtAmt")

	@LmtAmt.deleter
	def LmtAmt(self):
		del self._LmtAmt
		self._LmtAmt = None

	@property
	def LmtCcy(self):
		return self._LmtCcy

	@LmtCcy.setter
	def LmtCcy(self, value):
		self._LmtCcy = value if type(value) != base_types.auto else self.make_default("LmtCcy")

	@LmtCcy.deleter
	def LmtCcy(self):
		del self._LmtCcy
		self._LmtCcy = None

	@property
	def LmtVldAsOfDt(self):
		return self._LmtVldAsOfDt

	@LmtVldAsOfDt.setter
	def LmtVldAsOfDt(self, value):
		self._LmtVldAsOfDt = value if type(value) != base_types.auto else self.make_default("LmtVldAsOfDt")

	@LmtVldAsOfDt.deleter
	def LmtVldAsOfDt(self):
		del self._LmtVldAsOfDt
		self._LmtVldAsOfDt = None

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if type(value) != base_types.auto else self.make_default("SysId")

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = None

	@property
	def UsdAmt(self):
		return self._UsdAmt

	@UsdAmt.setter
	def UsdAmt(self, value):
		self._UsdAmt = value if type(value) != base_types.auto else self.make_default("UsdAmt")

	@UsdAmt.deleter
	def UsdAmt(self):
		del self._UsdAmt
		self._UsdAmt = None

	@property
	def UsdPctg(self):
		return self._UsdPctg

	@UsdPctg.setter
	def UsdPctg(self, value):
		self._UsdPctg = value if type(value) != base_types.auto else self.make_default("UsdPctg")

	@UsdPctg.deleter
	def UsdPctg(self):
		del self._UsdPctg
		self._UsdPctg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilLmtCtrPtyId', type=BranchAndFinancialInstitutionIdentification8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CurLmtTp', type=LimitType1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DfltLmtTp', type=LimitType1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LmtAmt', type=ActiveAmountRange3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtVldAsOfDt', type=DateAndPeriod2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsdAmt', type=ActiveAmountRange3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsdPctg', type=PercentageRange1Choice, min=0, max=1, mutex_group=None, array=False),
	))

