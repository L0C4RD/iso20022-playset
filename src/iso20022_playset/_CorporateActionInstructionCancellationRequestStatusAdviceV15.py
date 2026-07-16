# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionGeneralInformation182
from . import CorporateActionNarrative10
from . import CorporateActionOption239
from . import DocumentIdentification33
from . import DocumentIdentification9
from . import InstructionCancellationRequestStatus21Choice
from . import ProtectInstruction4
from . import SupplementaryData1

class CorporateActionInstructionCancellationRequestStatusAdviceV15(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CorpActnGnlInf", "_CorpActnInstr", "_InstrCxlReqId", "_InstrCxlReqSts", "_OthrDocId", "_PrtctInstr", "_SplmtryData"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative10, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative10, False)

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation182, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation182, False)

	@property
	def CorpActnInstr(self):
		return self._CorpActnInstr

	@CorpActnInstr.setter
	def CorpActnInstr(self, value):
		self._CorpActnInstr = value if value is not None else base_types.UninitialisedField(self, 'CorpActnInstr', CorporateActionOption239, False)

	@CorpActnInstr.deleter
	def CorpActnInstr(self):
		del self._CorpActnInstr
		self._CorpActnInstr = base_types.UninitialisedField(self, 'CorpActnInstr', CorporateActionOption239, False)

	@property
	def InstrCxlReqId(self):
		return self._InstrCxlReqId

	@InstrCxlReqId.setter
	def InstrCxlReqId(self, value):
		self._InstrCxlReqId = value if value is not None else base_types.UninitialisedField(self, 'InstrCxlReqId', DocumentIdentification9, False)

	@InstrCxlReqId.deleter
	def InstrCxlReqId(self):
		del self._InstrCxlReqId
		self._InstrCxlReqId = base_types.UninitialisedField(self, 'InstrCxlReqId', DocumentIdentification9, False)

	@property
	def InstrCxlReqSts(self):
		return self._InstrCxlReqSts

	@InstrCxlReqSts.setter
	def InstrCxlReqSts(self, value):
		self._InstrCxlReqSts = value if value is not None else base_types.UninitialisedField(self, 'InstrCxlReqSts', InstructionCancellationRequestStatus21Choice, True)

	@InstrCxlReqSts.deleter
	def InstrCxlReqSts(self):
		del self._InstrCxlReqSts
		self._InstrCxlReqSts = base_types.UninitialisedField(self, 'InstrCxlReqSts', InstructionCancellationRequestStatus21Choice, True)

	@property
	def OthrDocId(self):
		return self._OthrDocId

	@OthrDocId.setter
	def OthrDocId(self, value):
		self._OthrDocId = value if value is not None else base_types.UninitialisedField(self, 'OthrDocId', DocumentIdentification33, True)

	@OthrDocId.deleter
	def OthrDocId(self):
		del self._OthrDocId
		self._OthrDocId = base_types.UninitialisedField(self, 'OthrDocId', DocumentIdentification33, True)

	@property
	def PrtctInstr(self):
		return self._PrtctInstr

	@PrtctInstr.setter
	def PrtctInstr(self, value):
		self._PrtctInstr = value if value is not None else base_types.UninitialisedField(self, 'PrtctInstr', ProtectInstruction4, False)

	@PrtctInstr.deleter
	def PrtctInstr(self):
		del self._PrtctInstr
		self._PrtctInstr = base_types.UninitialisedField(self, 'PrtctInstr', ProtectInstruction4, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation182, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnInstr', type=CorporateActionOption239, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCxlReqId', type=DocumentIdentification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCxlReqSts', type=InstructionCancellationRequestStatus21Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification33, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctInstr', type=ProtectInstruction4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))