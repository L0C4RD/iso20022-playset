# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import ActiveCurrencyCode
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import DatePeriod2Choice
from . import Max35Text
from . import Number
from . import StandingOrderType1Choice
from . import TrueFalseIndicator

class StandingOrderSearchCriteria5(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AssoctdPoolAcct", "_Ccy", "_KeyAttrbtsInd", "_LkSetId", "_LkSetOrdrId", "_LkSetOrdrSeq", "_RspnsblPty", "_StgOrdrId", "_SysMmb", "_Tp", "_VldtyPrd", "_ZeroSweepInd"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if value is not None else base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = base_types.UninitialisedField(self, 'Acct', CashAccount40, False)

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
	def KeyAttrbtsInd(self):
		return self._KeyAttrbtsInd

	@KeyAttrbtsInd.setter
	def KeyAttrbtsInd(self, value):
		self._KeyAttrbtsInd = value if value is not None else base_types.UninitialisedField(self, 'KeyAttrbtsInd', TrueFalseIndicator, False)

	@KeyAttrbtsInd.deleter
	def KeyAttrbtsInd(self):
		del self._KeyAttrbtsInd
		self._KeyAttrbtsInd = base_types.UninitialisedField(self, 'KeyAttrbtsInd', TrueFalseIndicator, False)

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
	def StgOrdrId(self):
		return self._StgOrdrId

	@StgOrdrId.setter
	def StgOrdrId(self, value):
		self._StgOrdrId = value if value is not None else base_types.UninitialisedField(self, 'StgOrdrId', Max35Text, False)

	@StgOrdrId.deleter
	def StgOrdrId(self):
		del self._StgOrdrId
		self._StgOrdrId = base_types.UninitialisedField(self, 'StgOrdrId', Max35Text, False)

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
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if value is not None else base_types.UninitialisedField(self, 'VldtyPrd', DatePeriod2Choice, False)

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = base_types.UninitialisedField(self, 'VldtyPrd', DatePeriod2Choice, False)

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
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdPoolAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyAttrbtsInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetOrdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetOrdrSeq', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPty', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysMmb', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=StandingOrderType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=DatePeriod2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ZeroSweepInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))