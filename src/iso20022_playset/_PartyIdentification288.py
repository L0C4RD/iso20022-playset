# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Address2
from . import CorporateTaxType1Code
from . import GeographicPointInDecimalDegrees
from . import LocalData11
from . import Max256Text
from . import Max35Text
from . import Max70Text
from . import Max99Text
from . import SponsoredMerchant3

class PartyIdentification288(base_types._BaseFieldType):

	__slots__ = ["_AddtlAdr", "_AddtlCtct", "_AddtlData", "_AddtlId", "_AddtlTxRefNb", "_Adr", "_Assgnr", "_BizTp", "_BizTpPrvddBy", "_CertfctnTp", "_CertfctnTpPrvddBy", "_CorpTaxId", "_CorpTaxIdTp", "_CstmrSvc", "_Email", "_GeogcLctn", "_Id", "_LclData", "_LglCorpNm", "_NmAndLctn", "_OwnrEthnctyTp", "_OwnrEthnctyTpPrvddBy", "_OwnrTp", "_OwnrTpPrvddBy", "_Phne", "_ShrtNm", "_SpnsrdMrchnt", "_TaxRegnId", "_URL"]
	@property
	def AddtlAdr(self):
		return self._AddtlAdr

	@AddtlAdr.setter
	def AddtlAdr(self, value):
		self._AddtlAdr = value if value is not None else base_types.UninitialisedField(self, 'AddtlAdr', Max256Text, False)

	@AddtlAdr.deleter
	def AddtlAdr(self):
		del self._AddtlAdr
		self._AddtlAdr = base_types.UninitialisedField(self, 'AddtlAdr', Max256Text, False)

	@property
	def AddtlCtct(self):
		return self._AddtlCtct

	@AddtlCtct.setter
	def AddtlCtct(self, value):
		self._AddtlCtct = value if value is not None else base_types.UninitialisedField(self, 'AddtlCtct', Max256Text, False)

	@AddtlCtct.deleter
	def AddtlCtct(self):
		del self._AddtlCtct
		self._AddtlCtct = base_types.UninitialisedField(self, 'AddtlCtct', Max256Text, False)

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if value is not None else base_types.UninitialisedField(self, 'AddtlId', AdditionalData1, True)

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = base_types.UninitialisedField(self, 'AddtlId', AdditionalData1, True)

	@property
	def AddtlTxRefNb(self):
		return self._AddtlTxRefNb

	@AddtlTxRefNb.setter
	def AddtlTxRefNb(self, value):
		self._AddtlTxRefNb = value if value is not None else base_types.UninitialisedField(self, 'AddtlTxRefNb', Max70Text, False)

	@AddtlTxRefNb.deleter
	def AddtlTxRefNb(self):
		del self._AddtlTxRefNb
		self._AddtlTxRefNb = base_types.UninitialisedField(self, 'AddtlTxRefNb', Max70Text, False)

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Address2, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Address2, False)

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if value is not None else base_types.UninitialisedField(self, 'Assgnr', Max35Text, False)

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = base_types.UninitialisedField(self, 'Assgnr', Max35Text, False)

	@property
	def BizTp(self):
		return self._BizTp

	@BizTp.setter
	def BizTp(self, value):
		self._BizTp = value if value is not None else base_types.UninitialisedField(self, 'BizTp', Max35Text, False)

	@BizTp.deleter
	def BizTp(self):
		del self._BizTp
		self._BizTp = base_types.UninitialisedField(self, 'BizTp', Max35Text, False)

	@property
	def BizTpPrvddBy(self):
		return self._BizTpPrvddBy

	@BizTpPrvddBy.setter
	def BizTpPrvddBy(self, value):
		self._BizTpPrvddBy = value if value is not None else base_types.UninitialisedField(self, 'BizTpPrvddBy', Max35Text, False)

	@BizTpPrvddBy.deleter
	def BizTpPrvddBy(self):
		del self._BizTpPrvddBy
		self._BizTpPrvddBy = base_types.UninitialisedField(self, 'BizTpPrvddBy', Max35Text, False)

	@property
	def CertfctnTp(self):
		return self._CertfctnTp

	@CertfctnTp.setter
	def CertfctnTp(self, value):
		self._CertfctnTp = value if value is not None else base_types.UninitialisedField(self, 'CertfctnTp', Max35Text, False)

	@CertfctnTp.deleter
	def CertfctnTp(self):
		del self._CertfctnTp
		self._CertfctnTp = base_types.UninitialisedField(self, 'CertfctnTp', Max35Text, False)

	@property
	def CertfctnTpPrvddBy(self):
		return self._CertfctnTpPrvddBy

	@CertfctnTpPrvddBy.setter
	def CertfctnTpPrvddBy(self, value):
		self._CertfctnTpPrvddBy = value if value is not None else base_types.UninitialisedField(self, 'CertfctnTpPrvddBy', Max35Text, False)

	@CertfctnTpPrvddBy.deleter
	def CertfctnTpPrvddBy(self):
		del self._CertfctnTpPrvddBy
		self._CertfctnTpPrvddBy = base_types.UninitialisedField(self, 'CertfctnTpPrvddBy', Max35Text, False)

	@property
	def CorpTaxId(self):
		return self._CorpTaxId

	@CorpTaxId.setter
	def CorpTaxId(self, value):
		self._CorpTaxId = value if value is not None else base_types.UninitialisedField(self, 'CorpTaxId', Max35Text, False)

	@CorpTaxId.deleter
	def CorpTaxId(self):
		del self._CorpTaxId
		self._CorpTaxId = base_types.UninitialisedField(self, 'CorpTaxId', Max35Text, False)

	@property
	def CorpTaxIdTp(self):
		return self._CorpTaxIdTp

	@CorpTaxIdTp.setter
	def CorpTaxIdTp(self, value):
		self._CorpTaxIdTp = value if value is not None else base_types.UninitialisedField(self, 'CorpTaxIdTp', CorporateTaxType1Code, False)

	@CorpTaxIdTp.deleter
	def CorpTaxIdTp(self):
		del self._CorpTaxIdTp
		self._CorpTaxIdTp = base_types.UninitialisedField(self, 'CorpTaxIdTp', CorporateTaxType1Code, False)

	@property
	def CstmrSvc(self):
		return self._CstmrSvc

	@CstmrSvc.setter
	def CstmrSvc(self, value):
		self._CstmrSvc = value if value is not None else base_types.UninitialisedField(self, 'CstmrSvc', Max35Text, False)

	@CstmrSvc.deleter
	def CstmrSvc(self):
		del self._CstmrSvc
		self._CstmrSvc = base_types.UninitialisedField(self, 'CstmrSvc', Max35Text, False)

	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if value is not None else base_types.UninitialisedField(self, 'Email', Max256Text, False)

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = base_types.UninitialisedField(self, 'Email', Max256Text, False)

	@property
	def GeogcLctn(self):
		return self._GeogcLctn

	@GeogcLctn.setter
	def GeogcLctn(self, value):
		self._GeogcLctn = value if value is not None else base_types.UninitialisedField(self, 'GeogcLctn', GeographicPointInDecimalDegrees, False)

	@GeogcLctn.deleter
	def GeogcLctn(self):
		del self._GeogcLctn
		self._GeogcLctn = base_types.UninitialisedField(self, 'GeogcLctn', GeographicPointInDecimalDegrees, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if value is not None else base_types.UninitialisedField(self, 'LclData', LocalData11, True)

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = base_types.UninitialisedField(self, 'LclData', LocalData11, True)

	@property
	def LglCorpNm(self):
		return self._LglCorpNm

	@LglCorpNm.setter
	def LglCorpNm(self, value):
		self._LglCorpNm = value if value is not None else base_types.UninitialisedField(self, 'LglCorpNm', Max99Text, False)

	@LglCorpNm.deleter
	def LglCorpNm(self):
		del self._LglCorpNm
		self._LglCorpNm = base_types.UninitialisedField(self, 'LglCorpNm', Max99Text, False)

	@property
	def NmAndLctn(self):
		return self._NmAndLctn

	@NmAndLctn.setter
	def NmAndLctn(self, value):
		self._NmAndLctn = value if value is not None else base_types.UninitialisedField(self, 'NmAndLctn', Max99Text, False)

	@NmAndLctn.deleter
	def NmAndLctn(self):
		del self._NmAndLctn
		self._NmAndLctn = base_types.UninitialisedField(self, 'NmAndLctn', Max99Text, False)

	@property
	def OwnrEthnctyTp(self):
		return self._OwnrEthnctyTp

	@OwnrEthnctyTp.setter
	def OwnrEthnctyTp(self, value):
		self._OwnrEthnctyTp = value if value is not None else base_types.UninitialisedField(self, 'OwnrEthnctyTp', Max35Text, False)

	@OwnrEthnctyTp.deleter
	def OwnrEthnctyTp(self):
		del self._OwnrEthnctyTp
		self._OwnrEthnctyTp = base_types.UninitialisedField(self, 'OwnrEthnctyTp', Max35Text, False)

	@property
	def OwnrEthnctyTpPrvddBy(self):
		return self._OwnrEthnctyTpPrvddBy

	@OwnrEthnctyTpPrvddBy.setter
	def OwnrEthnctyTpPrvddBy(self, value):
		self._OwnrEthnctyTpPrvddBy = value if value is not None else base_types.UninitialisedField(self, 'OwnrEthnctyTpPrvddBy', Max35Text, False)

	@OwnrEthnctyTpPrvddBy.deleter
	def OwnrEthnctyTpPrvddBy(self):
		del self._OwnrEthnctyTpPrvddBy
		self._OwnrEthnctyTpPrvddBy = base_types.UninitialisedField(self, 'OwnrEthnctyTpPrvddBy', Max35Text, False)

	@property
	def OwnrTp(self):
		return self._OwnrTp

	@OwnrTp.setter
	def OwnrTp(self, value):
		self._OwnrTp = value if value is not None else base_types.UninitialisedField(self, 'OwnrTp', Max35Text, False)

	@OwnrTp.deleter
	def OwnrTp(self):
		del self._OwnrTp
		self._OwnrTp = base_types.UninitialisedField(self, 'OwnrTp', Max35Text, False)

	@property
	def OwnrTpPrvddBy(self):
		return self._OwnrTpPrvddBy

	@OwnrTpPrvddBy.setter
	def OwnrTpPrvddBy(self, value):
		self._OwnrTpPrvddBy = value if value is not None else base_types.UninitialisedField(self, 'OwnrTpPrvddBy', Max35Text, False)

	@OwnrTpPrvddBy.deleter
	def OwnrTpPrvddBy(self):
		del self._OwnrTpPrvddBy
		self._OwnrTpPrvddBy = base_types.UninitialisedField(self, 'OwnrTpPrvddBy', Max35Text, False)

	@property
	def Phne(self):
		return self._Phne

	@Phne.setter
	def Phne(self, value):
		self._Phne = value if value is not None else base_types.UninitialisedField(self, 'Phne', Max35Text, False)

	@Phne.deleter
	def Phne(self):
		del self._Phne
		self._Phne = base_types.UninitialisedField(self, 'Phne', Max35Text, False)

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if value is not None else base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = base_types.UninitialisedField(self, 'ShrtNm', Max35Text, False)

	@property
	def SpnsrdMrchnt(self):
		return self._SpnsrdMrchnt

	@SpnsrdMrchnt.setter
	def SpnsrdMrchnt(self, value):
		self._SpnsrdMrchnt = value if value is not None else base_types.UninitialisedField(self, 'SpnsrdMrchnt', SponsoredMerchant3, True)

	@SpnsrdMrchnt.deleter
	def SpnsrdMrchnt(self):
		del self._SpnsrdMrchnt
		self._SpnsrdMrchnt = base_types.UninitialisedField(self, 'SpnsrdMrchnt', SponsoredMerchant3, True)

	@property
	def TaxRegnId(self):
		return self._TaxRegnId

	@TaxRegnId.setter
	def TaxRegnId(self, value):
		self._TaxRegnId = value if value is not None else base_types.UninitialisedField(self, 'TaxRegnId', Max35Text, False)

	@TaxRegnId.deleter
	def TaxRegnId(self):
		del self._TaxRegnId
		self._TaxRegnId = base_types.UninitialisedField(self, 'TaxRegnId', Max35Text, False)

	@property
	def URL(self):
		return self._URL

	@URL.setter
	def URL(self, value):
		self._URL = value if value is not None else base_types.UninitialisedField(self, 'URL', Max256Text, False)

	@URL.deleter
	def URL(self):
		del self._URL
		self._URL = base_types.UninitialisedField(self, 'URL', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlCtct', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlId', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlTxRefNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertfctnTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpTaxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpTaxIdTp', type=CorporateTaxType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrSvc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcLctn', type=GeographicPointInDecimalDegrees, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LglCorpNm', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndLctn', type=Max99Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrEthnctyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrEthnctyTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OwnrTpPrvddBy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Phne', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpnsrdMrchnt', type=SponsoredMerchant3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxRegnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URL', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))