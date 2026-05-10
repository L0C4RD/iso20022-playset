from . import base_types
from .Max35Text import Max35Text
from .CorporateActionEventType2FormatChoice import CorporateActionEventType2FormatChoice
from .PartyIdentification2Choice import PartyIdentification2Choice
from .StandingInstructionType1Code import StandingInstructionType1Code
from .IncludedAccount1 import IncludedAccount1
from .FinancialInstrumentDescription3 import FinancialInstrumentDescription3

class CorporateActionStandingInstructionGeneralInformation1(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_ClntStgInstrId", "_EvtTp", "_UndrlygScty", "_InstgPtyId", "_StgInstrTp"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != base_types.auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def ClntStgInstrId(self):
		return self._ClntStgInstrId

	@ClntStgInstrId.setter
	def ClntStgInstrId(self, value):
		self._ClntStgInstrId = value if type(value) != base_types.auto else self.make_default("ClntStgInstrId")

	@ClntStgInstrId.deleter
	def ClntStgInstrId(self):
		del self._ClntStgInstrId
		self._ClntStgInstrId = None

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if type(value) != base_types.auto else self.make_default("EvtTp")

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = None

	@property
	def UndrlygScty(self):
		return self._UndrlygScty

	@UndrlygScty.setter
	def UndrlygScty(self, value):
		self._UndrlygScty = value if type(value) != base_types.auto else self.make_default("UndrlygScty")

	@UndrlygScty.deleter
	def UndrlygScty(self):
		del self._UndrlygScty
		self._UndrlygScty = None

	@property
	def InstgPtyId(self):
		return self._InstgPtyId

	@InstgPtyId.setter
	def InstgPtyId(self, value):
		self._InstgPtyId = value if type(value) != base_types.auto else self.make_default("InstgPtyId")

	@InstgPtyId.deleter
	def InstgPtyId(self):
		del self._InstgPtyId
		self._InstgPtyId = None

	@property
	def StgInstrTp(self):
		return self._StgInstrTp

	@StgInstrTp.setter
	def StgInstrTp(self, value):
		self._StgInstrTp = value if type(value) != base_types.auto else self.make_default("StgInstrTp")

	@StgInstrTp.deleter
	def StgInstrTp(self):
		del self._StgInstrTp
		self._StgInstrTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=IncludedAccount1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClntStgInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType2FormatChoice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UndrlygScty', type=FinancialInstrumentDescription3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgPtyId', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstrTp', type=StandingInstructionType1Code, min=1, max=1, mutex_group=None, array=False),
	))

