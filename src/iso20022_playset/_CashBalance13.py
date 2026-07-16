# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceRestrictionType1
from . import BalanceStatus1Code
from . import BalanceType11Choice
from . import CreditDebitCode
from . import DateAndDateTime2Choice
from . import ImpliedCurrencyAndAmount
from . import Number

class CashBalance13(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CdtDbtInd", "_NbOfPmts", "_PrcgDt", "_RstrctnTp", "_Sts", "_Tp", "_ValDt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def NbOfPmts(self):
		return self._NbOfPmts

	@NbOfPmts.setter
	def NbOfPmts(self, value):
		self._NbOfPmts = value if value is not None else base_types.UninitialisedField(self, 'NbOfPmts', Number, False)

	@NbOfPmts.deleter
	def NbOfPmts(self):
		del self._NbOfPmts
		self._NbOfPmts = base_types.UninitialisedField(self, 'NbOfPmts', Number, False)

	@property
	def PrcgDt(self):
		return self._PrcgDt

	@PrcgDt.setter
	def PrcgDt(self, value):
		self._PrcgDt = value if value is not None else base_types.UninitialisedField(self, 'PrcgDt', DateAndDateTime2Choice, False)

	@PrcgDt.deleter
	def PrcgDt(self):
		del self._PrcgDt
		self._PrcgDt = base_types.UninitialisedField(self, 'PrcgDt', DateAndDateTime2Choice, False)

	@property
	def RstrctnTp(self):
		return self._RstrctnTp

	@RstrctnTp.setter
	def RstrctnTp(self, value):
		self._RstrctnTp = value if value is not None else base_types.UninitialisedField(self, 'RstrctnTp', BalanceRestrictionType1, False)

	@RstrctnTp.deleter
	def RstrctnTp(self):
		del self._RstrctnTp
		self._RstrctnTp = base_types.UninitialisedField(self, 'RstrctnTp', BalanceRestrictionType1, False)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', BalanceStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', BalanceStatus1Code, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', BalanceType11Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', BalanceType11Choice, False)

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if value is not None else base_types.UninitialisedField(self, 'ValDt', DateAndDateTime2Choice, False)

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = base_types.UninitialisedField(self, 'ValDt', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfPmts', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctnTp', type=BalanceRestrictionType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=BalanceStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BalanceType11Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))