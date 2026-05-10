from . import base_types
from .AllocationSatus4Choice import AllocationSatus4Choice
from .SettlementConditionModificationStatus4Choice import SettlementConditionModificationStatus4Choice
from .CancellationProcessingStatus8Choice import CancellationProcessingStatus8Choice
from .ResponseStatus7Choice import ResponseStatus7Choice
from .MatchingStatus28Choice import MatchingStatus28Choice
from .RegistrationProcessingStatus4Choice import RegistrationProcessingStatus4Choice
from .AffirmationStatus9Choice import AffirmationStatus9Choice
from .InstructionProcessingStatus26Choice import InstructionProcessingStatus26Choice
from .SettlementStatus25Choice import SettlementStatus25Choice
from .RepoCallRequestStatus10Choice import RepoCallRequestStatus10Choice
from .ReplacementProcessingStatus9Choice import ReplacementProcessingStatus9Choice
from .CorporateActionEventStage4Choice import CorporateActionEventStage4Choice
from .CorporateActionEventProcessingStatus4Choice import CorporateActionEventProcessingStatus4Choice

class Status22Choice(base_types._BaseFieldType):

	__slots__ = ["_RplcmntPrcgSts", "_RspnSts", "_RegnPrcgSts", "_CorpActnEvtPrcgSts", "_SttlmSts", "_AllcnSts", "_RepoCallReqSts", "_InstrPrcgSts", "_SttlmCondModSts", "_CorpActnEvtStag", "_AffirmSts", "_CxlPrcgSts", "_IfrrdMtchgSts", "_MtchgSts"]
	@property
	def RplcmntPrcgSts(self):
		return self._RplcmntPrcgSts

	@RplcmntPrcgSts.setter
	def RplcmntPrcgSts(self, value):
		self._RplcmntPrcgSts = value if type(value) != base_types.auto else self.make_default("RplcmntPrcgSts")

	@RplcmntPrcgSts.deleter
	def RplcmntPrcgSts(self):
		del self._RplcmntPrcgSts
		self._RplcmntPrcgSts = None

	@property
	def RspnSts(self):
		return self._RspnSts

	@RspnSts.setter
	def RspnSts(self, value):
		self._RspnSts = value if type(value) != base_types.auto else self.make_default("RspnSts")

	@RspnSts.deleter
	def RspnSts(self):
		del self._RspnSts
		self._RspnSts = None

	@property
	def RegnPrcgSts(self):
		return self._RegnPrcgSts

	@RegnPrcgSts.setter
	def RegnPrcgSts(self, value):
		self._RegnPrcgSts = value if type(value) != base_types.auto else self.make_default("RegnPrcgSts")

	@RegnPrcgSts.deleter
	def RegnPrcgSts(self):
		del self._RegnPrcgSts
		self._RegnPrcgSts = None

	@property
	def CorpActnEvtPrcgSts(self):
		return self._CorpActnEvtPrcgSts

	@CorpActnEvtPrcgSts.setter
	def CorpActnEvtPrcgSts(self, value):
		self._CorpActnEvtPrcgSts = value if type(value) != base_types.auto else self.make_default("CorpActnEvtPrcgSts")

	@CorpActnEvtPrcgSts.deleter
	def CorpActnEvtPrcgSts(self):
		del self._CorpActnEvtPrcgSts
		self._CorpActnEvtPrcgSts = None

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if type(value) != base_types.auto else self.make_default("SttlmSts")

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = None

	@property
	def AllcnSts(self):
		return self._AllcnSts

	@AllcnSts.setter
	def AllcnSts(self, value):
		self._AllcnSts = value if type(value) != base_types.auto else self.make_default("AllcnSts")

	@AllcnSts.deleter
	def AllcnSts(self):
		del self._AllcnSts
		self._AllcnSts = None

	@property
	def RepoCallReqSts(self):
		return self._RepoCallReqSts

	@RepoCallReqSts.setter
	def RepoCallReqSts(self, value):
		self._RepoCallReqSts = value if type(value) != base_types.auto else self.make_default("RepoCallReqSts")

	@RepoCallReqSts.deleter
	def RepoCallReqSts(self):
		del self._RepoCallReqSts
		self._RepoCallReqSts = None

	@property
	def InstrPrcgSts(self):
		return self._InstrPrcgSts

	@InstrPrcgSts.setter
	def InstrPrcgSts(self, value):
		self._InstrPrcgSts = value if type(value) != base_types.auto else self.make_default("InstrPrcgSts")

	@InstrPrcgSts.deleter
	def InstrPrcgSts(self):
		del self._InstrPrcgSts
		self._InstrPrcgSts = None

	@property
	def SttlmCondModSts(self):
		return self._SttlmCondModSts

	@SttlmCondModSts.setter
	def SttlmCondModSts(self, value):
		self._SttlmCondModSts = value if type(value) != base_types.auto else self.make_default("SttlmCondModSts")

	@SttlmCondModSts.deleter
	def SttlmCondModSts(self):
		del self._SttlmCondModSts
		self._SttlmCondModSts = None

	@property
	def CorpActnEvtStag(self):
		return self._CorpActnEvtStag

	@CorpActnEvtStag.setter
	def CorpActnEvtStag(self, value):
		self._CorpActnEvtStag = value if type(value) != base_types.auto else self.make_default("CorpActnEvtStag")

	@CorpActnEvtStag.deleter
	def CorpActnEvtStag(self):
		del self._CorpActnEvtStag
		self._CorpActnEvtStag = None

	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if type(value) != base_types.auto else self.make_default("AffirmSts")

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = None

	@property
	def CxlPrcgSts(self):
		return self._CxlPrcgSts

	@CxlPrcgSts.setter
	def CxlPrcgSts(self, value):
		self._CxlPrcgSts = value if type(value) != base_types.auto else self.make_default("CxlPrcgSts")

	@CxlPrcgSts.deleter
	def CxlPrcgSts(self):
		del self._CxlPrcgSts
		self._CxlPrcgSts = None

	@property
	def IfrrdMtchgSts(self):
		return self._IfrrdMtchgSts

	@IfrrdMtchgSts.setter
	def IfrrdMtchgSts(self, value):
		self._IfrrdMtchgSts = value if type(value) != base_types.auto else self.make_default("IfrrdMtchgSts")

	@IfrrdMtchgSts.deleter
	def IfrrdMtchgSts(self):
		del self._IfrrdMtchgSts
		self._IfrrdMtchgSts = None

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if type(value) != base_types.auto else self.make_default("MtchgSts")

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RplcmntPrcgSts', type=ReplacementProcessingStatus9Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RspnSts', type=ResponseStatus7Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RegnPrcgSts', type=RegistrationProcessingStatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnEvtPrcgSts', type=CorporateActionEventProcessingStatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus25Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AllcnSts', type=AllocationSatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RepoCallReqSts', type=RepoCallRequestStatus10Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=InstructionProcessingStatus26Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmCondModSts', type=SettlementConditionModificationStatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnEvtStag', type=CorporateActionEventStage4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AffirmSts', type=AffirmationStatus9Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlPrcgSts', type=CancellationProcessingStatus8Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus28Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus28Choice, min=0, max=1, mutex_group=1, array=False),
	))

