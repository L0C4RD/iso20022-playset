from . import base_types
from .MessageIdentification1 import MessageIdentification1
from .CashSettlement3 import CashSettlement3
from .AccountParties17 import AccountParties17
from .AccountManagementConfirmation5 import AccountManagementConfirmation5
from .MarketPracticeVersion1 import MarketPracticeVersion1
from .DocumentToSend4 import DocumentToSend4
from .AdditionalReference13 import AdditionalReference13
from .NewIssueAllocation2 import NewIssueAllocation2
from .Intermediary46 import Intermediary46
from .Extension1 import Extension1
from .InvestmentFundOrder4 import InvestmentFundOrder4
from .InvestmentPlan17 import InvestmentPlan17
from .InvestmentAccount74 import InvestmentAccount74
from .AdditiononalInformation13 import AdditiononalInformation13
from .ReferredAgent3 import ReferredAgent3

class AccountDetailsConfirmationV08(base_types._BaseFieldType):

	__slots__ = ["_Plcmnt", "_Xtnsn", "_AddtlInf", "_OrdrRef", "_MsgId", "_AcctPties", "_SvgsInvstmtPlan", "_MktPrctcVrsn", "_InvstmtAcct", "_RltdRef", "_Intrmies", "_NewIsseAllcn", "_SvcLvlAgrmt", "_ConfDtls", "_CshSttlm", "_WdrwlInvstmtPlan"]
	@property
	def Plcmnt(self):
		return self._Plcmnt

	@Plcmnt.setter
	def Plcmnt(self, value):
		self._Plcmnt = value if type(value) != auto else self.make_default("Plcmnt")

	@Plcmnt.deleter
	def Plcmnt(self):
		del self._Plcmnt
		self._Plcmnt = None

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if type(value) != auto else self.make_default("OrdrRef")

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def AcctPties(self):
		return self._AcctPties

	@AcctPties.setter
	def AcctPties(self, value):
		self._AcctPties = value if type(value) != auto else self.make_default("AcctPties")

	@AcctPties.deleter
	def AcctPties(self):
		del self._AcctPties
		self._AcctPties = None

	@property
	def SvgsInvstmtPlan(self):
		return self._SvgsInvstmtPlan

	@SvgsInvstmtPlan.setter
	def SvgsInvstmtPlan(self, value):
		self._SvgsInvstmtPlan = value if type(value) != auto else self.make_default("SvgsInvstmtPlan")

	@SvgsInvstmtPlan.deleter
	def SvgsInvstmtPlan(self):
		del self._SvgsInvstmtPlan
		self._SvgsInvstmtPlan = None

	@property
	def MktPrctcVrsn(self):
		return self._MktPrctcVrsn

	@MktPrctcVrsn.setter
	def MktPrctcVrsn(self, value):
		self._MktPrctcVrsn = value if type(value) != auto else self.make_default("MktPrctcVrsn")

	@MktPrctcVrsn.deleter
	def MktPrctcVrsn(self):
		del self._MktPrctcVrsn
		self._MktPrctcVrsn = None

	@property
	def InvstmtAcct(self):
		return self._InvstmtAcct

	@InvstmtAcct.setter
	def InvstmtAcct(self, value):
		self._InvstmtAcct = value if type(value) != auto else self.make_default("InvstmtAcct")

	@InvstmtAcct.deleter
	def InvstmtAcct(self):
		del self._InvstmtAcct
		self._InvstmtAcct = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	@property
	def Intrmies(self):
		return self._Intrmies

	@Intrmies.setter
	def Intrmies(self, value):
		self._Intrmies = value if type(value) != auto else self.make_default("Intrmies")

	@Intrmies.deleter
	def Intrmies(self):
		del self._Intrmies
		self._Intrmies = None

	@property
	def NewIsseAllcn(self):
		return self._NewIsseAllcn

	@NewIsseAllcn.setter
	def NewIsseAllcn(self, value):
		self._NewIsseAllcn = value if type(value) != auto else self.make_default("NewIsseAllcn")

	@NewIsseAllcn.deleter
	def NewIsseAllcn(self):
		del self._NewIsseAllcn
		self._NewIsseAllcn = None

	@property
	def SvcLvlAgrmt(self):
		return self._SvcLvlAgrmt

	@SvcLvlAgrmt.setter
	def SvcLvlAgrmt(self, value):
		self._SvcLvlAgrmt = value if type(value) != auto else self.make_default("SvcLvlAgrmt")

	@SvcLvlAgrmt.deleter
	def SvcLvlAgrmt(self):
		del self._SvcLvlAgrmt
		self._SvcLvlAgrmt = None

	@property
	def ConfDtls(self):
		return self._ConfDtls

	@ConfDtls.setter
	def ConfDtls(self, value):
		self._ConfDtls = value if type(value) != auto else self.make_default("ConfDtls")

	@ConfDtls.deleter
	def ConfDtls(self):
		del self._ConfDtls
		self._ConfDtls = None

	@property
	def CshSttlm(self):
		return self._CshSttlm

	@CshSttlm.setter
	def CshSttlm(self, value):
		self._CshSttlm = value if type(value) != auto else self.make_default("CshSttlm")

	@CshSttlm.deleter
	def CshSttlm(self):
		del self._CshSttlm
		self._CshSttlm = None

	@property
	def WdrwlInvstmtPlan(self):
		return self._WdrwlInvstmtPlan

	@WdrwlInvstmtPlan.setter
	def WdrwlInvstmtPlan(self, value):
		self._WdrwlInvstmtPlan = value if type(value) != auto else self.make_default("WdrwlInvstmtPlan")

	@WdrwlInvstmtPlan.deleter
	def WdrwlInvstmtPlan(self):
		del self._WdrwlInvstmtPlan
		self._WdrwlInvstmtPlan = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Plcmnt', type=ReferredAgent3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=AdditiononalInformation13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrRef', type=InvestmentFundOrder4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctPties', type=AccountParties17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvgsInvstmtPlan', type=InvestmentPlan17, min=0, max=50, mutex_group=None, array=True),
		base_types.FieldEntry(name='MktPrctcVrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcct', type=InvestmentAccount74, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmies', type=Intermediary46, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NewIsseAllcn', type=NewIssueAllocation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcLvlAgrmt', type=DocumentToSend4, min=0, max=30, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfDtls', type=AccountManagementConfirmation5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlm', type=CashSettlement3, min=0, max=8, mutex_group=None, array=True),
		base_types.FieldEntry(name='WdrwlInvstmtPlan', type=InvestmentPlan17, min=0, max=10, mutex_group=None, array=True),
	))

