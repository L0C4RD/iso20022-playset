# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountManagementConfirmation5
from . import AccountParties17
from . import AdditionalReference13
from . import AdditiononalInformation13
from . import CashSettlement3
from . import DocumentToSend4
from . import Extension1
from . import Intermediary46
from . import InvestmentAccount74
from . import InvestmentFundOrder4
from . import InvestmentPlan17
from . import MarketPracticeVersion1
from . import MessageIdentification1
from . import NewIssueAllocation2
from . import ReferredAgent3

class AccountDetailsConfirmationV08(base_types._BaseFieldType):

	__slots__ = ["_AcctPties", "_AddtlInf", "_ConfDtls", "_CshSttlm", "_Intrmies", "_InvstmtAcct", "_MktPrctcVrsn", "_MsgId", "_NewIsseAllcn", "_OrdrRef", "_Plcmnt", "_RltdRef", "_SvcLvlAgrmt", "_SvgsInvstmtPlan", "_WdrwlInvstmtPlan", "_Xtnsn"]
	@property
	def AcctPties(self):
		return self._AcctPties

	@AcctPties.setter
	def AcctPties(self, value):
		self._AcctPties = value if value is not None else base_types.UninitialisedField(self, 'AcctPties', AccountParties17, False)

	@AcctPties.deleter
	def AcctPties(self):
		del self._AcctPties
		self._AcctPties = base_types.UninitialisedField(self, 'AcctPties', AccountParties17, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditiononalInformation13, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditiononalInformation13, True)

	@property
	def ConfDtls(self):
		return self._ConfDtls

	@ConfDtls.setter
	def ConfDtls(self, value):
		self._ConfDtls = value if value is not None else base_types.UninitialisedField(self, 'ConfDtls', AccountManagementConfirmation5, False)

	@ConfDtls.deleter
	def ConfDtls(self):
		del self._ConfDtls
		self._ConfDtls = base_types.UninitialisedField(self, 'ConfDtls', AccountManagementConfirmation5, False)

	@property
	def CshSttlm(self):
		return self._CshSttlm

	@CshSttlm.setter
	def CshSttlm(self, value):
		self._CshSttlm = value if value is not None else base_types.UninitialisedField(self, 'CshSttlm', CashSettlement3, True)

	@CshSttlm.deleter
	def CshSttlm(self):
		del self._CshSttlm
		self._CshSttlm = base_types.UninitialisedField(self, 'CshSttlm', CashSettlement3, True)

	@property
	def Intrmies(self):
		return self._Intrmies

	@Intrmies.setter
	def Intrmies(self, value):
		self._Intrmies = value if value is not None else base_types.UninitialisedField(self, 'Intrmies', Intermediary46, True)

	@Intrmies.deleter
	def Intrmies(self):
		del self._Intrmies
		self._Intrmies = base_types.UninitialisedField(self, 'Intrmies', Intermediary46, True)

	@property
	def InvstmtAcct(self):
		return self._InvstmtAcct

	@InvstmtAcct.setter
	def InvstmtAcct(self, value):
		self._InvstmtAcct = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcct', InvestmentAccount74, False)

	@InvstmtAcct.deleter
	def InvstmtAcct(self):
		del self._InvstmtAcct
		self._InvstmtAcct = base_types.UninitialisedField(self, 'InvstmtAcct', InvestmentAccount74, False)

	@property
	def MktPrctcVrsn(self):
		return self._MktPrctcVrsn

	@MktPrctcVrsn.setter
	def MktPrctcVrsn(self, value):
		self._MktPrctcVrsn = value if value is not None else base_types.UninitialisedField(self, 'MktPrctcVrsn', MarketPracticeVersion1, False)

	@MktPrctcVrsn.deleter
	def MktPrctcVrsn(self):
		del self._MktPrctcVrsn
		self._MktPrctcVrsn = base_types.UninitialisedField(self, 'MktPrctcVrsn', MarketPracticeVersion1, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def NewIsseAllcn(self):
		return self._NewIsseAllcn

	@NewIsseAllcn.setter
	def NewIsseAllcn(self, value):
		self._NewIsseAllcn = value if value is not None else base_types.UninitialisedField(self, 'NewIsseAllcn', NewIssueAllocation2, False)

	@NewIsseAllcn.deleter
	def NewIsseAllcn(self):
		del self._NewIsseAllcn
		self._NewIsseAllcn = base_types.UninitialisedField(self, 'NewIsseAllcn', NewIssueAllocation2, False)

	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if value is not None else base_types.UninitialisedField(self, 'OrdrRef', InvestmentFundOrder4, False)

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = base_types.UninitialisedField(self, 'OrdrRef', InvestmentFundOrder4, False)

	@property
	def Plcmnt(self):
		return self._Plcmnt

	@Plcmnt.setter
	def Plcmnt(self, value):
		self._Plcmnt = value if value is not None else base_types.UninitialisedField(self, 'Plcmnt', ReferredAgent3, False)

	@Plcmnt.deleter
	def Plcmnt(self):
		del self._Plcmnt
		self._Plcmnt = base_types.UninitialisedField(self, 'Plcmnt', ReferredAgent3, False)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', AdditionalReference13, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', AdditionalReference13, False)

	@property
	def SvcLvlAgrmt(self):
		return self._SvcLvlAgrmt

	@SvcLvlAgrmt.setter
	def SvcLvlAgrmt(self, value):
		self._SvcLvlAgrmt = value if value is not None else base_types.UninitialisedField(self, 'SvcLvlAgrmt', DocumentToSend4, True)

	@SvcLvlAgrmt.deleter
	def SvcLvlAgrmt(self):
		del self._SvcLvlAgrmt
		self._SvcLvlAgrmt = base_types.UninitialisedField(self, 'SvcLvlAgrmt', DocumentToSend4, True)

	@property
	def SvgsInvstmtPlan(self):
		return self._SvgsInvstmtPlan

	@SvgsInvstmtPlan.setter
	def SvgsInvstmtPlan(self, value):
		self._SvgsInvstmtPlan = value if value is not None else base_types.UninitialisedField(self, 'SvgsInvstmtPlan', InvestmentPlan17, True)

	@SvgsInvstmtPlan.deleter
	def SvgsInvstmtPlan(self):
		del self._SvgsInvstmtPlan
		self._SvgsInvstmtPlan = base_types.UninitialisedField(self, 'SvgsInvstmtPlan', InvestmentPlan17, True)

	@property
	def WdrwlInvstmtPlan(self):
		return self._WdrwlInvstmtPlan

	@WdrwlInvstmtPlan.setter
	def WdrwlInvstmtPlan(self, value):
		self._WdrwlInvstmtPlan = value if value is not None else base_types.UninitialisedField(self, 'WdrwlInvstmtPlan', InvestmentPlan17, True)

	@WdrwlInvstmtPlan.deleter
	def WdrwlInvstmtPlan(self):
		del self._WdrwlInvstmtPlan
		self._WdrwlInvstmtPlan = base_types.UninitialisedField(self, 'WdrwlInvstmtPlan', InvestmentPlan17, True)

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if value is not None else base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = base_types.UninitialisedField(self, 'Xtnsn', Extension1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctPties', type=AccountParties17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditiononalInformation13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ConfDtls', type=AccountManagementConfirmation5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlm', type=CashSettlement3, min=0, max=8, mutex_group=None, array=True),
		base_types.FieldEntry(name='Intrmies', type=Intermediary46, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtAcct', type=InvestmentAccount74, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktPrctcVrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewIsseAllcn', type=NewIssueAllocation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=InvestmentFundOrder4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Plcmnt', type=ReferredAgent3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcLvlAgrmt', type=DocumentToSend4, min=0, max=30, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvgsInvstmtPlan', type=InvestmentPlan17, min=0, max=50, mutex_group=None, array=True),
		base_types.FieldEntry(name='WdrwlInvstmtPlan', type=InvestmentPlan17, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))