# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountIdentification4Choice import AccountIdentification4Choice
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._Amount2Choice import Amount2Choice
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._CreditDebitCode import CreditDebitCode
from ._DatePeriod3 import DatePeriod3
from ._ExecutionType1Choice import ExecutionType1Choice
from ._Frequency2Code import Frequency2Code
from ._Max35Text import Max35Text
from ._Number import Number
from ._StandingOrderTotalAmount1 import StandingOrderTotalAmount1
from ._StandingOrderType1Choice import StandingOrderType1Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class StandingOrder11(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AssoctdPoolAcct", "_Ccy", "_CdtDbtInd", "_Cdtr", "_CdtrAcct", "_Dbtr", "_DbtrAcct", "_ExctnTp", "_Frqcy", "_LkSetId", "_LkSetOrdrId", "_LkSetOrdrSeq", "_Ref", "_RspnsblPty", "_SysMmb", "_Tp", "_TtlsPerStgOrdr", "_VldtyPrd", "_ZeroSweepInd"]
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
	def AssoctdPoolAcct(self):
		return self._AssoctdPoolAcct

	@AssoctdPoolAcct.setter
	def AssoctdPoolAcct(self, value):
		self._AssoctdPoolAcct = value if type(value) != base_types.auto else self.make_default("AssoctdPoolAcct")

	@AssoctdPoolAcct.deleter
	def AssoctdPoolAcct(self):
		del self._AssoctdPoolAcct
		self._AssoctdPoolAcct = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

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
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != base_types.auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if type(value) != base_types.auto else self.make_default("CdtrAcct")

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = None

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
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if type(value) != base_types.auto else self.make_default("DbtrAcct")

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = None

	@property
	def ExctnTp(self):
		return self._ExctnTp

	@ExctnTp.setter
	def ExctnTp(self, value):
		self._ExctnTp = value if type(value) != base_types.auto else self.make_default("ExctnTp")

	@ExctnTp.deleter
	def ExctnTp(self):
		del self._ExctnTp
		self._ExctnTp = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def LkSetId(self):
		return self._LkSetId

	@LkSetId.setter
	def LkSetId(self, value):
		self._LkSetId = value if type(value) != base_types.auto else self.make_default("LkSetId")

	@LkSetId.deleter
	def LkSetId(self):
		del self._LkSetId
		self._LkSetId = None

	@property
	def LkSetOrdrId(self):
		return self._LkSetOrdrId

	@LkSetOrdrId.setter
	def LkSetOrdrId(self, value):
		self._LkSetOrdrId = value if type(value) != base_types.auto else self.make_default("LkSetOrdrId")

	@LkSetOrdrId.deleter
	def LkSetOrdrId(self):
		del self._LkSetOrdrId
		self._LkSetOrdrId = None

	@property
	def LkSetOrdrSeq(self):
		return self._LkSetOrdrSeq

	@LkSetOrdrSeq.setter
	def LkSetOrdrSeq(self, value):
		self._LkSetOrdrSeq = value if type(value) != base_types.auto else self.make_default("LkSetOrdrSeq")

	@LkSetOrdrSeq.deleter
	def LkSetOrdrSeq(self):
		del self._LkSetOrdrSeq
		self._LkSetOrdrSeq = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def RspnsblPty(self):
		return self._RspnsblPty

	@RspnsblPty.setter
	def RspnsblPty(self, value):
		self._RspnsblPty = value if type(value) != base_types.auto else self.make_default("RspnsblPty")

	@RspnsblPty.deleter
	def RspnsblPty(self):
		del self._RspnsblPty
		self._RspnsblPty = None

	@property
	def SysMmb(self):
		return self._SysMmb

	@SysMmb.setter
	def SysMmb(self, value):
		self._SysMmb = value if type(value) != base_types.auto else self.make_default("SysMmb")

	@SysMmb.deleter
	def SysMmb(self):
		del self._SysMmb
		self._SysMmb = None

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
	def TtlsPerStgOrdr(self):
		return self._TtlsPerStgOrdr

	@TtlsPerStgOrdr.setter
	def TtlsPerStgOrdr(self, value):
		self._TtlsPerStgOrdr = value if type(value) != base_types.auto else self.make_default("TtlsPerStgOrdr")

	@TtlsPerStgOrdr.deleter
	def TtlsPerStgOrdr(self):
		del self._TtlsPerStgOrdr
		self._TtlsPerStgOrdr = None

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if type(value) != base_types.auto else self.make_default("VldtyPrd")

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = None

	@property
	def ZeroSweepInd(self):
		return self._ZeroSweepInd

	@ZeroSweepInd.setter
	def ZeroSweepInd(self, value):
		self._ZeroSweepInd = value if type(value) != base_types.auto else self.make_default("ZeroSweepInd")

	@ZeroSweepInd.deleter
	def ZeroSweepInd(self):
		del self._ZeroSweepInd
		self._ZeroSweepInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdPoolAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnTp', type=ExecutionType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetOrdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetOrdrSeq', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPty', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysMmb', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=StandingOrderType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlsPerStgOrdr', type=StandingOrderTotalAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=DatePeriod3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ZeroSweepInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))