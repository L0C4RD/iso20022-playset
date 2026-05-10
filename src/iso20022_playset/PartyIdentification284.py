from . import base_types
import Max256Text
import Address2
import Max99Text
import Max35Text
import CorporateTaxType1Code
import LocalData11
import GeographicPointInDecimalDegrees
import AdditionalData1
import ISO3NumericCountryCode

class PartyIdentification284(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Ctry", "_OwnrTp", "_AddtlAdr", "_URLAdr", "_LglCorpNm", "_Email", "_AddtlData", "_AddtlId", "_CorpTaxIdTp", "_LclData", "_BizTpPrvddBy", "_CstmrSvc", "_CorpTaxId", "_GeogcLctn", "_AddtlCtct", "_Adr", "_BizTp", "_PhneNb", "_NmAndLctn", "_OwnrEthnctyTpPrvddBy", "_OwnrEthnctyTp", "_CertfctnTp", "_Assgnr", "_TaxRegnId", "_OwnrTpPrvddBy", "_ShrtNm", "_CertfctnTpPrvddBy"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def OwnrTp(self):
		return self._OwnrTp

	@OwnrTp.setter
	def OwnrTp(self, value):
		self._OwnrTp = value if type(value) != auto else self.make_default("OwnrTp")

	@OwnrTp.deleter
	def OwnrTp(self):
		del self._OwnrTp
		self._OwnrTp = None

	@property
	def AddtlAdr(self):
		return self._AddtlAdr

	@AddtlAdr.setter
	def AddtlAdr(self, value):
		self._AddtlAdr = value if type(value) != auto else self.make_default("AddtlAdr")

	@AddtlAdr.deleter
	def AddtlAdr(self):
		del self._AddtlAdr
		self._AddtlAdr = None

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if type(value) != auto else self.make_default("URLAdr")

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = None

	@property
	def LglCorpNm(self):
		return self._LglCorpNm

	@LglCorpNm.setter
	def LglCorpNm(self, value):
		self._LglCorpNm = value if type(value) != auto else self.make_default("LglCorpNm")

	@LglCorpNm.deleter
	def LglCorpNm(self):
		del self._LglCorpNm
		self._LglCorpNm = None

	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if type(value) != auto else self.make_default("Email")

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if type(value) != auto else self.make_default("AddtlId")

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = None

	@property
	def CorpTaxIdTp(self):
		return self._CorpTaxIdTp

	@CorpTaxIdTp.setter
	def CorpTaxIdTp(self, value):
		self._CorpTaxIdTp = value if type(value) != auto else self.make_default("CorpTaxIdTp")

	@CorpTaxIdTp.deleter
	def CorpTaxIdTp(self):
		del self._CorpTaxIdTp
		self._CorpTaxIdTp = None

	@property
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if type(value) != auto else self.make_default("LclData")

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = None

	@property
	def BizTpPrvddBy(self):
		return self._BizTpPrvddBy

	@BizTpPrvddBy.setter
	def BizTpPrvddBy(self, value):
		self._BizTpPrvddBy = value if type(value) != auto else self.make_default("BizTpPrvddBy")

	@BizTpPrvddBy.deleter
	def BizTpPrvddBy(self):
		del self._BizTpPrvddBy
		self._BizTpPrvddBy = None

	@property
	def CstmrSvc(self):
		return self._CstmrSvc

	@CstmrSvc.setter
	def CstmrSvc(self, value):
		self._CstmrSvc = value if type(value) != auto else self.make_default("CstmrSvc")

	@CstmrSvc.deleter
	def CstmrSvc(self):
		del self._CstmrSvc
		self._CstmrSvc = None

	@property
	def CorpTaxId(self):
		return self._CorpTaxId

	@CorpTaxId.setter
	def CorpTaxId(self, value):
		self._CorpTaxId = value if type(value) != auto else self.make_default("CorpTaxId")

	@CorpTaxId.deleter
	def CorpTaxId(self):
		del self._CorpTaxId
		self._CorpTaxId = None

	@property
	def GeogcLctn(self):
		return self._GeogcLctn

	@GeogcLctn.setter
	def GeogcLctn(self, value):
		self._GeogcLctn = value if type(value) != auto else self.make_default("GeogcLctn")

	@GeogcLctn.deleter
	def GeogcLctn(self):
		del self._GeogcLctn
		self._GeogcLctn = None

	@property
	def AddtlCtct(self):
		return self._AddtlCtct

	@AddtlCtct.setter
	def AddtlCtct(self, value):
		self._AddtlCtct = value if type(value) != auto else self.make_default("AddtlCtct")

	@AddtlCtct.deleter
	def AddtlCtct(self):
		del self._AddtlCtct
		self._AddtlCtct = None

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def BizTp(self):
		return self._BizTp

	@BizTp.setter
	def BizTp(self, value):
		self._BizTp = value if type(value) != auto else self.make_default("BizTp")

	@BizTp.deleter
	def BizTp(self):
		del self._BizTp
		self._BizTp = None

	@property
	def PhneNb(self):
		return self._PhneNb

	@PhneNb.setter
	def PhneNb(self, value):
		self._PhneNb = value if type(value) != auto else self.make_default("PhneNb")

	@PhneNb.deleter
	def PhneNb(self):
		del self._PhneNb
		self._PhneNb = None

	@property
	def NmAndLctn(self):
		return self._NmAndLctn

	@NmAndLctn.setter
	def NmAndLctn(self, value):
		self._NmAndLctn = value if type(value) != auto else self.make_default("NmAndLctn")

	@NmAndLctn.deleter
	def NmAndLctn(self):
		del self._NmAndLctn
		self._NmAndLctn = None

	@property
	def OwnrEthnctyTpPrvddBy(self):
		return self._OwnrEthnctyTpPrvddBy

	@OwnrEthnctyTpPrvddBy.setter
	def OwnrEthnctyTpPrvddBy(self, value):
		self._OwnrEthnctyTpPrvddBy = value if type(value) != auto else self.make_default("OwnrEthnctyTpPrvddBy")

	@OwnrEthnctyTpPrvddBy.deleter
	def OwnrEthnctyTpPrvddBy(self):
		del self._OwnrEthnctyTpPrvddBy
		self._OwnrEthnctyTpPrvddBy = None

	@property
	def OwnrEthnctyTp(self):
		return self._OwnrEthnctyTp

	@OwnrEthnctyTp.setter
	def OwnrEthnctyTp(self, value):
		self._OwnrEthnctyTp = value if type(value) != auto else self.make_default("OwnrEthnctyTp")

	@OwnrEthnctyTp.deleter
	def OwnrEthnctyTp(self):
		del self._OwnrEthnctyTp
		self._OwnrEthnctyTp = None

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if type(value) != auto else self.make_default("CertfctnTp")

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = None

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	@property
	def TaxRegnId(self):
		return self._TaxRegnId

	@TaxRegnId.setter
	def TaxRegnId(self, value):
		self._TaxRegnId = value if type(value) != auto else self.make_default("TaxRegnId")

	@TaxRegnId.deleter
	def TaxRegnId(self):
		del self._TaxRegnId
		self._TaxRegnId = None

	@property
	def OwnrTpPrvddBy(self):
		return self._OwnrTpPrvddBy

	@OwnrTpPrvddBy.setter
	def OwnrTpPrvddBy(self, value):
		self._OwnrTpPrvddBy = value if type(value) != auto else self.make_default("OwnrTpPrvddBy")

	@OwnrTpPrvddBy.deleter
	def OwnrTpPrvddBy(self):
		del self._OwnrTpPrvddBy
		self._OwnrTpPrvddBy = None

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

	@property
	def CertfctnTpPrvddBy(self):
		return self._CertfctnTpPrvddBy

	@CertfctnTpPrvddBy.setter
	def CertfctnTpPrvddBy(self, value):
		self._CertfctnTpPrvddBy = value if type(value) != auto else self.make_default("CertfctnTpPrvddBy")

	@CertfctnTpPrvddBy.deleter
	def CertfctnTpPrvddBy(self):
		del self._CertfctnTpPrvddBy
		self._CertfctnTpPrvddBy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlId', type=AdditionalData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpTaxIdTp', type=CorporateTaxType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrSvc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpTaxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcLctn', type=GeographicPointInDecimalDegrees, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlCtct', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhneNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndLctn', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrEthnctyTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrEthnctyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRegnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

