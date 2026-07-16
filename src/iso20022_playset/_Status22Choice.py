# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AffirmationStatus9Choice
from . import AllocationSatus4Choice
from . import CancellationProcessingStatus8Choice
from . import CorporateActionEventProcessingStatus4Choice
from . import CorporateActionEventStage4Choice
from . import InstructionProcessingStatus26Choice
from . import MatchingStatus28Choice
from . import RegistrationProcessingStatus4Choice
from . import ReplacementProcessingStatus9Choice
from . import RepoCallRequestStatus10Choice
from . import ResponseStatus7Choice
from . import SettlementConditionModificationStatus4Choice
from . import SettlementStatus25Choice

class Status22Choice(base_types._BaseFieldType):

	__slots__ = ["_AffirmSts", "_AllcnSts", "_CorpActnEvtPrcgSts", "_CorpActnEvtStag", "_CxlPrcgSts", "_IfrrdMtchgSts", "_InstrPrcgSts", "_MtchgSts", "_RegnPrcgSts", "_RepoCallReqSts", "_RplcmntPrcgSts", "_RspnSts", "_SttlmCondModSts", "_SttlmSts"]
	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if value is not None else base_types.UninitialisedField(self, 'AffirmSts', AffirmationStatus9Choice, False)

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = base_types.UninitialisedField(self, 'AffirmSts', AffirmationStatus9Choice, False)

	@property
	def AllcnSts(self):
		return self._AllcnSts

	@AllcnSts.setter
	def AllcnSts(self, value):
		self._AllcnSts = value if value is not None else base_types.UninitialisedField(self, 'AllcnSts', AllocationSatus4Choice, False)

	@AllcnSts.deleter
	def AllcnSts(self):
		del self._AllcnSts
		self._AllcnSts = base_types.UninitialisedField(self, 'AllcnSts', AllocationSatus4Choice, False)

	@property
	def CorpActnEvtPrcgSts(self):
		return self._CorpActnEvtPrcgSts

	@CorpActnEvtPrcgSts.setter
	def CorpActnEvtPrcgSts(self, value):
		self._CorpActnEvtPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtPrcgSts', CorporateActionEventProcessingStatus4Choice, False)

	@CorpActnEvtPrcgSts.deleter
	def CorpActnEvtPrcgSts(self):
		del self._CorpActnEvtPrcgSts
		self._CorpActnEvtPrcgSts = base_types.UninitialisedField(self, 'CorpActnEvtPrcgSts', CorporateActionEventProcessingStatus4Choice, False)

	@property
	def CorpActnEvtStag(self):
		return self._CorpActnEvtStag

	@CorpActnEvtStag.setter
	def CorpActnEvtStag(self, value):
		self._CorpActnEvtStag = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtStag', CorporateActionEventStage4Choice, False)

	@CorpActnEvtStag.deleter
	def CorpActnEvtStag(self):
		del self._CorpActnEvtStag
		self._CorpActnEvtStag = base_types.UninitialisedField(self, 'CorpActnEvtStag', CorporateActionEventStage4Choice, False)

	@property
	def CxlPrcgSts(self):
		return self._CxlPrcgSts

	@CxlPrcgSts.setter
	def CxlPrcgSts(self, value):
		self._CxlPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'CxlPrcgSts', CancellationProcessingStatus8Choice, False)

	@CxlPrcgSts.deleter
	def CxlPrcgSts(self):
		del self._CxlPrcgSts
		self._CxlPrcgSts = base_types.UninitialisedField(self, 'CxlPrcgSts', CancellationProcessingStatus8Choice, False)

	@property
	def IfrrdMtchgSts(self):
		return self._IfrrdMtchgSts

	@IfrrdMtchgSts.setter
	def IfrrdMtchgSts(self, value):
		self._IfrrdMtchgSts = value if value is not None else base_types.UninitialisedField(self, 'IfrrdMtchgSts', MatchingStatus28Choice, False)

	@IfrrdMtchgSts.deleter
	def IfrrdMtchgSts(self):
		del self._IfrrdMtchgSts
		self._IfrrdMtchgSts = base_types.UninitialisedField(self, 'IfrrdMtchgSts', MatchingStatus28Choice, False)

	@property
	def InstrPrcgSts(self):
		return self._InstrPrcgSts

	@InstrPrcgSts.setter
	def InstrPrcgSts(self, value):
		self._InstrPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'InstrPrcgSts', InstructionProcessingStatus26Choice, False)

	@InstrPrcgSts.deleter
	def InstrPrcgSts(self):
		del self._InstrPrcgSts
		self._InstrPrcgSts = base_types.UninitialisedField(self, 'InstrPrcgSts', InstructionProcessingStatus26Choice, False)

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if value is not None else base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus28Choice, False)

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus28Choice, False)

	@property
	def RegnPrcgSts(self):
		return self._RegnPrcgSts

	@RegnPrcgSts.setter
	def RegnPrcgSts(self, value):
		self._RegnPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'RegnPrcgSts', RegistrationProcessingStatus4Choice, False)

	@RegnPrcgSts.deleter
	def RegnPrcgSts(self):
		del self._RegnPrcgSts
		self._RegnPrcgSts = base_types.UninitialisedField(self, 'RegnPrcgSts', RegistrationProcessingStatus4Choice, False)

	@property
	def RepoCallReqSts(self):
		return self._RepoCallReqSts

	@RepoCallReqSts.setter
	def RepoCallReqSts(self, value):
		self._RepoCallReqSts = value if value is not None else base_types.UninitialisedField(self, 'RepoCallReqSts', RepoCallRequestStatus10Choice, False)

	@RepoCallReqSts.deleter
	def RepoCallReqSts(self):
		del self._RepoCallReqSts
		self._RepoCallReqSts = base_types.UninitialisedField(self, 'RepoCallReqSts', RepoCallRequestStatus10Choice, False)

	@property
	def RplcmntPrcgSts(self):
		return self._RplcmntPrcgSts

	@RplcmntPrcgSts.setter
	def RplcmntPrcgSts(self, value):
		self._RplcmntPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'RplcmntPrcgSts', ReplacementProcessingStatus9Choice, False)

	@RplcmntPrcgSts.deleter
	def RplcmntPrcgSts(self):
		del self._RplcmntPrcgSts
		self._RplcmntPrcgSts = base_types.UninitialisedField(self, 'RplcmntPrcgSts', ReplacementProcessingStatus9Choice, False)

	@property
	def RspnSts(self):
		return self._RspnSts

	@RspnSts.setter
	def RspnSts(self, value):
		self._RspnSts = value if value is not None else base_types.UninitialisedField(self, 'RspnSts', ResponseStatus7Choice, False)

	@RspnSts.deleter
	def RspnSts(self):
		del self._RspnSts
		self._RspnSts = base_types.UninitialisedField(self, 'RspnSts', ResponseStatus7Choice, False)

	@property
	def SttlmCondModSts(self):
		return self._SttlmCondModSts

	@SttlmCondModSts.setter
	def SttlmCondModSts(self, value):
		self._SttlmCondModSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmCondModSts', SettlementConditionModificationStatus4Choice, False)

	@SttlmCondModSts.deleter
	def SttlmCondModSts(self):
		del self._SttlmCondModSts
		self._SttlmCondModSts = base_types.UninitialisedField(self, 'SttlmCondModSts', SettlementConditionModificationStatus4Choice, False)

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus25Choice, False)

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus25Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AffirmSts', type=AffirmationStatus9Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AllcnSts', type=AllocationSatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnEvtPrcgSts', type=CorporateActionEventProcessingStatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnEvtStag', type=CorporateActionEventStage4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlPrcgSts', type=CancellationProcessingStatus8Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus28Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=InstructionProcessingStatus26Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus28Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RegnPrcgSts', type=RegistrationProcessingStatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RepoCallReqSts', type=RepoCallRequestStatus10Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RplcmntPrcgSts', type=ReplacementProcessingStatus9Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RspnSts', type=ResponseStatus7Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmCondModSts', type=SettlementConditionModificationStatus4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus25Choice, min=0, max=1, mutex_group=1, array=False),
	))