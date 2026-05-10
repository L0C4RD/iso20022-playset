from . import base_types
from ._AdditionalReference10 import AdditionalReference10
from ._AdditionalReference11 import AdditionalReference11
from ._BusinessFlowDirectionType1Code import BusinessFlowDirectionType1Code
from ._Extension1 import Extension1
from ._IndividualPerson8 import IndividualPerson8
from ._InvestmentAccount69 import InvestmentAccount69
from ._MarketPracticeVersion1 import MarketPracticeVersion1
from ._MessageIdentification1 import MessageIdentification1
from ._Organisation36 import Organisation36
from ._PartyIdentification132 import PartyIdentification132
from ._PortfolioTransfer12 import PortfolioTransfer12

class AccountHoldingInformationRequestV08(base_types._BaseFieldType):

	__slots__ = ["_BizFlowDrctnTp", "_MktPrctcVrsn", "_MsgRef", "_NmneeAcct", "_OthrCorpInvstr", "_OthrIndvInvstr", "_PdctTrf", "_PmryCorpInvstr", "_PmryIndvInvstr", "_PoolRef", "_PrvsRef", "_RltdRef", "_ScndryCorpInvstr", "_ScndryIndvInvstr", "_Trfee", "_TrfrAcct", "_Xtnsn"]
	@property
	def BizFlowDrctnTp(self):
		return self._BizFlowDrctnTp

	@BizFlowDrctnTp.setter
	def BizFlowDrctnTp(self, value):
		self._BizFlowDrctnTp = value if type(value) != base_types.auto else self.make_default("BizFlowDrctnTp")

	@BizFlowDrctnTp.deleter
	def BizFlowDrctnTp(self):
		del self._BizFlowDrctnTp
		self._BizFlowDrctnTp = None

	@property
	def MktPrctcVrsn(self):
		return self._MktPrctcVrsn

	@MktPrctcVrsn.setter
	def MktPrctcVrsn(self, value):
		self._MktPrctcVrsn = value if type(value) != base_types.auto else self.make_default("MktPrctcVrsn")

	@MktPrctcVrsn.deleter
	def MktPrctcVrsn(self):
		del self._MktPrctcVrsn
		self._MktPrctcVrsn = None

	@property
	def MsgRef(self):
		return self._MsgRef

	@MsgRef.setter
	def MsgRef(self, value):
		self._MsgRef = value if type(value) != base_types.auto else self.make_default("MsgRef")

	@MsgRef.deleter
	def MsgRef(self):
		del self._MsgRef
		self._MsgRef = None

	@property
	def NmneeAcct(self):
		return self._NmneeAcct

	@NmneeAcct.setter
	def NmneeAcct(self, value):
		self._NmneeAcct = value if type(value) != base_types.auto else self.make_default("NmneeAcct")

	@NmneeAcct.deleter
	def NmneeAcct(self):
		del self._NmneeAcct
		self._NmneeAcct = None

	@property
	def OthrCorpInvstr(self):
		return self._OthrCorpInvstr

	@OthrCorpInvstr.setter
	def OthrCorpInvstr(self, value):
		self._OthrCorpInvstr = value if type(value) != base_types.auto else self.make_default("OthrCorpInvstr")

	@OthrCorpInvstr.deleter
	def OthrCorpInvstr(self):
		del self._OthrCorpInvstr
		self._OthrCorpInvstr = None

	@property
	def OthrIndvInvstr(self):
		return self._OthrIndvInvstr

	@OthrIndvInvstr.setter
	def OthrIndvInvstr(self, value):
		self._OthrIndvInvstr = value if type(value) != base_types.auto else self.make_default("OthrIndvInvstr")

	@OthrIndvInvstr.deleter
	def OthrIndvInvstr(self):
		del self._OthrIndvInvstr
		self._OthrIndvInvstr = None

	@property
	def PdctTrf(self):
		return self._PdctTrf

	@PdctTrf.setter
	def PdctTrf(self, value):
		self._PdctTrf = value if type(value) != base_types.auto else self.make_default("PdctTrf")

	@PdctTrf.deleter
	def PdctTrf(self):
		del self._PdctTrf
		self._PdctTrf = None

	@property
	def PmryCorpInvstr(self):
		return self._PmryCorpInvstr

	@PmryCorpInvstr.setter
	def PmryCorpInvstr(self, value):
		self._PmryCorpInvstr = value if type(value) != base_types.auto else self.make_default("PmryCorpInvstr")

	@PmryCorpInvstr.deleter
	def PmryCorpInvstr(self):
		del self._PmryCorpInvstr
		self._PmryCorpInvstr = None

	@property
	def PmryIndvInvstr(self):
		return self._PmryIndvInvstr

	@PmryIndvInvstr.setter
	def PmryIndvInvstr(self, value):
		self._PmryIndvInvstr = value if type(value) != base_types.auto else self.make_default("PmryIndvInvstr")

	@PmryIndvInvstr.deleter
	def PmryIndvInvstr(self):
		del self._PmryIndvInvstr
		self._PmryIndvInvstr = None

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if type(value) != base_types.auto else self.make_default("PoolRef")

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = None

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if type(value) != base_types.auto else self.make_default("PrvsRef")

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = None

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if type(value) != base_types.auto else self.make_default("RltdRef")

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = None

	@property
	def ScndryCorpInvstr(self):
		return self._ScndryCorpInvstr

	@ScndryCorpInvstr.setter
	def ScndryCorpInvstr(self, value):
		self._ScndryCorpInvstr = value if type(value) != base_types.auto else self.make_default("ScndryCorpInvstr")

	@ScndryCorpInvstr.deleter
	def ScndryCorpInvstr(self):
		del self._ScndryCorpInvstr
		self._ScndryCorpInvstr = None

	@property
	def ScndryIndvInvstr(self):
		return self._ScndryIndvInvstr

	@ScndryIndvInvstr.setter
	def ScndryIndvInvstr(self, value):
		self._ScndryIndvInvstr = value if type(value) != base_types.auto else self.make_default("ScndryIndvInvstr")

	@ScndryIndvInvstr.deleter
	def ScndryIndvInvstr(self):
		del self._ScndryIndvInvstr
		self._ScndryIndvInvstr = None

	@property
	def Trfee(self):
		return self._Trfee

	@Trfee.setter
	def Trfee(self, value):
		self._Trfee = value if type(value) != base_types.auto else self.make_default("Trfee")

	@Trfee.deleter
	def Trfee(self):
		del self._Trfee
		self._Trfee = None

	@property
	def TrfrAcct(self):
		return self._TrfrAcct

	@TrfrAcct.setter
	def TrfrAcct(self, value):
		self._TrfrAcct = value if type(value) != base_types.auto else self.make_default("TrfrAcct")

	@TrfrAcct.deleter
	def TrfrAcct(self):
		del self._TrfrAcct
		self._TrfrAcct = None

	@property
	def Xtnsn(self):
		return self._Xtnsn

	@Xtnsn.setter
	def Xtnsn(self, value):
		self._Xtnsn = value if type(value) != base_types.auto else self.make_default("Xtnsn")

	@Xtnsn.deleter
	def Xtnsn(self):
		del self._Xtnsn
		self._Xtnsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizFlowDrctnTp', type=BusinessFlowDirectionType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktPrctcVrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmneeAcct', type=InvestmentAccount69, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCorpInvstr', type=Organisation36, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrIndvInvstr', type=IndividualPerson8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctTrf', type=PortfolioTransfer12, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmryCorpInvstr', type=Organisation36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryIndvInvstr', type=IndividualPerson8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryCorpInvstr', type=Organisation36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryIndvInvstr', type=IndividualPerson8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trfee', type=PartyIdentification132, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfrAcct', type=InvestmentAccount69, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))

