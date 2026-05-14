from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._Address4 import Address4
from ._CorporateTaxType1Code import CorporateTaxType1Code
from ._LocalData19 import LocalData19
from ._Max15AlphaNumericText import Max15AlphaNumericText
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._Max99Text import Max99Text

class AcceptorData3(base_types._BaseFieldType):

	__slots__ = ["_AddtlAdr", "_AddtlCtct", "_Adr", "_BizNm", "_BizRegnId", "_BizRegnIdTp", "_BizTp", "_BizTpPrvddBy", "_CertfctnTp", "_CertfctnTpPrvddBy", "_CorpTaxId", "_CorpTaxIdTp", "_CstmrSvc", "_Email", "_Id", "_LclData", "_LglCorpNm", "_NmAndLctn", "_NtlData", "_OwnrEthnctyTp", "_OwnrEthnctyTpPrvddBy", "_OwnrTp", "_OwnrTpPrvddBy", "_PhneNb", "_PrvtData", "_SchmeAssgndId", "_URLAdr"]
	@property
	def AddtlAdr(self):
		return self._AddtlAdr

	@AddtlAdr.setter
	def AddtlAdr(self, value):
		self._AddtlAdr = value if type(value) != base_types.auto else self.make_default("AddtlAdr")

	@AddtlAdr.deleter
	def AddtlAdr(self):
		del self._AddtlAdr
		self._AddtlAdr = None

	@property
	def AddtlCtct(self):
		return self._AddtlCtct

	@AddtlCtct.setter
	def AddtlCtct(self, value):
		self._AddtlCtct = value if type(value) != base_types.auto else self.make_default("AddtlCtct")

	@AddtlCtct.deleter
	def AddtlCtct(self):
		del self._AddtlCtct
		self._AddtlCtct = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def BizNm(self):
		return self._BizNm

	@BizNm.setter
	def BizNm(self, value):
		self._BizNm = value if type(value) != base_types.auto else self.make_default("BizNm")

	@BizNm.deleter
	def BizNm(self):
		del self._BizNm
		self._BizNm = None

	@property
	def BizRegnId(self):
		return self._BizRegnId

	@BizRegnId.setter
	def BizRegnId(self, value):
		self._BizRegnId = value if type(value) != base_types.auto else self.make_default("BizRegnId")

	@BizRegnId.deleter
	def BizRegnId(self):
		del self._BizRegnId
		self._BizRegnId = None

	@property
	def BizRegnIdTp(self):
		return self._BizRegnIdTp

	@BizRegnIdTp.setter
	def BizRegnIdTp(self, value):
		self._BizRegnIdTp = value if type(value) != base_types.auto else self.make_default("BizRegnIdTp")

	@BizRegnIdTp.deleter
	def BizRegnIdTp(self):
		del self._BizRegnIdTp
		self._BizRegnIdTp = None

	@property
	def BizTp(self):
		return self._BizTp

	@BizTp.setter
	def BizTp(self, value):
		self._BizTp = value if type(value) != base_types.auto else self.make_default("BizTp")

	@BizTp.deleter
	def BizTp(self):
		del self._BizTp
		self._BizTp = None

	@property
	def BizTpPrvddBy(self):
		return self._BizTpPrvddBy

	@BizTpPrvddBy.setter
	def BizTpPrvddBy(self, value):
		self._BizTpPrvddBy = value if type(value) != base_types.auto else self.make_default("BizTpPrvddBy")

	@BizTpPrvddBy.deleter
	def BizTpPrvddBy(self):
		del self._BizTpPrvddBy
		self._BizTpPrvddBy = None

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if type(value) != base_types.auto else self.make_default("CertfctnTp")

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = None

	@property
	def CertfctnTpPrvddBy(self):
		return self._CertfctnTpPrvddBy

	@CertfctnTpPrvddBy.setter
	def CertfctnTpPrvddBy(self, value):
		self._CertfctnTpPrvddBy = value if type(value) != base_types.auto else self.make_default("CertfctnTpPrvddBy")

	@CertfctnTpPrvddBy.deleter
	def CertfctnTpPrvddBy(self):
		del self._CertfctnTpPrvddBy
		self._CertfctnTpPrvddBy = None

	@property
	def CorpTaxId(self):
		return self._CorpTaxId

	@CorpTaxId.setter
	def CorpTaxId(self, value):
		self._CorpTaxId = value if type(value) != base_types.auto else self.make_default("CorpTaxId")

	@CorpTaxId.deleter
	def CorpTaxId(self):
		del self._CorpTaxId
		self._CorpTaxId = None

	@property
	def CorpTaxIdTp(self):
		return self._CorpTaxIdTp

	@CorpTaxIdTp.setter
	def CorpTaxIdTp(self, value):
		self._CorpTaxIdTp = value if type(value) != base_types.auto else self.make_default("CorpTaxIdTp")

	@CorpTaxIdTp.deleter
	def CorpTaxIdTp(self):
		del self._CorpTaxIdTp
		self._CorpTaxIdTp = None

	@property
	def CstmrSvc(self):
		return self._CstmrSvc

	@CstmrSvc.setter
	def CstmrSvc(self, value):
		self._CstmrSvc = value if type(value) != base_types.auto else self.make_default("CstmrSvc")

	@CstmrSvc.deleter
	def CstmrSvc(self):
		del self._CstmrSvc
		self._CstmrSvc = None

	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if type(value) != base_types.auto else self.make_default("Email")

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if type(value) != base_types.auto else self.make_default("LclData")

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = None

	@property
	def LglCorpNm(self):
		return self._LglCorpNm

	@LglCorpNm.setter
	def LglCorpNm(self, value):
		self._LglCorpNm = value if type(value) != base_types.auto else self.make_default("LglCorpNm")

	@LglCorpNm.deleter
	def LglCorpNm(self):
		del self._LglCorpNm
		self._LglCorpNm = None

	@property
	def NmAndLctn(self):
		return self._NmAndLctn

	@NmAndLctn.setter
	def NmAndLctn(self, value):
		self._NmAndLctn = value if type(value) != base_types.auto else self.make_default("NmAndLctn")

	@NmAndLctn.deleter
	def NmAndLctn(self):
		del self._NmAndLctn
		self._NmAndLctn = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def OwnrEthnctyTp(self):
		return self._OwnrEthnctyTp

	@OwnrEthnctyTp.setter
	def OwnrEthnctyTp(self, value):
		self._OwnrEthnctyTp = value if type(value) != base_types.auto else self.make_default("OwnrEthnctyTp")

	@OwnrEthnctyTp.deleter
	def OwnrEthnctyTp(self):
		del self._OwnrEthnctyTp
		self._OwnrEthnctyTp = None

	@property
	def OwnrEthnctyTpPrvddBy(self):
		return self._OwnrEthnctyTpPrvddBy

	@OwnrEthnctyTpPrvddBy.setter
	def OwnrEthnctyTpPrvddBy(self, value):
		self._OwnrEthnctyTpPrvddBy = value if type(value) != base_types.auto else self.make_default("OwnrEthnctyTpPrvddBy")

	@OwnrEthnctyTpPrvddBy.deleter
	def OwnrEthnctyTpPrvddBy(self):
		del self._OwnrEthnctyTpPrvddBy
		self._OwnrEthnctyTpPrvddBy = None

	@property
	def OwnrTp(self):
		return self._OwnrTp

	@OwnrTp.setter
	def OwnrTp(self, value):
		self._OwnrTp = value if type(value) != base_types.auto else self.make_default("OwnrTp")

	@OwnrTp.deleter
	def OwnrTp(self):
		del self._OwnrTp
		self._OwnrTp = None

	@property
	def OwnrTpPrvddBy(self):
		return self._OwnrTpPrvddBy

	@OwnrTpPrvddBy.setter
	def OwnrTpPrvddBy(self, value):
		self._OwnrTpPrvddBy = value if type(value) != base_types.auto else self.make_default("OwnrTpPrvddBy")

	@OwnrTpPrvddBy.deleter
	def OwnrTpPrvddBy(self):
		del self._OwnrTpPrvddBy
		self._OwnrTpPrvddBy = None

	@property
	def PhneNb(self):
		return self._PhneNb

	@PhneNb.setter
	def PhneNb(self, value):
		self._PhneNb = value if type(value) != base_types.auto else self.make_default("PhneNb")

	@PhneNb.deleter
	def PhneNb(self):
		del self._PhneNb
		self._PhneNb = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def SchmeAssgndId(self):
		return self._SchmeAssgndId

	@SchmeAssgndId.setter
	def SchmeAssgndId(self, value):
		self._SchmeAssgndId = value if type(value) != base_types.auto else self.make_default("SchmeAssgndId")

	@SchmeAssgndId.deleter
	def SchmeAssgndId(self):
		del self._SchmeAssgndId
		self._SchmeAssgndId = None

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if type(value) != base_types.auto else self.make_default("URLAdr")

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlCtct', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizRegnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizRegnIdTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpTaxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpTaxIdTp', type=CorporateTaxType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrSvc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndLctn', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OwnrEthnctyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrEthnctyTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhneNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SchmeAssgndId', type=Max15AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

