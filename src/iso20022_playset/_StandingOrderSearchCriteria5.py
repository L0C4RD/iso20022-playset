# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountIdentification4Choice import AccountIdentification4Choice
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._DatePeriod2Choice import DatePeriod2Choice
from ._Max35Text import Max35Text
from ._Number import Number
from ._StandingOrderType1Choice import StandingOrderType1Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class StandingOrderSearchCriteria5(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_AssoctdPoolAcct", "_Ccy", "_KeyAttrbtsInd", "_LkSetId", "_LkSetOrdrId", "_LkSetOrdrSeq", "_RspnsblPty", "_StgOrdrId", "_SysMmb", "_Tp", "_VldtyPrd", "_ZeroSweepInd"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

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
	def KeyAttrbtsInd(self):
		return self._KeyAttrbtsInd

	@KeyAttrbtsInd.setter
	def KeyAttrbtsInd(self, value):
		self._KeyAttrbtsInd = value if type(value) != base_types.auto else self.make_default("KeyAttrbtsInd")

	@KeyAttrbtsInd.deleter
	def KeyAttrbtsInd(self):
		del self._KeyAttrbtsInd
		self._KeyAttrbtsInd = None

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
	def StgOrdrId(self):
		return self._StgOrdrId

	@StgOrdrId.setter
	def StgOrdrId(self, value):
		self._StgOrdrId = value if type(value) != base_types.auto else self.make_default("StgOrdrId")

	@StgOrdrId.deleter
	def StgOrdrId(self):
		del self._StgOrdrId
		self._StgOrdrId = None

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