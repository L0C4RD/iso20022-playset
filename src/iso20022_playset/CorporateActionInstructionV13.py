import base_types
import YesNoIndicator
import SupplementaryData1
import DocumentIdentification31
import CorporateActionGeneralInformation180
import DocumentIdentification32
import CorporateActionNarrative30
import CorporateActionEventReference3
import CorporateActionOption237
import PartyIdentification313
import AccountAndBalance61
import ProtectInstruction1

class CorporateActionInstructionV13(base_types._BaseFieldType):

	__slots__ = ["_EvtsLkg", "_ChngInstrInd", "_AddtlInf", "_CancInstrId", "_PrtctInstr", "_SplmtryData", "_BnfclOwnrDtls", "_AcctDtls", "_CorpActnGnlInf", "_InstrCxlReqId", "_CorpActnInstr", "_OthrDocId"]
	@property
	def EvtsLkg(self):
		return self._EvtsLkg

	@EvtsLkg.setter
	def EvtsLkg(self, value):
		self._EvtsLkg = value if type(value) != auto else self.make_default("EvtsLkg")

	@EvtsLkg.deleter
	def EvtsLkg(self):
		del self._EvtsLkg
		self._EvtsLkg = None

	@property
	def ChngInstrInd(self):
		return self._ChngInstrInd

	@ChngInstrInd.setter
	def ChngInstrInd(self, value):
		self._ChngInstrInd = value if type(value) != auto else self.make_default("ChngInstrInd")

	@ChngInstrInd.deleter
	def ChngInstrInd(self):
		del self._ChngInstrInd
		self._ChngInstrInd = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CancInstrId(self):
		return self._CancInstrId

	@CancInstrId.setter
	def CancInstrId(self, value):
		self._CancInstrId = value if type(value) != auto else self.make_default("CancInstrId")

	@CancInstrId.deleter
	def CancInstrId(self):
		del self._CancInstrId
		self._CancInstrId = None

	@property
	def PrtctInstr(self):
		return self._PrtctInstr

	@PrtctInstr.setter
	def PrtctInstr(self, value):
		self._PrtctInstr = value if type(value) != auto else self.make_default("PrtctInstr")

	@PrtctInstr.deleter
	def PrtctInstr(self):
		del self._PrtctInstr
		self._PrtctInstr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def BnfclOwnrDtls(self):
		return self._BnfclOwnrDtls

	@BnfclOwnrDtls.setter
	def BnfclOwnrDtls(self, value):
		self._BnfclOwnrDtls = value if type(value) != auto else self.make_default("BnfclOwnrDtls")

	@BnfclOwnrDtls.deleter
	def BnfclOwnrDtls(self):
		del self._BnfclOwnrDtls
		self._BnfclOwnrDtls = None

	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if type(value) != auto else self.make_default("CorpActnGnlInf")

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = None

	@property
	def InstrCxlReqId(self):
		return self._InstrCxlReqId

	@InstrCxlReqId.setter
	def InstrCxlReqId(self, value):
		self._InstrCxlReqId = value if type(value) != auto else self.make_default("InstrCxlReqId")

	@InstrCxlReqId.deleter
	def InstrCxlReqId(self):
		del self._InstrCxlReqId
		self._InstrCxlReqId = None

	@property
	def CorpActnInstr(self):
		return self._CorpActnInstr

	@CorpActnInstr.setter
	def CorpActnInstr(self, value):
		self._CorpActnInstr = value if type(value) != auto else self.make_default("CorpActnInstr")

	@CorpActnInstr.deleter
	def CorpActnInstr(self):
		del self._CorpActnInstr
		self._CorpActnInstr = None

	@property
	def OthrDocId(self):
		return self._OthrDocId

	@OthrDocId.setter
	def OthrDocId(self, value):
		self._OthrDocId = value if type(value) != auto else self.make_default("OthrDocId")

	@OthrDocId.deleter
	def OthrDocId(self):
		del self._OthrDocId
		self._OthrDocId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtsLkg', type=CorporateActionEventReference3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChngInstrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CancInstrId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctInstr', type=ProtectInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BnfclOwnrDtls', type=PartyIdentification313, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctDtls', type=AccountAndBalance61, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation180, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCxlReqId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnInstr', type=CorporateActionOption237, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification32, min=0, max=None, mutex_group=None, array=True),
	))

