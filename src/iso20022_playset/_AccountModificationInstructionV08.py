# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountParties18
from . import AccountSelection3Choice
from . import AdditionalReference13
from . import CashSettlement4
from . import Extension1
from . import InvestmentAccount75
from . import InvestmentAccountModification4
from . import MarketPracticeVersion1
from . import MessageIdentification1
from . import ModificationScope21
from . import ModificationScope40
from . import ModificationScope41
from . import ModificationScope43
from . import ModificationScope44
from . import ModificationScope45

class AccountModificationInstructionV08(base_types._BaseFieldType):

	__slots__ = ["_InstrDtls", "_InvstmtAcctSelctn", "_MktPrctcVrsn", "_ModfdAcctPties", "_ModfdAddtlInf", "_ModfdCshSttlm", "_ModfdIntrmies", "_ModfdInvstmtAcct", "_ModfdIsseAllcn", "_ModfdPlcmnt", "_ModfdSvcLvlAgrmt", "_ModfdSvgsInvstmtPlan", "_ModfdWdrwlInvstmtPlan", "_MsgId", "_PrvsRef", "_Xtnsn"]
	@property
	def InstrDtls(self):
		return self._InstrDtls

	@InstrDtls.setter
	def InstrDtls(self, value):
		self._InstrDtls = value if value is not None else base_types.UninitialisedField(self, 'InstrDtls', InvestmentAccountModification4, False)

	@InstrDtls.deleter
	def InstrDtls(self):
		del self._InstrDtls
		self._InstrDtls = base_types.UninitialisedField(self, 'InstrDtls', InvestmentAccountModification4, False)

	@property
	def InvstmtAcctSelctn(self):
		return self._InvstmtAcctSelctn

	@InvstmtAcctSelctn.setter
	def InvstmtAcctSelctn(self, value):
		self._InvstmtAcctSelctn = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctSelctn', AccountSelection3Choice, False)

	@InvstmtAcctSelctn.deleter
	def InvstmtAcctSelctn(self):
		del self._InvstmtAcctSelctn
		self._InvstmtAcctSelctn = base_types.UninitialisedField(self, 'InvstmtAcctSelctn', AccountSelection3Choice, False)

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
	def ModfdAcctPties(self):
		return self._ModfdAcctPties

	@ModfdAcctPties.setter
	def ModfdAcctPties(self, value):
		self._ModfdAcctPties = value if value is not None else base_types.UninitialisedField(self, 'ModfdAcctPties', AccountParties18, True)

	@ModfdAcctPties.deleter
	def ModfdAcctPties(self):
		del self._ModfdAcctPties
		self._ModfdAcctPties = base_types.UninitialisedField(self, 'ModfdAcctPties', AccountParties18, True)

	@property
	def ModfdAddtlInf(self):
		return self._ModfdAddtlInf

	@ModfdAddtlInf.setter
	def ModfdAddtlInf(self, value):
		self._ModfdAddtlInf = value if value is not None else base_types.UninitialisedField(self, 'ModfdAddtlInf', ModificationScope45, True)

	@ModfdAddtlInf.deleter
	def ModfdAddtlInf(self):
		del self._ModfdAddtlInf
		self._ModfdAddtlInf = base_types.UninitialisedField(self, 'ModfdAddtlInf', ModificationScope45, True)

	@property
	def ModfdCshSttlm(self):
		return self._ModfdCshSttlm

	@ModfdCshSttlm.setter
	def ModfdCshSttlm(self, value):
		self._ModfdCshSttlm = value if value is not None else base_types.UninitialisedField(self, 'ModfdCshSttlm', CashSettlement4, True)

	@ModfdCshSttlm.deleter
	def ModfdCshSttlm(self):
		del self._ModfdCshSttlm
		self._ModfdCshSttlm = base_types.UninitialisedField(self, 'ModfdCshSttlm', CashSettlement4, True)

	@property
	def ModfdIntrmies(self):
		return self._ModfdIntrmies

	@ModfdIntrmies.setter
	def ModfdIntrmies(self, value):
		self._ModfdIntrmies = value if value is not None else base_types.UninitialisedField(self, 'ModfdIntrmies', ModificationScope40, True)

	@ModfdIntrmies.deleter
	def ModfdIntrmies(self):
		del self._ModfdIntrmies
		self._ModfdIntrmies = base_types.UninitialisedField(self, 'ModfdIntrmies', ModificationScope40, True)

	@property
	def ModfdInvstmtAcct(self):
		return self._ModfdInvstmtAcct

	@ModfdInvstmtAcct.setter
	def ModfdInvstmtAcct(self, value):
		self._ModfdInvstmtAcct = value if value is not None else base_types.UninitialisedField(self, 'ModfdInvstmtAcct', InvestmentAccount75, False)

	@ModfdInvstmtAcct.deleter
	def ModfdInvstmtAcct(self):
		del self._ModfdInvstmtAcct
		self._ModfdInvstmtAcct = base_types.UninitialisedField(self, 'ModfdInvstmtAcct', InvestmentAccount75, False)

	@property
	def ModfdIsseAllcn(self):
		return self._ModfdIsseAllcn

	@ModfdIsseAllcn.setter
	def ModfdIsseAllcn(self, value):
		self._ModfdIsseAllcn = value if value is not None else base_types.UninitialisedField(self, 'ModfdIsseAllcn', ModificationScope21, False)

	@ModfdIsseAllcn.deleter
	def ModfdIsseAllcn(self):
		del self._ModfdIsseAllcn
		self._ModfdIsseAllcn = base_types.UninitialisedField(self, 'ModfdIsseAllcn', ModificationScope21, False)

	@property
	def ModfdPlcmnt(self):
		return self._ModfdPlcmnt

	@ModfdPlcmnt.setter
	def ModfdPlcmnt(self, value):
		self._ModfdPlcmnt = value if value is not None else base_types.UninitialisedField(self, 'ModfdPlcmnt', ModificationScope43, False)

	@ModfdPlcmnt.deleter
	def ModfdPlcmnt(self):
		del self._ModfdPlcmnt
		self._ModfdPlcmnt = base_types.UninitialisedField(self, 'ModfdPlcmnt', ModificationScope43, False)

	@property
	def ModfdSvcLvlAgrmt(self):
		return self._ModfdSvcLvlAgrmt

	@ModfdSvcLvlAgrmt.setter
	def ModfdSvcLvlAgrmt(self, value):
		self._ModfdSvcLvlAgrmt = value if value is not None else base_types.UninitialisedField(self, 'ModfdSvcLvlAgrmt', ModificationScope44, True)

	@ModfdSvcLvlAgrmt.deleter
	def ModfdSvcLvlAgrmt(self):
		del self._ModfdSvcLvlAgrmt
		self._ModfdSvcLvlAgrmt = base_types.UninitialisedField(self, 'ModfdSvcLvlAgrmt', ModificationScope44, True)

	@property
	def ModfdSvgsInvstmtPlan(self):
		return self._ModfdSvgsInvstmtPlan

	@ModfdSvgsInvstmtPlan.setter
	def ModfdSvgsInvstmtPlan(self, value):
		self._ModfdSvgsInvstmtPlan = value if value is not None else base_types.UninitialisedField(self, 'ModfdSvgsInvstmtPlan', ModificationScope41, True)

	@ModfdSvgsInvstmtPlan.deleter
	def ModfdSvgsInvstmtPlan(self):
		del self._ModfdSvgsInvstmtPlan
		self._ModfdSvgsInvstmtPlan = base_types.UninitialisedField(self, 'ModfdSvgsInvstmtPlan', ModificationScope41, True)

	@property
	def ModfdWdrwlInvstmtPlan(self):
		return self._ModfdWdrwlInvstmtPlan

	@ModfdWdrwlInvstmtPlan.setter
	def ModfdWdrwlInvstmtPlan(self, value):
		self._ModfdWdrwlInvstmtPlan = value if value is not None else base_types.UninitialisedField(self, 'ModfdWdrwlInvstmtPlan', ModificationScope41, True)

	@ModfdWdrwlInvstmtPlan.deleter
	def ModfdWdrwlInvstmtPlan(self):
		del self._ModfdWdrwlInvstmtPlan
		self._ModfdWdrwlInvstmtPlan = base_types.UninitialisedField(self, 'ModfdWdrwlInvstmtPlan', ModificationScope41, True)

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
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if value is not None else base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference13, False)

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference13, False)

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
		base_types.FieldEntry(name='InstrDtls', type=InvestmentAccountModification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctSelctn', type=AccountSelection3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktPrctcVrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdAcctPties', type=AccountParties18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdAddtlInf', type=ModificationScope45, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdCshSttlm', type=CashSettlement4, min=0, max=8, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdIntrmies', type=ModificationScope40, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdInvstmtAcct', type=InvestmentAccount75, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdIsseAllcn', type=ModificationScope21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdPlcmnt', type=ModificationScope43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdSvcLvlAgrmt', type=ModificationScope44, min=0, max=30, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdSvgsInvstmtPlan', type=ModificationScope41, min=0, max=50, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdWdrwlInvstmtPlan', type=ModificationScope41, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))