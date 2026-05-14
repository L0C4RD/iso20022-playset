# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountIdentification78Choice import AccountIdentification78Choice
from ._CorporateAction87 import CorporateAction87
from ._CorporateActionEventReference4 import CorporateActionEventReference4
from ._CorporateActionGeneralInformation194 import CorporateActionGeneralInformation194
from ._CorporateActionNarrative65 import CorporateActionNarrative65
from ._CorporateActionNotification11 import CorporateActionNotification11
from ._CorporateActionOption247 import CorporateActionOption247
from ._DocumentIdentification17 import DocumentIdentification17
from ._DocumentIdentification37 import DocumentIdentification37
from ._DocumentIdentification38 import DocumentIdentification38
from ._FinancialInstrumentAttributes117 import FinancialInstrumentAttributes117
from ._Pagination1 import Pagination1
from ._PartyIdentification137Choice import PartyIdentification137Choice
from ._PartyIdentification151Choice import PartyIdentification151Choice
from ._SupplementaryData1 import SupplementaryData1

class CorporateActionNotification002V15(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_AddtlInf", "_CorpActnDtls", "_CorpActnGnlInf", "_CorpActnOptnDtls", "_DrpAgt", "_EvtsLkg", "_InfAgt", "_InstrId", "_IntrmdtScty", "_Issr", "_IssrAgt", "_NtfctnGnlInf", "_Offerr", "_OthrDocId", "_Pgntn", "_PhysSctiesAgt", "_PngAgt", "_PrvsNtfctnId", "_Regar", "_RsellngAgt", "_SlctnAgt", "_SplmtryData", "_SubPngAgt", "_TrfAgt"]
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
	def CorpActnOptnDtls(self):
		return self._CorpActnOptnDtls

	@CorpActnOptnDtls.setter
	def CorpActnOptnDtls(self, value):
		self._CorpActnOptnDtls = value if type(value) != base_types.auto else self.make_default("CorpActnOptnDtls")

	@CorpActnOptnDtls.deleter
	def CorpActnOptnDtls(self):
		del self._CorpActnOptnDtls
		self._CorpActnOptnDtls = None

	@property
	def DrpAgt(self):
		return self._DrpAgt

	@DrpAgt.setter
	def DrpAgt(self, value):
		self._DrpAgt = value if type(value) != base_types.auto else self.make_default("DrpAgt")

	@DrpAgt.deleter
	def DrpAgt(self):
		del self._DrpAgt
		self._DrpAgt = None

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
	def InfAgt(self):
		return self._InfAgt

	@InfAgt.setter
	def InfAgt(self, value):
		self._InfAgt = value if type(value) != base_types.auto else self.make_default("InfAgt")

	@InfAgt.deleter
	def InfAgt(self):
		del self._InfAgt
		self._InfAgt = None

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
	def IntrmdtScty(self):
		return self._IntrmdtScty

	@IntrmdtScty.setter
	def IntrmdtScty(self, value):
		self._IntrmdtScty = value if type(value) != base_types.auto else self.make_default("IntrmdtScty")

	@IntrmdtScty.deleter
	def IntrmdtScty(self):
		del self._IntrmdtScty
		self._IntrmdtScty = None

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if type(value) != base_types.auto else self.make_default("Issr")

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = None

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
	def NtfctnGnlInf(self):
		return self._NtfctnGnlInf

	@NtfctnGnlInf.setter
	def NtfctnGnlInf(self, value):
		self._NtfctnGnlInf = value if type(value) != base_types.auto else self.make_default("NtfctnGnlInf")

	@NtfctnGnlInf.deleter
	def NtfctnGnlInf(self):
		del self._NtfctnGnlInf
		self._NtfctnGnlInf = None

	@property
	def Offerr(self):
		return self._Offerr

	@Offerr.setter
	def Offerr(self, value):
		self._Offerr = value if type(value) != base_types.auto else self.make_default("Offerr")

	@Offerr.deleter
	def Offerr(self):
		del self._Offerr
		self._Offerr = None

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
	def PhysSctiesAgt(self):
		return self._PhysSctiesAgt

	@PhysSctiesAgt.setter
	def PhysSctiesAgt(self, value):
		self._PhysSctiesAgt = value if type(value) != base_types.auto else self.make_default("PhysSctiesAgt")

	@PhysSctiesAgt.deleter
	def PhysSctiesAgt(self):
		del self._PhysSctiesAgt
		self._PhysSctiesAgt = None

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
	def PrvsNtfctnId(self):
		return self._PrvsNtfctnId

	@PrvsNtfctnId.setter
	def PrvsNtfctnId(self, value):
		self._PrvsNtfctnId = value if type(value) != base_types.auto else self.make_default("PrvsNtfctnId")

	@PrvsNtfctnId.deleter
	def PrvsNtfctnId(self):
		del self._PrvsNtfctnId
		self._PrvsNtfctnId = None

	@property
	def Regar(self):
		return self._Regar

	@Regar.setter
	def Regar(self, value):
		self._Regar = value if type(value) != base_types.auto else self.make_default("Regar")

	@Regar.deleter
	def Regar(self):
		del self._Regar
		self._Regar = None

	@property
	def RsellngAgt(self):
		return self._RsellngAgt

	@RsellngAgt.setter
	def RsellngAgt(self, value):
		self._RsellngAgt = value if type(value) != base_types.auto else self.make_default("RsellngAgt")

	@RsellngAgt.deleter
	def RsellngAgt(self):
		del self._RsellngAgt
		self._RsellngAgt = None

	@property
	def SlctnAgt(self):
		return self._SlctnAgt

	@SlctnAgt.setter
	def SlctnAgt(self, value):
		self._SlctnAgt = value if type(value) != base_types.auto else self.make_default("SlctnAgt")

	@SlctnAgt.deleter
	def SlctnAgt(self):
		del self._SlctnAgt
		self._SlctnAgt = None

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
	def TrfAgt(self):
		return self._TrfAgt

	@TrfAgt.setter
	def TrfAgt(self, value):
		self._TrfAgt = value if type(value) != base_types.auto else self.make_default("TrfAgt")

	@TrfAgt.deleter
	def TrfAgt(self):
		del self._TrfAgt
		self._TrfAgt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=AccountIdentification78Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=CorporateActionNarrative65, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnDtls', type=CorporateAction87, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnGnlInf', type=CorporateActionGeneralInformation194, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnOptnDtls', type=CorporateActionOption247, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DrpAgt', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtsLkg', type=CorporateActionEventReference4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InfAgt', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrId', type=DocumentIdentification17, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmdtScty', type=FinancialInstrumentAttributes117, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification151Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrAgt', type=PartyIdentification151Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtfctnGnlInf', type=CorporateActionNotification11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Offerr', type=PartyIdentification151Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrDocId', type=DocumentIdentification38, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysSctiesAgt', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsNtfctnId', type=DocumentIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regar', type=PartyIdentification137Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsellngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SlctnAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubPngAgt', type=PartyIdentification137Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfAgt', type=PartyIdentification151Choice, min=0, max=1, mutex_group=None, array=False),
	))