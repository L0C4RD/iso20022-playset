# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import ChargeType3Choice
from . import ChargesPerTypeRecord5
from . import Max140Text
from . import Max35Text
from . import TotalCharges7

class ChargesPerType5(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ChrgsAcct", "_ChrgsAcctOwnr", "_ChrgsId", "_Rcrd", "_Tp", "_TtlChrgsPerChrgTp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max140Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max140Text, False)

	@property
	def ChrgsAcct(self):
		return self._ChrgsAcct

	@ChrgsAcct.setter
	def ChrgsAcct(self, value):
		self._ChrgsAcct = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAcct', CashAccount40, False)

	@ChrgsAcct.deleter
	def ChrgsAcct(self):
		del self._ChrgsAcct
		self._ChrgsAcct = base_types.UninitialisedField(self, 'ChrgsAcct', CashAccount40, False)

	@property
	def ChrgsAcctOwnr(self):
		return self._ChrgsAcctOwnr

	@ChrgsAcctOwnr.setter
	def ChrgsAcctOwnr(self, value):
		self._ChrgsAcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAcctOwnr', BranchAndFinancialInstitutionIdentification8, False)

	@ChrgsAcctOwnr.deleter
	def ChrgsAcctOwnr(self):
		del self._ChrgsAcctOwnr
		self._ChrgsAcctOwnr = base_types.UninitialisedField(self, 'ChrgsAcctOwnr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def ChrgsId(self):
		return self._ChrgsId

	@ChrgsId.setter
	def ChrgsId(self, value):
		self._ChrgsId = value if value is not None else base_types.UninitialisedField(self, 'ChrgsId', Max35Text, False)

	@ChrgsId.deleter
	def ChrgsId(self):
		del self._ChrgsId
		self._ChrgsId = base_types.UninitialisedField(self, 'ChrgsId', Max35Text, False)

	@property
	def Rcrd(self):
		return self._Rcrd

	@Rcrd.setter
	def Rcrd(self, value):
		self._Rcrd = value if value is not None else base_types.UninitialisedField(self, 'Rcrd', ChargesPerTypeRecord5, True)

	@Rcrd.deleter
	def Rcrd(self):
		del self._Rcrd
		self._Rcrd = base_types.UninitialisedField(self, 'Rcrd', ChargesPerTypeRecord5, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ChargeType3Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ChargeType3Choice, False)

	@property
	def TtlChrgsPerChrgTp(self):
		return self._TtlChrgsPerChrgTp

	@TtlChrgsPerChrgTp.setter
	def TtlChrgsPerChrgTp(self, value):
		self._TtlChrgsPerChrgTp = value if value is not None else base_types.UninitialisedField(self, 'TtlChrgsPerChrgTp', TotalCharges7, False)

	@TtlChrgsPerChrgTp.deleter
	def TtlChrgsPerChrgTp(self):
		del self._TtlChrgsPerChrgTp
		self._TtlChrgsPerChrgTp = base_types.UninitialisedField(self, 'TtlChrgsPerChrgTp', TotalCharges7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctOwnr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcrd', type=ChargesPerTypeRecord5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=ChargeType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlChrgsPerChrgTp', type=TotalCharges7, min=0, max=1, mutex_group=None, array=False),
	))