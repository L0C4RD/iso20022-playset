# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalReference10
from . import AdditionalReference11
from . import Extension1
from . import IndividualPerson8
from . import InvestmentAccount69
from . import MarketPracticeVersion1
from . import MessageIdentification1
from . import Organisation36
from . import PartyIdentification309
from . import PortfolioTransfer13

class PortfolioTransferCompletionV01(base_types._BaseFieldType):

	__slots__ = ["_MktPrctcVrsn", "_MsgRef", "_NmneeAcct", "_OthrCorpInvstr", "_OthrIndvInvstr", "_PdctTrf", "_PmryCorpInvstr", "_PmryIndvInvstr", "_PoolRef", "_PrvsRef", "_RegdHldr", "_RltdRef", "_ScndryCorpInvstr", "_ScndryIndvInvstr", "_Trfee", "_TrfrAcct", "_Xtnsn"]
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
	def MsgRef(self):
		return self._MsgRef

	@MsgRef.setter
	def MsgRef(self, value):
		self._MsgRef = value if value is not None else base_types.UninitialisedField(self, 'MsgRef', MessageIdentification1, False)

	@MsgRef.deleter
	def MsgRef(self):
		del self._MsgRef
		self._MsgRef = base_types.UninitialisedField(self, 'MsgRef', MessageIdentification1, False)

	@property
	def NmneeAcct(self):
		return self._NmneeAcct

	@NmneeAcct.setter
	def NmneeAcct(self, value):
		self._NmneeAcct = value if value is not None else base_types.UninitialisedField(self, 'NmneeAcct', InvestmentAccount69, False)

	@NmneeAcct.deleter
	def NmneeAcct(self):
		del self._NmneeAcct
		self._NmneeAcct = base_types.UninitialisedField(self, 'NmneeAcct', InvestmentAccount69, False)

	@property
	def OthrCorpInvstr(self):
		return self._OthrCorpInvstr

	@OthrCorpInvstr.setter
	def OthrCorpInvstr(self, value):
		self._OthrCorpInvstr = value if value is not None else base_types.UninitialisedField(self, 'OthrCorpInvstr', Organisation36, True)

	@OthrCorpInvstr.deleter
	def OthrCorpInvstr(self):
		del self._OthrCorpInvstr
		self._OthrCorpInvstr = base_types.UninitialisedField(self, 'OthrCorpInvstr', Organisation36, True)

	@property
	def OthrIndvInvstr(self):
		return self._OthrIndvInvstr

	@OthrIndvInvstr.setter
	def OthrIndvInvstr(self, value):
		self._OthrIndvInvstr = value if value is not None else base_types.UninitialisedField(self, 'OthrIndvInvstr', IndividualPerson8, True)

	@OthrIndvInvstr.deleter
	def OthrIndvInvstr(self):
		del self._OthrIndvInvstr
		self._OthrIndvInvstr = base_types.UninitialisedField(self, 'OthrIndvInvstr', IndividualPerson8, True)

	@property
	def PdctTrf(self):
		return self._PdctTrf

	@PdctTrf.setter
	def PdctTrf(self, value):
		self._PdctTrf = value if value is not None else base_types.UninitialisedField(self, 'PdctTrf', PortfolioTransfer13, True)

	@PdctTrf.deleter
	def PdctTrf(self):
		del self._PdctTrf
		self._PdctTrf = base_types.UninitialisedField(self, 'PdctTrf', PortfolioTransfer13, True)

	@property
	def PmryCorpInvstr(self):
		return self._PmryCorpInvstr

	@PmryCorpInvstr.setter
	def PmryCorpInvstr(self, value):
		self._PmryCorpInvstr = value if value is not None else base_types.UninitialisedField(self, 'PmryCorpInvstr', Organisation36, False)

	@PmryCorpInvstr.deleter
	def PmryCorpInvstr(self):
		del self._PmryCorpInvstr
		self._PmryCorpInvstr = base_types.UninitialisedField(self, 'PmryCorpInvstr', Organisation36, False)

	@property
	def PmryIndvInvstr(self):
		return self._PmryIndvInvstr

	@PmryIndvInvstr.setter
	def PmryIndvInvstr(self, value):
		self._PmryIndvInvstr = value if value is not None else base_types.UninitialisedField(self, 'PmryIndvInvstr', IndividualPerson8, False)

	@PmryIndvInvstr.deleter
	def PmryIndvInvstr(self):
		del self._PmryIndvInvstr
		self._PmryIndvInvstr = base_types.UninitialisedField(self, 'PmryIndvInvstr', IndividualPerson8, False)

	@property
	def PoolRef(self):
		return self._PoolRef

	@PoolRef.setter
	def PoolRef(self, value):
		self._PoolRef = value if value is not None else base_types.UninitialisedField(self, 'PoolRef', AdditionalReference11, False)

	@PoolRef.deleter
	def PoolRef(self):
		del self._PoolRef
		self._PoolRef = base_types.UninitialisedField(self, 'PoolRef', AdditionalReference11, False)

	@property
	def PrvsRef(self):
		return self._PrvsRef

	@PrvsRef.setter
	def PrvsRef(self, value):
		self._PrvsRef = value if value is not None else base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference10, False)

	@PrvsRef.deleter
	def PrvsRef(self):
		del self._PrvsRef
		self._PrvsRef = base_types.UninitialisedField(self, 'PrvsRef', AdditionalReference10, False)

	@property
	def RegdHldr(self):
		return self._RegdHldr

	@RegdHldr.setter
	def RegdHldr(self, value):
		self._RegdHldr = value if value is not None else base_types.UninitialisedField(self, 'RegdHldr', IndividualPerson8, False)

	@RegdHldr.deleter
	def RegdHldr(self):
		del self._RegdHldr
		self._RegdHldr = base_types.UninitialisedField(self, 'RegdHldr', IndividualPerson8, False)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', AdditionalReference10, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', AdditionalReference10, False)

	@property
	def ScndryCorpInvstr(self):
		return self._ScndryCorpInvstr

	@ScndryCorpInvstr.setter
	def ScndryCorpInvstr(self, value):
		self._ScndryCorpInvstr = value if value is not None else base_types.UninitialisedField(self, 'ScndryCorpInvstr', Organisation36, False)

	@ScndryCorpInvstr.deleter
	def ScndryCorpInvstr(self):
		del self._ScndryCorpInvstr
		self._ScndryCorpInvstr = base_types.UninitialisedField(self, 'ScndryCorpInvstr', Organisation36, False)

	@property
	def ScndryIndvInvstr(self):
		return self._ScndryIndvInvstr

	@ScndryIndvInvstr.setter
	def ScndryIndvInvstr(self, value):
		self._ScndryIndvInvstr = value if value is not None else base_types.UninitialisedField(self, 'ScndryIndvInvstr', IndividualPerson8, False)

	@ScndryIndvInvstr.deleter
	def ScndryIndvInvstr(self):
		del self._ScndryIndvInvstr
		self._ScndryIndvInvstr = base_types.UninitialisedField(self, 'ScndryIndvInvstr', IndividualPerson8, False)

	@property
	def Trfee(self):
		return self._Trfee

	@Trfee.setter
	def Trfee(self, value):
		self._Trfee = value if value is not None else base_types.UninitialisedField(self, 'Trfee', PartyIdentification309, False)

	@Trfee.deleter
	def Trfee(self):
		del self._Trfee
		self._Trfee = base_types.UninitialisedField(self, 'Trfee', PartyIdentification309, False)

	@property
	def TrfrAcct(self):
		return self._TrfrAcct

	@TrfrAcct.setter
	def TrfrAcct(self, value):
		self._TrfrAcct = value if value is not None else base_types.UninitialisedField(self, 'TrfrAcct', InvestmentAccount69, False)

	@TrfrAcct.deleter
	def TrfrAcct(self):
		del self._TrfrAcct
		self._TrfrAcct = base_types.UninitialisedField(self, 'TrfrAcct', InvestmentAccount69, False)

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
		base_types.FieldEntry(name='MktPrctcVrsn', type=MarketPracticeVersion1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmneeAcct', type=InvestmentAccount69, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCorpInvstr', type=Organisation36, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrIndvInvstr', type=IndividualPerson8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctTrf', type=PortfolioTransfer13, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmryCorpInvstr', type=Organisation36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryIndvInvstr', type=IndividualPerson8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolRef', type=AdditionalReference11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdHldr', type=IndividualPerson8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=AdditionalReference10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryCorpInvstr', type=Organisation36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryIndvInvstr', type=IndividualPerson8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trfee', type=PartyIdentification309, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfrAcct', type=InvestmentAccount69, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Xtnsn', type=Extension1, min=0, max=None, mutex_group=None, array=True),
	))