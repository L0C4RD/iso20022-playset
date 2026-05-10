from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .ProtectInstruction8 import ProtectInstruction8
from .DocumentIdentification34 import DocumentIdentification34
from .CorporateActionNarrative19 import CorporateActionNarrative19
from .CorporateActionGeneralInformation186 import CorporateActionGeneralInformation186
from .DocumentIdentification17 import DocumentIdentification17
from .InstructionCancellationRequestStatus18Choice import InstructionCancellationRequestStatus18Choice
from .CorporateActionOption241 import CorporateActionOption241

class CorporateActionInstructionCancellationRequestStatusAdvice002V14(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_SplmtryData", "_CorpActnInstr", "_InstrCxlReqId", "_OthrDocId", "_PrtctInstr", "_InstrCxlReqSts", "_CorpActnGnlInf"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def CorpActnInstr(self):
		return self._CorpActnInstr

	@CorpActnInstr.setter
	def CorpActnInstr(self, value):
		self._CorpActnInstr = value if type(value) != base_types.auto else self.make_default("CorpActnInstr")

	@CorpActnInstr.deleter
	def CorpActnInstr(self):
		del self._CorpActnInstr
		self._CorpActnInstr = None

	@property
	def InstrCxlReqId(self):
		return self._InstrCxlReqId

	@InstrCxlReqId.setter
	def InstrCxlReqId(self, value):
		self._InstrCxlReqId = value if type(value) != base_types.auto else self.make_default("InstrCxlReqId")

	@InstrCxlReqId.deleter
	def InstrCxlReqId(self):
		del self._InstrCxlReqId
		self._InstrCxlReqId = None

	@property
	def OthrDocId(self):
		return self._OthrDocId

	@OthrDocId.setter
	def OthrDocId(self, value):
		self._OthrDocId = value if type(value) != base_types.auto else self.make_default("OthrDocId")

	@OthrDocId.deleter
	def OthrDocId(self):
		del self._OthrDocId
		self._OthrDocId = None

	@property
	def PrtctInstr(self):
		return self._PrtctInstr

	@PrtctInstr.setter
	def PrtctInstr(self, value):
		self._PrtctInstr = value if type(value) != base_types.auto else self.make_default("PrtctInstr")

	@PrtctInstr.deleter
	def PrtctInstr(self):
		del self._PrtctInstr
		self._PrtctInstr = None

	@property
	def InstrCxlReqSts(self):
		return self._InstrCxlReqSts

	@InstrCxlReqSts.setter
	def InstrCxlReqSts(self, value):
		self._InstrCxlReqSts = value if type(value) != base_types.auto else self.make_default("InstrCxlReqSts")

	@InstrCxlReqSts.deleter
	def InstrCxlReqSts(self):
		del self._InstrCxlReqSts
		self._InstrCxlReqSts = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != base_types.auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnInstr', type=CorporateActionOption241, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCxlReqId', type=DocumentIdentification17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification34, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctInstr', type=ProtectInstruction8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCxlReqSts', type=InstructionCancellationRequestStatus18Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation186, min=1, max=1, mutex_group=None, array=False),
	))

