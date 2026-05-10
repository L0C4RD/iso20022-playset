from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._CorporateActionOption242 import CorporateActionOption242
from ._DocumentIdentification17 import DocumentIdentification17
from ._DocumentIdentification34 import DocumentIdentification34
from ._CorporateActionGeneralInformation188 import CorporateActionGeneralInformation188
from ._CorporateActionNarrative19 import CorporateActionNarrative19
from ._InstructionProcessingStatus58Choice import InstructionProcessingStatus58Choice
from ._ProtectInstruction6 import ProtectInstruction6

class CorporateActionInstructionStatusAdvice002V15(base_types._BaseFieldType):

	__slots__ = ["_InstrId", "_InstrPrcgSts", "_OthrDocId", "_AddtlInf", "_CorpActnInstr", "_PrtctInstr", "_SplmtryData", "_CorpActnGnlInf"]
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
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != base_types.auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

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
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if type(value) != base_types.auto else self.make_default("InstrId")

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = None

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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation188, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnInstr', type=CorporateActionOption242, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrId', type=DocumentIdentification17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgSts', type=InstructionProcessingStatus58Choice, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification34, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctInstr', type=ProtectInstruction6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

