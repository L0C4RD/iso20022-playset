# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AffirmationStatus8Choice
from . import AllocationSatus3Choice
from . import CancellationProcessingStatus7Choice
from . import CorporateActionEventProcessingStatus3Choice
from . import CorporateActionEventStage3Choice
from . import InstructionProcessingStatus23Choice
from . import MatchingStatus27Choice
from . import RegistrationProcessingStatus3Choice
from . import ReplacementProcessingStatus8Choice
from . import RepoCallRequestStatus8Choice
from . import ResponseStatus5Choice
from . import SettlementConditionModificationStatus3Choice
from . import SettlementStatus19Choice

class Status19Choice(base_types._BaseFieldType):

	__slots__ = ["_AffirmSts", "_AllcnSts", "_CorpActnEvtPrcgSts", "_CorpActnEvtStag", "_CxlPrcgSts", "_IfrrdMtchgSts", "_InstrPrcgSts", "_MtchgSts", "_RegnPrcgSts", "_RepoCallReqSts", "_RplcmntPrcgSts", "_RspnSts", "_SttlmCondModSts", "_SttlmSts"]
	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if value is not None else base_types.UninitialisedField(self, 'AffirmSts', AffirmationStatus8Choice, False)

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = base_types.UninitialisedField(self, 'AffirmSts', AffirmationStatus8Choice, False)

	@property
	def AllcnSts(self):
		return self._AllcnSts

	@AllcnSts.setter
	def AllcnSts(self, value):
		self._AllcnSts = value if value is not None else base_types.UninitialisedField(self, 'AllcnSts', AllocationSatus3Choice, False)

	@AllcnSts.deleter
	def AllcnSts(self):
		del self._AllcnSts
		self._AllcnSts = base_types.UninitialisedField(self, 'AllcnSts', AllocationSatus3Choice, False)

	@property
	def CorpActnEvtPrcgSts(self):
		return self._CorpActnEvtPrcgSts

	@CorpActnEvtPrcgSts.setter
	def CorpActnEvtPrcgSts(self, value):
		self._CorpActnEvtPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtPrcgSts', CorporateActionEventProcessingStatus3Choice, False)

	@CorpActnEvtPrcgSts.deleter
	def CorpActnEvtPrcgSts(self):
		del self._CorpActnEvtPrcgSts
		self._CorpActnEvtPrcgSts = base_types.UninitialisedField(self, 'CorpActnEvtPrcgSts', CorporateActionEventProcessingStatus3Choice, False)

	@property
	def CorpActnEvtStag(self):
		return self._CorpActnEvtStag

	@CorpActnEvtStag.setter
	def CorpActnEvtStag(self, value):
		self._CorpActnEvtStag = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtStag', CorporateActionEventStage3Choice, False)

	@CorpActnEvtStag.deleter
	def CorpActnEvtStag(self):
		del self._CorpActnEvtStag
		self._CorpActnEvtStag = base_types.UninitialisedField(self, 'CorpActnEvtStag', CorporateActionEventStage3Choice, False)

	@property
	def CxlPrcgSts(self):
		return self._CxlPrcgSts

	@CxlPrcgSts.setter
	def CxlPrcgSts(self, value):
		self._CxlPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'CxlPrcgSts', CancellationProcessingStatus7Choice, False)

	@CxlPrcgSts.deleter
	def CxlPrcgSts(self):
		del self._CxlPrcgSts
		self._CxlPrcgSts = base_types.UninitialisedField(self, 'CxlPrcgSts', CancellationProcessingStatus7Choice, False)

	@property
	def IfrrdMtchgSts(self):
		return self._IfrrdMtchgSts

	@IfrrdMtchgSts.setter
	def IfrrdMtchgSts(self, value):
		self._IfrrdMtchgSts = value if value is not None else base_types.UninitialisedField(self, 'IfrrdMtchgSts', MatchingStatus27Choice, False)

	@IfrrdMtchgSts.deleter
	def IfrrdMtchgSts(self):
		del self._IfrrdMtchgSts
		self._IfrrdMtchgSts = base_types.UninitialisedField(self, 'IfrrdMtchgSts', MatchingStatus27Choice, False)

	@property
	def InstrPrcgSts(self):
		return self._InstrPrcgSts

	@InstrPrcgSts.setter
	def InstrPrcgSts(self, value):
		self._InstrPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'InstrPrcgSts', InstructionProcessingStatus23Choice, False)

	@InstrPrcgSts.deleter
	def InstrPrcgSts(self):
		del self._InstrPrcgSts
		self._InstrPrcgSts = base_types.UninitialisedField(self, 'InstrPrcgSts', InstructionProcessingStatus23Choice, False)

	@property
	def MtchgSts(self):
		return self._MtchgSts

	@MtchgSts.setter
	def MtchgSts(self, value):
		self._MtchgSts = value if value is not None else base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus27Choice, False)

	@MtchgSts.deleter
	def MtchgSts(self):
		del self._MtchgSts
		self._MtchgSts = base_types.UninitialisedField(self, 'MtchgSts', MatchingStatus27Choice, False)

	@property
	def RegnPrcgSts(self):
		return self._RegnPrcgSts

	@RegnPrcgSts.setter
	def RegnPrcgSts(self, value):
		self._RegnPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'RegnPrcgSts', RegistrationProcessingStatus3Choice, False)

	@RegnPrcgSts.deleter
	def RegnPrcgSts(self):
		del self._RegnPrcgSts
		self._RegnPrcgSts = base_types.UninitialisedField(self, 'RegnPrcgSts', RegistrationProcessingStatus3Choice, False)

	@property
	def RepoCallReqSts(self):
		return self._RepoCallReqSts

	@RepoCallReqSts.setter
	def RepoCallReqSts(self, value):
		self._RepoCallReqSts = value if value is not None else base_types.UninitialisedField(self, 'RepoCallReqSts', RepoCallRequestStatus8Choice, False)

	@RepoCallReqSts.deleter
	def RepoCallReqSts(self):
		del self._RepoCallReqSts
		self._RepoCallReqSts = base_types.UninitialisedField(self, 'RepoCallReqSts', RepoCallRequestStatus8Choice, False)

	@property
	def RplcmntPrcgSts(self):
		return self._RplcmntPrcgSts

	@RplcmntPrcgSts.setter
	def RplcmntPrcgSts(self, value):
		self._RplcmntPrcgSts = value if value is not None else base_types.UninitialisedField(self, 'RplcmntPrcgSts', ReplacementProcessingStatus8Choice, False)

	@RplcmntPrcgSts.deleter
	def RplcmntPrcgSts(self):
		del self._RplcmntPrcgSts
		self._RplcmntPrcgSts = base_types.UninitialisedField(self, 'RplcmntPrcgSts', ReplacementProcessingStatus8Choice, False)

	@property
	def RspnSts(self):
		return self._RspnSts

	@RspnSts.setter
	def RspnSts(self, value):
		self._RspnSts = value if value is not None else base_types.UninitialisedField(self, 'RspnSts', ResponseStatus5Choice, False)

	@RspnSts.deleter
	def RspnSts(self):
		del self._RspnSts
		self._RspnSts = base_types.UninitialisedField(self, 'RspnSts', ResponseStatus5Choice, False)

	@property
	def SttlmCondModSts(self):
		return self._SttlmCondModSts

	@SttlmCondModSts.setter
	def SttlmCondModSts(self, value):
		self._SttlmCondModSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmCondModSts', SettlementConditionModificationStatus3Choice, False)

	@SttlmCondModSts.deleter
	def SttlmCondModSts(self):
		del self._SttlmCondModSts
		self._SttlmCondModSts = base_types.UninitialisedField(self, 'SttlmCondModSts', SettlementConditionModificationStatus3Choice, False)

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus19Choice, False)

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus19Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AffirmSts', type=AffirmationStatus8Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AllcnSts', type=AllocationSatus3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnEvtPrcgSts', type=CorporateActionEventProcessingStatus3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnEvtStag', type=CorporateActionEventStage3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlPrcgSts', type=CancellationProcessingStatus7Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IfrrdMtchgSts', type=MatchingStatus27Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=InstructionProcessingStatus23Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MtchgSts', type=MatchingStatus27Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RegnPrcgSts', type=RegistrationProcessingStatus3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RepoCallReqSts', type=RepoCallRequestStatus8Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RplcmntPrcgSts', type=ReplacementProcessingStatus8Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RspnSts', type=ResponseStatus5Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmCondModSts', type=SettlementConditionModificationStatus3Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus19Choice, min=0, max=1, mutex_group=1, array=False),
	))