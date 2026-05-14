# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Amount2Choice import Amount2Choice
from ._CreditDebitCode import CreditDebitCode
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._LimitStatus1Code import LimitStatus1Code
from ._PercentageRate import PercentageRate

class Limit7(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CdtDbtInd", "_RmngAmt", "_StartDtTm", "_Sts", "_UsdAmt", "_UsdAmtCdtDbtInd", "_UsdPctg"]
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
	def RmngAmt(self):
		return self._RmngAmt

	@RmngAmt.setter
	def RmngAmt(self, value):
		self._RmngAmt = value if type(value) != base_types.auto else self.make_default("RmngAmt")

	@RmngAmt.deleter
	def RmngAmt(self):
		del self._RmngAmt
		self._RmngAmt = None

	@property
	def StartDtTm(self):
		return self._StartDtTm

	@StartDtTm.setter
	def StartDtTm(self, value):
		self._StartDtTm = value if type(value) != base_types.auto else self.make_default("StartDtTm")

	@StartDtTm.deleter
	def StartDtTm(self):
		del self._StartDtTm
		self._StartDtTm = None

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
	def UsdAmtCdtDbtInd(self):
		return self._UsdAmtCdtDbtInd

	@UsdAmtCdtDbtInd.setter
	def UsdAmtCdtDbtInd(self, value):
		self._UsdAmtCdtDbtInd = value if type(value) != base_types.auto else self.make_default("UsdAmtCdtDbtInd")

	@UsdAmtCdtDbtInd.deleter
	def UsdAmtCdtDbtInd(self):
		del self._UsdAmtCdtDbtInd
		self._UsdAmtCdtDbtInd = None

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
		base_types.FieldEntry(name='Amt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngAmt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=LimitStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsdAmt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsdAmtCdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UsdPctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))