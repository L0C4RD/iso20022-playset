# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BalanceStatus1Code import BalanceStatus1Code
from ._BalanceType9Choice import BalanceType9Choice
from ._CreditDebitCode import CreditDebitCode
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Number import Number

class CashBalance11(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CdtDbtInd", "_NbOfPmts", "_Sts", "_Tp", "_ValDt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def NbOfPmts(self):
		return self._NbOfPmts

	@NbOfPmts.setter
	def NbOfPmts(self, value):
		self._NbOfPmts = value if type(value) != base_types.auto else self.make_default("NbOfPmts")

	@NbOfPmts.deleter
	def NbOfPmts(self):
		del self._NbOfPmts
		self._NbOfPmts = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfPmts', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=BalanceStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=BalanceType9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))