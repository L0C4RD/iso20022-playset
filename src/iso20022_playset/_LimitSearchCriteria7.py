# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import ActiveAmountRange3Choice
from . import ActiveCurrencyCode
from . import BranchAndFinancialInstitutionIdentification8
from . import DateAndPeriod2Choice
from . import LimitType1Choice
from . import PercentageRange1Choice
from . import SystemIdentification2Choice

class LimitSearchCriteria7(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_BilLmtCtrPtyId", "_CurLmtTp", "_DfltLmtTp", "_LmtAmt", "_LmtCcy", "_LmtVldAsOfDt", "_SysId", "_UsdAmt", "_UsdPctg"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', AccountIdentification4Choice, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', AccountIdentification4Choice, False)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', BranchAndFinancialInstitutionIdentification8, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def BilLmtCtrPtyId(self):
		return self._BilLmtCtrPtyId

	@BilLmtCtrPtyId.setter
	def BilLmtCtrPtyId(self, value):
		self._BilLmtCtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'BilLmtCtrPtyId', BranchAndFinancialInstitutionIdentification8, True)

	@BilLmtCtrPtyId.deleter
	def BilLmtCtrPtyId(self):
		del self._BilLmtCtrPtyId
		self._BilLmtCtrPtyId = base_types.UninitialisedField(self, 'BilLmtCtrPtyId', BranchAndFinancialInstitutionIdentification8, True)

	@property
	def CurLmtTp(self):
		return self._CurLmtTp

	@CurLmtTp.setter
	def CurLmtTp(self, value):
		self._CurLmtTp = value if value is not None else base_types.UninitialisedField(self, 'CurLmtTp', LimitType1Choice, True)

	@CurLmtTp.deleter
	def CurLmtTp(self):
		del self._CurLmtTp
		self._CurLmtTp = base_types.UninitialisedField(self, 'CurLmtTp', LimitType1Choice, True)

	@property
	def DfltLmtTp(self):
		return self._DfltLmtTp

	@DfltLmtTp.setter
	def DfltLmtTp(self, value):
		self._DfltLmtTp = value if value is not None else base_types.UninitialisedField(self, 'DfltLmtTp', LimitType1Choice, True)

	@DfltLmtTp.deleter
	def DfltLmtTp(self):
		del self._DfltLmtTp
		self._DfltLmtTp = base_types.UninitialisedField(self, 'DfltLmtTp', LimitType1Choice, True)

	@property
	def LmtAmt(self):
		return self._LmtAmt

	@LmtAmt.setter
	def LmtAmt(self, value):
		self._LmtAmt = value if value is not None else base_types.UninitialisedField(self, 'LmtAmt', ActiveAmountRange3Choice, False)

	@LmtAmt.deleter
	def LmtAmt(self):
		del self._LmtAmt
		self._LmtAmt = base_types.UninitialisedField(self, 'LmtAmt', ActiveAmountRange3Choice, False)

	@property
	def LmtCcy(self):
		return self._LmtCcy

	@LmtCcy.setter
	def LmtCcy(self, value):
		self._LmtCcy = value if value is not None else base_types.UninitialisedField(self, 'LmtCcy', ActiveCurrencyCode, False)

	@LmtCcy.deleter
	def LmtCcy(self):
		del self._LmtCcy
		self._LmtCcy = base_types.UninitialisedField(self, 'LmtCcy', ActiveCurrencyCode, False)

	@property
	def LmtVldAsOfDt(self):
		return self._LmtVldAsOfDt

	@LmtVldAsOfDt.setter
	def LmtVldAsOfDt(self, value):
		self._LmtVldAsOfDt = value if value is not None else base_types.UninitialisedField(self, 'LmtVldAsOfDt', DateAndPeriod2Choice, False)

	@LmtVldAsOfDt.deleter
	def LmtVldAsOfDt(self):
		del self._LmtVldAsOfDt
		self._LmtVldAsOfDt = base_types.UninitialisedField(self, 'LmtVldAsOfDt', DateAndPeriod2Choice, False)

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if value is not None else base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, False)

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, False)

	@property
	def UsdAmt(self):
		return self._UsdAmt

	@UsdAmt.setter
	def UsdAmt(self, value):
		self._UsdAmt = value if value is not None else base_types.UninitialisedField(self, 'UsdAmt', ActiveAmountRange3Choice, False)

	@UsdAmt.deleter
	def UsdAmt(self):
		del self._UsdAmt
		self._UsdAmt = base_types.UninitialisedField(self, 'UsdAmt', ActiveAmountRange3Choice, False)

	@property
	def UsdPctg(self):
		return self._UsdPctg

	@UsdPctg.setter
	def UsdPctg(self, value):
		self._UsdPctg = value if value is not None else base_types.UninitialisedField(self, 'UsdPctg', PercentageRange1Choice, False)

	@UsdPctg.deleter
	def UsdPctg(self):
		del self._UsdPctg
		self._UsdPctg = base_types.UninitialisedField(self, 'UsdPctg', PercentageRange1Choice, False)

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