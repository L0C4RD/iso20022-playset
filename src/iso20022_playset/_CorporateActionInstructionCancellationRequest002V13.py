from . import base_types
from ._AccountIdentification73 import AccountIdentification73
from ._CorporateActionGeneralInformation187 import CorporateActionGeneralInformation187
from ._CorporateActionNarrative19 import CorporateActionNarrative19
from ._CorporateActionOption202 import CorporateActionOption202
from ._DocumentIdentification37 import DocumentIdentification37
from ._ProtectInstruction7 import ProtectInstruction7
from ._SupplementaryData1 import SupplementaryData1
from ._YesNoIndicator import YesNoIndicator

class CorporateActionInstructionCancellationRequest002V13(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_AddtlInf", "_ChngInstrInd", "_CorpActnGnlInf", "_CorpActnInstr", "_InstrId", "_PrtctInstr", "_SplmtryData"]
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
	def ChngInstrInd(self):
		return self._ChngInstrInd

	@ChngInstrInd.setter
	def ChngInstrInd(self, value):
		self._ChngInstrInd = value if type(value) != base_types.auto else self.make_default("ChngInstrInd")

	@ChngInstrInd.deleter
	def ChngInstrInd(self):
		del self._ChngInstrInd
		self._ChngInstrInd = None

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
		base_types.FieldEntry(name='AcctDtls', type=AccountIdentification73, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngInstrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation187, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnInstr', type=CorporateActionOption202, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrId', type=DocumentIdentification37, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctInstr', type=ProtectInstruction7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

