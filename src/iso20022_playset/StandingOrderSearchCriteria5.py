import base_types
import ActiveCurrencyCode
import AccountIdentification4Choice
import StandingOrderType1Choice
import CashAccount40
import Number
import Max35Text
import TrueFalseIndicator
import BranchAndFinancialInstitutionIdentification8
import DatePeriod2Choice

class StandingOrderSearchCriteria5(base_types._BaseFieldType):

	__slots__ = ["_SysMmb", "_VldtyPrd", "_Acct", "_ZeroSweepInd", "_StgOrdrId", "_Ccy", "_Tp", "_RspnsblPty", "_LkSetId", "_LkSetOrdrSeq", "_LkSetOrdrId", "_KeyAttrbtsInd", "_AssoctdPoolAcct"]
	@property
	def SysMmb(self):
		return self._SysMmb

	@SysMmb.setter
	def SysMmb(self, value):
		self._SysMmb = value if type(value) != auto else self.make_default("SysMmb")

	@SysMmb.deleter
	def SysMmb(self):
		del self._SysMmb
		self._SysMmb = None

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if type(value) != auto else self.make_default("VldtyPrd")

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def ZeroSweepInd(self):
		return self._ZeroSweepInd

	@ZeroSweepInd.setter
	def ZeroSweepInd(self, value):
		self._ZeroSweepInd = value if type(value) != auto else self.make_default("ZeroSweepInd")

	@ZeroSweepInd.deleter
	def ZeroSweepInd(self):
		del self._ZeroSweepInd
		self._ZeroSweepInd = None

	@property
	def StgOrdrId(self):
		return self._StgOrdrId

	@StgOrdrId.setter
	def StgOrdrId(self, value):
		self._StgOrdrId = value if type(value) != auto else self.make_default("StgOrdrId")

	@StgOrdrId.deleter
	def StgOrdrId(self):
		del self._StgOrdrId
		self._StgOrdrId = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def RspnsblPty(self):
		return self._RspnsblPty

	@RspnsblPty.setter
	def RspnsblPty(self, value):
		self._RspnsblPty = value if type(value) != auto else self.make_default("RspnsblPty")

	@RspnsblPty.deleter
	def RspnsblPty(self):
		del self._RspnsblPty
		self._RspnsblPty = None

	@property
	def LkSetId(self):
		return self._LkSetId

	@LkSetId.setter
	def LkSetId(self, value):
		self._LkSetId = value if type(value) != auto else self.make_default("LkSetId")

	@LkSetId.deleter
	def LkSetId(self):
		del self._LkSetId
		self._LkSetId = None

	@property
	def LkSetOrdrSeq(self):
		return self._LkSetOrdrSeq

	@LkSetOrdrSeq.setter
	def LkSetOrdrSeq(self, value):
		self._LkSetOrdrSeq = value if type(value) != auto else self.make_default("LkSetOrdrSeq")

	@LkSetOrdrSeq.deleter
	def LkSetOrdrSeq(self):
		del self._LkSetOrdrSeq
		self._LkSetOrdrSeq = None

	@property
	def LkSetOrdrId(self):
		return self._LkSetOrdrId

	@LkSetOrdrId.setter
	def LkSetOrdrId(self, value):
		self._LkSetOrdrId = value if type(value) != auto else self.make_default("LkSetOrdrId")

	@LkSetOrdrId.deleter
	def LkSetOrdrId(self):
		del self._LkSetOrdrId
		self._LkSetOrdrId = None

	@property
	def KeyAttrbtsInd(self):
		return self._KeyAttrbtsInd

	@KeyAttrbtsInd.setter
	def KeyAttrbtsInd(self, value):
		self._KeyAttrbtsInd = value if type(value) != auto else self.make_default("KeyAttrbtsInd")

	@KeyAttrbtsInd.deleter
	def KeyAttrbtsInd(self):
		del self._KeyAttrbtsInd
		self._KeyAttrbtsInd = None

	@property
	def AssoctdPoolAcct(self):
		return self._AssoctdPoolAcct

	@AssoctdPoolAcct.setter
	def AssoctdPoolAcct(self, value):
		self._AssoctdPoolAcct = value if type(value) != auto else self.make_default("AssoctdPoolAcct")

	@AssoctdPoolAcct.deleter
	def AssoctdPoolAcct(self):
		del self._AssoctdPoolAcct
		self._AssoctdPoolAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SysMmb', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=DatePeriod2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ZeroSweepInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgOrdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=StandingOrderType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnsblPty', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetOrdrSeq', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkSetOrdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='KeyAttrbtsInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdPoolAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
	))

