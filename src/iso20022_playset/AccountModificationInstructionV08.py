import base_types
import AccountParties18
import ModificationScope43
import ModificationScope21
import ModificationScope45
import ModificationScope40
import Extension1
import MarketPracticeVersion1
import ModificationScope44
import MessageIdentification1
import InvestmentAccount75
import AdditionalReference13
import InvestmentAccountModification4
import CashSettlement4
import AccountSelection3Choice
import ModificationScope41

class AccountModificationInstructionV08(base_types._BaseFieldType):

	__slots__ = ["_ModfdAcctPties", "_ModfdSvcLvlAgrmt", "_ModfdPlcmnt", "_ModfdAddtlInf", "_InstrDtls", "_MktPrctcVrsn", "_MsgId", "_InvstmtAcctSelctn", "_ModfdInvstmtAcct", "_ModfdIsseAllcn", "_ModfdIntrmies", "_ModfdCshSttlm", "_PrvsRef", "_ModfdWdrwlInvstmtPlan", "_Xtnsn", "_ModfdSvgsInvstmtPlan"]
	@property
	def ModfdAcctPties(self):
		return self._ModfdAcctPties

	@ModfdAcctPties.setter
	def ModfdAcctPties(self, value):
		self._ModfdAcctPties = value if type(value) != auto else self.make_default("ModfdAcctPties")

	@ModfdAcctPties.deleter
	def ModfdAcctPties(self):
		del self._ModfdAcctPties
		self._ModfdAcctPties = None

	@property
	def ModfdSvcLvlAgrmt(self):
		return self._ModfdSvcLvlAgrmt

	@ModfdSvcLvlAgrmt.setter
	def ModfdSvcLvlAgrmt(self, value):
		self._ModfdSvcLvlAgrmt = value if type(value) != auto else self.make_default("ModfdSvcLvlAgrmt")

	@ModfdSvcLvlAgrmt.deleter
	def ModfdSvcLvlAgrmt(self):
		del self._ModfdSvcLvlAgrmt
		self._ModfdSvcLvlAgrmt = None

	@property
	def ModfdPlcmnt(self):
		return self._ModfdPlcmnt

	@ModfdPlcmnt.setter
	def ModfdPlcmnt(self, value):
		self._ModfdPlcmnt = value if type(value) != auto else self.make_default("ModfdPlcmnt")

	@ModfdPlcmnt.deleter
	def ModfdPlcmnt(self):
		del self._ModfdPlcmnt
		self._ModfdPlcmnt = None

	@property
	def ModfdAddtlInf(self):
		return self._ModfdAddtlInf

	@ModfdAddtlInf.setter
	def ModfdAddtlInf(self, value):
		self._ModfdAddtlInf = value if type(value) != auto else self.make_default("ModfdAddtlInf")

	@ModfdAddtlInf.deleter
	def ModfdAddtlInf(self):
		del self._ModfdAddtlInf
		self._ModfdAddtlInf = None

	@property
	def InstrDtls(self):
		return self._InstrDtls

	@InstrDtls.setter
	def InstrDtls(self, value):
		self._InstrDtls = value if type(value) != auto else self.make_default("InstrDtls")

	@InstrDtls.deleter
	def InstrDtls(self):
		del self._InstrDtls
		self._InstrDtls = None

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
	def InvstmtAcctSelctn(self):
		return self._InvstmtAcctSelctn

	@InvstmtAcctSelctn.setter
	def InvstmtAcctSelctn(self, value):
		self._InvstmtAcctSelctn = value if type(value) != auto else self.make_default("InvstmtAcctSelctn")

	@InvstmtAcctSelctn.deleter
	def InvstmtAcctSelctn(self):
		del self._InvstmtAcctSelctn
		self._InvstmtAcctSelctn = None

	@property
	def ModfdInvstmtAcct(self):
		return self._ModfdInvstmtAcct

	@ModfdInvstmtAcct.setter
	def ModfdInvstmtAcct(self, value):
		self._ModfdInvstmtAcct = value if type(value) != auto else self.make_default("ModfdInvstmtAcct")

	@ModfdInvstmtAcct.deleter
	def ModfdInvstmtAcct(self):
		del self._ModfdInvstmtAcct
		self._ModfdInvstmtAcct = None

	@property
	def ModfdIsseAllcn(self):
		return self._ModfdIsseAllcn

	@ModfdIsseAllcn.setter
	def ModfdIsseAllcn(self, value):
		self._ModfdIsseAllcn = value if type(value) != auto else self.make_default("ModfdIsseAllcn")

	@ModfdIsseAllcn.deleter
	def ModfdIsseAllcn(self):
		del self._ModfdIsseAllcn
		self._ModfdIsseAllcn = None

	@property
	def ModfdIntrmies(self):
		return self._ModfdIntrmies

	@ModfdIntrmies.setter
	def ModfdIntrmies(self, value):
		self._ModfdIntrmies = value if type(value) != auto else self.make_default("ModfdIntrmies")

	@ModfdIntrmies.deleter
	def ModfdIntrmies(self):
		del self._ModfdIntrmies
		self._ModfdIntrmies = None

	@property
	def ModfdCshSttlm(self):
		return self._ModfdCshSttlm

	@ModfdCshSttlm.setter
	def ModfdCshSttlm(self, value):
		self._ModfdCshSttlm = value if type(value) != auto else self.make_default("ModfdCshSttlm")

	@ModfdCshSttlm.deleter
	def ModfdCshSttlm(self):
		del self._ModfdCshSttlm
		self._ModfdCshSttlm = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def ModfdWdrwlInvstmtPlan(self):
		return self._ModfdWdrwlInvstmtPlan

	@ModfdWdrwlInvstmtPlan.setter
	def ModfdWdrwlInvstmtPlan(self, value):
		self._ModfdWdrwlInvstmtPlan = value if type(value) != auto else self.make_default("ModfdWdrwlInvstmtPlan")

	@ModfdWdrwlInvstmtPlan.deleter
	def ModfdWdrwlInvstmtPlan(self):
		del self._ModfdWdrwlInvstmtPlan
		self._ModfdWdrwlInvstmtPlan = None

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
	def ModfdSvgsInvstmtPlan(self):
		return self._ModfdSvgsInvstmtPlan

	@ModfdSvgsInvstmtPlan.setter
	def ModfdSvgsInvstmtPlan(self, value):
		self._ModfdSvgsInvstmtPlan = value if type(value) != auto else self.make_default("ModfdSvgsInvstmtPlan")

	@ModfdSvgsInvstmtPlan.deleter
	def ModfdSvgsInvstmtPlan(self):
		del self._ModfdSvgsInvstmtPlan
		self._ModfdSvgsInvstmtPlan = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModfdAcctPties', type=AccountParties18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdSvcLvlAgrmt', type=ModificationScope44, min=0, max=30, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdPlcmnt', type=ModificationScope43, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdAddtlInf', type=ModificationScope45, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrDtls', type=InvestmentAccountModification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktPrctcVrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctSelctn', type=AccountSelection3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdInvstmtAcct', type=InvestmentAccount75, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdIsseAllcn', type=ModificationScope21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdIntrmies', type=ModificationScope40, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdCshSttlm', type=CashSettlement4, min=0, max=8, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModfdWdrwlInvstmtPlan', type=ModificationScope41, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModfdSvgsInvstmtPlan', type=ModificationScope41, min=0, max=50, mutex_group=None, array=True),
	))

