# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import ActiveCurrencyCode
from . import Amount2Choice
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import CreditDebitCode
from . import DatePeriod3
from . import ExecutionType1Choice
from . import Frequency2Code
from . import Max35Text
from . import Number
from . import StandingOrderTotalAmount1
from . import StandingOrderType1Choice
from . import TrueFalseIndicator

class StandingOrder11(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AssoctdPoolAcct", "_Ccy", "_CdtDbtInd", "_Cdtr", "_CdtrAcct", "_Dbtr", "_DbtrAcct", "_ExctnTp", "_Frqcy", "_LkSetId", "_LkSetOrdrId", "_LkSetOrdrSeq", "_Ref", "_RspnsblPty", "_SysMmb", "_Tp", "_TtlsPerStgOrdr", "_VldtyPrd", "_ZeroSweepInd"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', Amount2Choice, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', Amount2Choice, False)

	@property
	def AssoctdPoolAcct(self):
		return self._AssoctdPoolAcct

	@AssoctdPoolAcct.setter
	def AssoctdPoolAcct(self, value):
		self._AssoctdPoolAcct = value if value is not None else base_types.UninitialisedField(self, 'AssoctdPoolAcct', AccountIdentification4Choice, False)

	@AssoctdPoolAcct.deleter
	def AssoctdPoolAcct(self):
		del self._AssoctdPoolAcct
		self._AssoctdPoolAcct = base_types.UninitialisedField(self, 'AssoctdPoolAcct', AccountIdentification4Choice, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

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
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', BranchAndFinancialInstitutionIdentification8, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', BranchAndFinancialInstitutionIdentification8, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@property
	def ExctnTp(self):
		return self._ExctnTp

	@ExctnTp.setter
	def ExctnTp(self, value):
		self._ExctnTp = value if value is not None else base_types.UninitialisedField(self, 'ExctnTp', ExecutionType1Choice, False)

	@ExctnTp.deleter
	def ExctnTp(self):
		del self._ExctnTp
		self._ExctnTp = base_types.UninitialisedField(self, 'ExctnTp', ExecutionType1Choice, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency2Code, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency2Code, False)

	@property
	def LkSetId(self):
		return self._LkSetId

	@LkSetId.setter
	def LkSetId(self, value):
		self._LkSetId = value if value is not None else base_types.UninitialisedField(self, 'LkSetId', Max35Text, False)

	@LkSetId.deleter
	def LkSetId(self):
		del self._LkSetId
		self._LkSetId = base_types.UninitialisedField(self, 'LkSetId', Max35Text, False)

	@property
	def LkSetOrdrId(self):
		return self._LkSetOrdrId

	@LkSetOrdrId.setter
	def LkSetOrdrId(self, value):
		self._LkSetOrdrId = value if value is not None else base_types.UninitialisedField(self, 'LkSetOrdrId', Max35Text, False)

	@LkSetOrdrId.deleter
	def LkSetOrdrId(self):
		del self._LkSetOrdrId
		self._LkSetOrdrId = base_types.UninitialisedField(self, 'LkSetOrdrId', Max35Text, False)

	@property
	def LkSetOrdrSeq(self):
		return self._LkSetOrdrSeq

	@LkSetOrdrSeq.setter
	def LkSetOrdrSeq(self, value):
		self._LkSetOrdrSeq = value if value is not None else base_types.UninitialisedField(self, 'LkSetOrdrSeq', Number, False)

	@LkSetOrdrSeq.deleter
	def LkSetOrdrSeq(self):
		del self._LkSetOrdrSeq
		self._LkSetOrdrSeq = base_types.UninitialisedField(self, 'LkSetOrdrSeq', Number, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@property
	def RspnsblPty(self):
		return self._RspnsblPty

	@RspnsblPty.setter
	def RspnsblPty(self, value):
		self._RspnsblPty = value if value is not None else base_types.UninitialisedField(self, 'RspnsblPty', BranchAndFinancialInstitutionIdentification8, False)

	@RspnsblPty.deleter
	def RspnsblPty(self):
		del self._RspnsblPty
		self._RspnsblPty = base_types.UninitialisedField(self, 'RspnsblPty', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def SysMmb(self):
		return self._SysMmb

	@SysMmb.setter
	def SysMmb(self, value):
		self._SysMmb = value if value is not None else base_types.UninitialisedField(self, 'SysMmb', BranchAndFinancialInstitutionIdentification8, False)

	@SysMmb.deleter
	def SysMmb(self):
		del self._SysMmb
		self._SysMmb = base_types.UninitialisedField(self, 'SysMmb', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', StandingOrderType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', StandingOrderType1Choice, False)

	@property
	def TtlsPerStgOrdr(self):
		return self._TtlsPerStgOrdr

	@TtlsPerStgOrdr.setter
	def TtlsPerStgOrdr(self, value):
		self._TtlsPerStgOrdr = value if value is not None else base_types.UninitialisedField(self, 'TtlsPerStgOrdr', StandingOrderTotalAmount1, False)

	@TtlsPerStgOrdr.deleter
	def TtlsPerStgOrdr(self):
		del self._TtlsPerStgOrdr
		self._TtlsPerStgOrdr = base_types.UninitialisedField(self, 'TtlsPerStgOrdr', StandingOrderTotalAmount1, False)

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if value is not None else base_types.UninitialisedField(self, 'VldtyPrd', DatePeriod3, False)

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = base_types.UninitialisedField(self, 'VldtyPrd', DatePeriod3, False)

	@property
	def ZeroSweepInd(self):
		return self._ZeroSweepInd

	@ZeroSweepInd.setter
	def ZeroSweepInd(self, value):
		self._ZeroSweepInd = value if value is not None else base_types.UninitialisedField(self, 'ZeroSweepInd', TrueFalseIndicator, False)

	@ZeroSweepInd.deleter
	def ZeroSweepInd(self):
		del self._ZeroSweepInd
		self._ZeroSweepInd = base_types.UninitialisedField(self, 'ZeroSweepInd', TrueFalseIndicator, False)

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