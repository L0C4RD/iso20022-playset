# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import Address4
from . import CorporateTaxType1Code
from . import LocalData19
from . import Max15AlphaNumericText
from . import Max256Text
from . import Max35Text
from . import Max99Text

class AcceptorData3(base_types._BaseFieldType):

	__slots__ = ["_AddtlAdr", "_AddtlCtct", "_Adr", "_BizNm", "_BizRegnId", "_BizRegnIdTp", "_BizTp", "_BizTpPrvddBy", "_CertfctnTp", "_CertfctnTpPrvddBy", "_CorpTaxId", "_CorpTaxIdTp", "_CstmrSvc", "_Email", "_Id", "_LclData", "_LglCorpNm", "_NmAndLctn", "_NtlData", "_OwnrEthnctyTp", "_OwnrEthnctyTpPrvddBy", "_OwnrTp", "_OwnrTpPrvddBy", "_PhneNb", "_PrvtData", "_SchmeAssgndId", "_URLAdr"]
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
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Address4, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Address4, False)

	@property
	def BizNm(self):
		return self._BizNm

	@BizNm.setter
	def BizNm(self, value):
		self._BizNm = value if value is not None else base_types.UninitialisedField(self, 'BizNm', Max35Text, False)

	@BizNm.deleter
	def BizNm(self):
		del self._BizNm
		self._BizNm = base_types.UninitialisedField(self, 'BizNm', Max35Text, False)

	@property
	def BizRegnId(self):
		return self._BizRegnId

	@BizRegnId.setter
	def BizRegnId(self, value):
		self._BizRegnId = value if value is not None else base_types.UninitialisedField(self, 'BizRegnId', Max35Text, False)

	@BizRegnId.deleter
	def BizRegnId(self):
		del self._BizRegnId
		self._BizRegnId = base_types.UninitialisedField(self, 'BizRegnId', Max35Text, False)

	@property
	def BizRegnIdTp(self):
		return self._BizRegnIdTp

	@BizRegnIdTp.setter
	def BizRegnIdTp(self, value):
		self._BizRegnIdTp = value if value is not None else base_types.UninitialisedField(self, 'BizRegnIdTp', Max35Text, False)

	@BizRegnIdTp.deleter
	def BizRegnIdTp(self):
		del self._BizRegnIdTp
		self._BizRegnIdTp = base_types.UninitialisedField(self, 'BizRegnIdTp', Max35Text, False)

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
		self._LclData = value if value is not None else base_types.UninitialisedField(self, 'LclData', LocalData19, False)

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = base_types.UninitialisedField(self, 'LclData', LocalData19, False)

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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

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
	def PhneNb(self):
		return self._PhneNb

	@PhneNb.setter
	def PhneNb(self, value):
		self._PhneNb = value if value is not None else base_types.UninitialisedField(self, 'PhneNb', Max35Text, False)

	@PhneNb.deleter
	def PhneNb(self):
		del self._PhneNb
		self._PhneNb = base_types.UninitialisedField(self, 'PhneNb', Max35Text, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def SchmeAssgndId(self):
		return self._SchmeAssgndId

	@SchmeAssgndId.setter
	def SchmeAssgndId(self, value):
		self._SchmeAssgndId = value if value is not None else base_types.UninitialisedField(self, 'SchmeAssgndId', Max15AlphaNumericText, False)

	@SchmeAssgndId.deleter
	def SchmeAssgndId(self):
		del self._SchmeAssgndId
		self._SchmeAssgndId = base_types.UninitialisedField(self, 'SchmeAssgndId', Max15AlphaNumericText, False)

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if value is not None else base_types.UninitialisedField(self, 'URLAdr', Max256Text, False)

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = base_types.UninitialisedField(self, 'URLAdr', Max256Text, False)

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