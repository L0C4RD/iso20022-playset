# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountAndBalance58 import AccountAndBalance58
from ._CorporateAction85 import CorporateAction85
from ._CorporateActionEventReference3 import CorporateActionEventReference3
from ._CorporateActionGeneralInformation179 import CorporateActionGeneralInformation179
from ._CorporateActionNarrative31 import CorporateActionNarrative31
from ._CorporateActionOption233 import CorporateActionOption233
from ._DocumentIdentification31 import DocumentIdentification31
from ._DocumentIdentification32 import DocumentIdentification32
from ._DocumentIdentification9 import DocumentIdentification9
from ._Max35Text import Max35Text
from ._Pagination1 import Pagination1
from ._PartyIdentification120Choice import PartyIdentification120Choice
from ._SupplementaryData1 import SupplementaryData1
from ._TransactionIdentification15 import TransactionIdentification15

class CorporateActionMovementConfirmationV16(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_AddtlInf", "_CorpActnConfDtls", "_CorpActnDtls", "_CorpActnGnlInf", "_EvtsLkg", "_InstrId", "_IssrAgt", "_MvmntConfId", "_MvmntPrlimryAdvcId", "_NtfctnId", "_OthrDocId", "_Pgntn", "_PngAgt", "_SplmtryData", "_SubPngAgt", "_TxId"]
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
	def CorpActnConfDtls(self):
		return self._CorpActnConfDtls

	@CorpActnConfDtls.setter
	def CorpActnConfDtls(self, value):
		self._CorpActnConfDtls = value if type(value) != base_types.auto else self.make_default("CorpActnConfDtls")

	@CorpActnConfDtls.deleter
	def CorpActnConfDtls(self):
		del self._CorpActnConfDtls
		self._CorpActnConfDtls = None

	@property
	def CorpActnDtls(self):
		return self._CorpActnDtls

	@CorpActnDtls.setter
	def CorpActnDtls(self, value):
		self._CorpActnDtls = value if type(value) != base_types.auto else self.make_default("CorpActnDtls")

	@CorpActnDtls.deleter
	def CorpActnDtls(self):
		del self._CorpActnDtls
		self._CorpActnDtls = None

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
	def EvtsLkg(self):
		return self._EvtsLkg

	@EvtsLkg.setter
	def EvtsLkg(self, value):
		self._EvtsLkg = value if type(value) != base_types.auto else self.make_default("EvtsLkg")

	@EvtsLkg.deleter
	def EvtsLkg(self):
		del self._EvtsLkg
		self._EvtsLkg = None

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
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if type(value) != base_types.auto else self.make_default("IssrAgt")

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = None

	@property
	def MvmntConfId(self):
		return self._MvmntConfId

	@MvmntConfId.setter
	def MvmntConfId(self, value):
		self._MvmntConfId = value if type(value) != base_types.auto else self.make_default("MvmntConfId")

	@MvmntConfId.deleter
	def MvmntConfId(self):
		del self._MvmntConfId
		self._MvmntConfId = None

	@property
	def MvmntPrlimryAdvcId(self):
		return self._MvmntPrlimryAdvcId

	@MvmntPrlimryAdvcId.setter
	def MvmntPrlimryAdvcId(self, value):
		self._MvmntPrlimryAdvcId = value if type(value) != base_types.auto else self.make_default("MvmntPrlimryAdvcId")

	@MvmntPrlimryAdvcId.deleter
	def MvmntPrlimryAdvcId(self):
		del self._MvmntPrlimryAdvcId
		self._MvmntPrlimryAdvcId = None

	@property
	def NtfctnId(self):
		return self._NtfctnId

	@NtfctnId.setter
	def NtfctnId(self, value):
		self._NtfctnId = value if type(value) != base_types.auto else self.make_default("NtfctnId")

	@NtfctnId.deleter
	def NtfctnId(self):
		del self._NtfctnId
		self._NtfctnId = None

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
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != base_types.auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if type(value) != base_types.auto else self.make_default("PngAgt")

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = None

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
	def SubPngAgt(self):
		return self._SubPngAgt

	@SubPngAgt.setter
	def SubPngAgt(self, value):
		self._SubPngAgt = value if type(value) != base_types.auto else self.make_default("SubPngAgt")

	@SubPngAgt.deleter
	def SubPngAgt(self):
		del self._SubPngAgt
		self._SubPngAgt = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=AccountAndBalance58, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative31, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnConfDtls', type=CorporateActionOption233, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction85, min=0, max=1, mutex_group=None, array=False),
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