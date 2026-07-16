# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountAndBalance58
from . import CorporateAction92
from . import CorporateActionEventReference3
from . import CorporateActionGeneralInformation179
from . import CorporateActionNarrative31
from . import CorporateActionOption253
from . import DocumentIdentification31
from . import DocumentIdentification32
from . import DocumentIdentification9
from . import Max35Text
from . import Pagination1
from . import PartyIdentification120Choice
from . import SupplementaryData1
from . import TransactionIdentification15

class CorporateActionMovementConfirmationV17(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_AddtlInf", "_CorpActnConfDtls", "_CorpActnDtls", "_CorpActnGnlInf", "_EvtsLkg", "_InstrId", "_IssrAgt", "_MvmntConfId", "_MvmntPrlimryAdvcId", "_NtfctnId", "_OthrDocId", "_Pgntn", "_PngAgt", "_SplmtryData", "_SubPngAgt", "_TxId"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', AccountAndBalance58, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', AccountAndBalance58, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative31, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', CorporateActionNarrative31, False)

	@property
	def CorpActnConfDtls(self):
		return self._CorpActnConfDtls

	@CorpActnConfDtls.setter
	def CorpActnConfDtls(self, value):
		self._CorpActnConfDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnConfDtls', CorporateActionOption253, False)

	@CorpActnConfDtls.deleter
	def CorpActnConfDtls(self):
		del self._CorpActnConfDtls
		self._CorpActnConfDtls = base_types.UninitialisedField(self, 'CorpActnConfDtls', CorporateActionOption253, False)

	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if value is not None else base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction92, False)

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = base_types.UninitialisedField(self, 'CorpActnDtls', CorporateAction92, False)

	@property
	def CorpActnGnlInf(self):
		return self._CorpActnGnlInf

	@CorpActnGnlInf.setter
	def CorpActnGnlInf(self, value):
		self._CorpActnGnlInf = value if value is not None else base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation179, False)

	@CorpActnGnlInf.deleter
	def CorpActnGnlInf(self):
		del self._CorpActnGnlInf
		self._CorpActnGnlInf = base_types.UninitialisedField(self, 'CorpActnGnlInf', CorporateActionGeneralInformation179, False)

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
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if value is not None else base_types.UninitialisedField(self, 'InstrId', DocumentIdentification9, False)

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = base_types.UninitialisedField(self, 'InstrId', DocumentIdentification9, False)

	@property
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if value is not None else base_types.UninitialisedField(self, 'IssrAgt', PartyIdentification120Choice, True)

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = base_types.UninitialisedField(self, 'IssrAgt', PartyIdentification120Choice, True)

	@property
	def MvmntConfId(self):
		return self._MvmntConfId

	@MvmntConfId.setter
	def MvmntConfId(self, value):
		self._MvmntConfId = value if value is not None else base_types.UninitialisedField(self, 'MvmntConfId', Max35Text, False)

	@MvmntConfId.deleter
	def MvmntConfId(self):
		del self._MvmntConfId
		self._MvmntConfId = base_types.UninitialisedField(self, 'MvmntConfId', Max35Text, False)

	@property
	def MvmntPrlimryAdvcId(self):
		return self._MvmntPrlimryAdvcId

	@MvmntPrlimryAdvcId.setter
	def MvmntPrlimryAdvcId(self, value):
		self._MvmntPrlimryAdvcId = value if value is not None else base_types.UninitialisedField(self, 'MvmntPrlimryAdvcId', DocumentIdentification31, False)

	@MvmntPrlimryAdvcId.deleter
	def MvmntPrlimryAdvcId(self):
		del self._MvmntPrlimryAdvcId
		self._MvmntPrlimryAdvcId = base_types.UninitialisedField(self, 'MvmntPrlimryAdvcId', DocumentIdentification31, False)

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if value is not None else base_types.UninitialisedField(self, 'NtfctnId', DocumentIdentification31, False)

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = base_types.UninitialisedField(self, 'NtfctnId', DocumentIdentification31, False)

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
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination1, False)

	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if value is not None else base_types.UninitialisedField(self, 'PngAgt', PartyIdentification120Choice, True)

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = base_types.UninitialisedField(self, 'PngAgt', PartyIdentification120Choice, True)

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

	@property
	def SubPngAgt(self):
		return self._SubPngAgt

	@SubPngAgt.setter
	def SubPngAgt(self, value):
		self._SubPngAgt = value if value is not None else base_types.UninitialisedField(self, 'SubPngAgt', PartyIdentification120Choice, True)

	@SubPngAgt.deleter
	def SubPngAgt(self):
		del self._SubPngAgt
		self._SubPngAgt = base_types.UninitialisedField(self, 'SubPngAgt', PartyIdentification120Choice, True)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentification15, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentification15, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=AccountAndBalance58, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnConfDtls', type=CorporateActionOption253, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction92, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation179, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtsLkg', type=CorporateActionEventReference3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrId', type=DocumentIdentification9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MvmntConfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntPrlimryAdvcId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnId', type=DocumentIdentification31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification32, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubPngAgt', type=PartyIdentification120Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification15, min=0, max=1, mutex_group=None, array=False),
	))