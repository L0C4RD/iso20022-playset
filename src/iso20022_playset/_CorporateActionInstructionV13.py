# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountAndBalance61
from . import CorporateActionEventReference3
from . import CorporateActionGeneralInformation180
from . import CorporateActionNarrative30
from . import CorporateActionOption237
from . import DocumentIdentification31
from . import DocumentIdentification32
from . import PartyIdentification313
from . import ProtectInstruction1
from . import SupplementaryData1
from . import YesNoIndicator

class CorporateActionInstructionV13(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_AddtlInf", "_BnfclOwnrDtls", "_CancInstrId", "_ChngInstrInd", "_CorpActnGnlInf", "_CorpActnInstr", "_EvtsLkg", "_InstrCxlReqId", "_OthrDocId", "_PrtctInstr", "_SplmtryData"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', AccountAndBalance61, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', AccountAndBalance61, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative30, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative30, False)

	@property
	def BnfclOwnrDtls(self):
		return self._BnfclOwnrDtls

	@BnfclOwnrDtls.setter
	def BnfclOwnrDtls(self, value):
		self._BnfclOwnrDtls = value if value is not None else base_types.UninitialisedField(self, 'BnfclOwnrDtls', PartyIdentification313, True)

	@BnfclOwnrDtls.deleter
	def BnfclOwnrDtls(self):
		del self._BnfclOwnrDtls
		self._BnfclOwnrDtls = base_types.UninitialisedField(self, 'BnfclOwnrDtls', PartyIdentification313, True)

	@property
	def CancInstrId(self):
		return self._CancInstrId

	@CancInstrId.setter
	def CancInstrId(self, value):
		self._CancInstrId = value if value is not None else base_types.UninitialisedField(self, 'CancInstrId', DocumentIdentification31, False)

	@CancInstrId.deleter
	def CancInstrId(self):
		del self._CancInstrId
		self._CancInstrId = base_types.UninitialisedField(self, 'CancInstrId', DocumentIdentification31, False)

	@property
	def ChngInstrInd(self):
		return self._ChngInstrInd

	@ChngInstrInd.setter
	def ChngInstrInd(self, value):
		self._ChngInstrInd = value if value is not None else base_types.UninitialisedField(self, 'ChngInstrInd', YesNoIndicator, False)

	@ChngInstrInd.deleter
	def ChngInstrInd(self):
		del self._ChngInstrInd
		self._ChngInstrInd = base_types.UninitialisedField(self, 'ChngInstrInd', YesNoIndicator, False)

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation180, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation180, False)

	@property
	def CorpActnInstr(self):
		return self._CorpActnInstr

	@CorpActnInstr.setter
	def CorpActnInstr(self, value):
		self._CorpActnInstr = value if value is not None else base_types.UninitialisedField(self, 'CorpActnInstr', CorporateActionOption237, False)

	@CorpActnInstr.deleter
	def CorpActnInstr(self):
		del self._CorpActnInstr
		self._CorpActnInstr = base_types.UninitialisedField(self, 'CorpActnInstr', CorporateActionOption237, False)

	@property
	def EvtsLkg(self):
		return self._EvtsLkg

	@EvtsLkg.setter
	def EvtsLkg(self, value):
		self._EvtsLkg = value if value is not None else base_types.UninitialisedField(self, 'EvtsLkg', CorporateActionEventReference3, True)

	@EvtsLkg.deleter
	def EvtsLkg(self):
		del self._EvtsLkg
		self._EvtsLkg = base_types.UninitialisedField(self, 'EvtsLkg', CorporateActionEventReference3, True)

	@property
	def InstrCxlReqId(self):
		return self._InstrCxlReqId

	@InstrCxlReqId.setter
	def InstrCxlReqId(self, value):
		self._InstrCxlReqId = value if value is not None else base_types.UninitialisedField(self, 'InstrCxlReqId', DocumentIdentification31, False)

	@InstrCxlReqId.deleter
	def InstrCxlReqId(self):
		del self._InstrCxlReqId
		self._InstrCxlReqId = base_types.UninitialisedField(self, 'InstrCxlReqId', DocumentIdentification31, False)

	@property
	def OthrDocId(self):
		return self._OthrDocId

	@OthrDocId.setter
	def OthrDocId(self, value):
		self._OthrDocId = value if value is not None else base_types.UninitialisedField(self, 'OthrDocId', DocumentIdentification32, True)

	@OthrDocId.deleter
	def OthrDocId(self):
		del self._OthrDocId
		self._OthrDocId = base_types.UninitialisedField(self, 'OthrDocId', DocumentIdentification32, True)

	@property
	def PrtctInstr(self):
		return self._PrtctInstr

	@PrtctInstr.setter
	def PrtctInstr(self, value):
		self._PrtctInstr = value if value is not None else base_types.UninitialisedField(self, 'PrtctInstr', ProtectInstruction1, False)

	@PrtctInstr.deleter
	def PrtctInstr(self):
		del self._PrtctInstr
		self._PrtctInstr = base_types.UninitialisedField(self, 'PrtctInstr', ProtectInstruction1, False)

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
		base_types.FieldEntry(name='AcctDtls', type=AccountAndBalance61, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfclOwnrDtls', type=PartyIdentification313, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CancInstrId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChngInstrInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation180, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnInstr', type=CorporateActionOption237, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtsLkg', type=CorporateActionEventReference3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrCxlReqId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification32, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctInstr', type=ProtectInstruction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))