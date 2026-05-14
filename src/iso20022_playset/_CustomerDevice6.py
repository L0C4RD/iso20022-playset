# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._DeviceIdentification2 import DeviceIdentification2
from ._ExternalCustomerDeviceType1Code import ExternalCustomerDeviceType1Code
from ._ExternalDeviceOperatingSystemType1Code import ExternalDeviceOperatingSystemType1Code
from ._GeographicPointInDecimalDegreesText import GeographicPointInDecimalDegreesText
from ._ISO2ALanguageCode import ISO2ALanguageCode
from ._ISO3NumericCountryCode import ISO3NumericCountryCode
from ._Max100Text import Max100Text
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._PhoneNumber import PhoneNumber

class CustomerDevice6(base_types._BaseFieldType):

	__slots__ = ["_DvcId", "_DvcNm", "_DvcNmNrmlzd", "_DvcTmZone", "_DvcTmZoneSrc", "_Email", "_GeogcLctn", "_GeogcLctnSrc", "_IPAdr", "_Lang", "_LctnCtryCd", "_Manfctr", "_ManfctrMdlId", "_NtlData", "_OprgSysBld", "_OprgSysId", "_OprgSysTp", "_OprgSysVrsn", "_Phne", "_Prvdr", "_PrvtData", "_Tp"]
	@property
	def DvcId(self):
		return self._DvcId

	@DvcId.setter
	def DvcId(self, value):
		self._DvcId = value if type(value) != base_types.auto else self.make_default("DvcId")

	@DvcId.deleter
	def DvcId(self):
		del self._DvcId
		self._DvcId = None

	@property
	def DvcNm(self):
		return self._DvcNm

	@DvcNm.setter
	def DvcNm(self, value):
		self._DvcNm = value if type(value) != base_types.auto else self.make_default("DvcNm")

	@DvcNm.deleter
	def DvcNm(self):
		del self._DvcNm
		self._DvcNm = None

	@property
	def DvcNmNrmlzd(self):
		return self._DvcNmNrmlzd

	@DvcNmNrmlzd.setter
	def DvcNmNrmlzd(self, value):
		self._DvcNmNrmlzd = value if type(value) != base_types.auto else self.make_default("DvcNmNrmlzd")

	@DvcNmNrmlzd.deleter
	def DvcNmNrmlzd(self):
		del self._DvcNmNrmlzd
		self._DvcNmNrmlzd = None

	@property
	def DvcTmZone(self):
		return self._DvcTmZone

	@DvcTmZone.setter
	def DvcTmZone(self, value):
		self._DvcTmZone = value if type(value) != base_types.auto else self.make_default("DvcTmZone")

	@DvcTmZone.deleter
	def DvcTmZone(self):
		del self._DvcTmZone
		self._DvcTmZone = None

	@property
	def DvcTmZoneSrc(self):
		return self._DvcTmZoneSrc

	@DvcTmZoneSrc.setter
	def DvcTmZoneSrc(self, value):
		self._DvcTmZoneSrc = value if type(value) != base_types.auto else self.make_default("DvcTmZoneSrc")

	@DvcTmZoneSrc.deleter
	def DvcTmZoneSrc(self):
		del self._DvcTmZoneSrc
		self._DvcTmZoneSrc = None

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
	def GeogcLctn(self):
		return self._GeogcLctn

	@GeogcLctn.setter
	def GeogcLctn(self, value):
		self._GeogcLctn = value if type(value) != base_types.auto else self.make_default("GeogcLctn")

	@GeogcLctn.deleter
	def GeogcLctn(self):
		del self._GeogcLctn
		self._GeogcLctn = None

	@property
	def GeogcLctnSrc(self):
		return self._GeogcLctnSrc

	@GeogcLctnSrc.setter
	def GeogcLctnSrc(self, value):
		self._GeogcLctnSrc = value if type(value) != base_types.auto else self.make_default("GeogcLctnSrc")

	@GeogcLctnSrc.deleter
	def GeogcLctnSrc(self):
		del self._GeogcLctnSrc
		self._GeogcLctnSrc = None

	@property
	def IPAdr(self):
		return self._IPAdr

	@IPAdr.setter
	def IPAdr(self, value):
		self._IPAdr = value if type(value) != base_types.auto else self.make_default("IPAdr")

	@IPAdr.deleter
	def IPAdr(self):
		del self._IPAdr
		self._IPAdr = None

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != base_types.auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def LctnCtryCd(self):
		return self._LctnCtryCd

	@LctnCtryCd.setter
	def LctnCtryCd(self, value):
		self._LctnCtryCd = value if type(value) != base_types.auto else self.make_default("LctnCtryCd")

	@LctnCtryCd.deleter
	def LctnCtryCd(self):
		del self._LctnCtryCd
		self._LctnCtryCd = None

	@property
	def Manfctr(self):
		return self._Manfctr

	@Manfctr.setter
	def Manfctr(self, value):
		self._Manfctr = value if type(value) != base_types.auto else self.make_default("Manfctr")

	@Manfctr.deleter
	def Manfctr(self):
		del self._Manfctr
		self._Manfctr = None

	@property
	def ManfctrMdlId(self):
		return self._ManfctrMdlId

	@ManfctrMdlId.setter
	def ManfctrMdlId(self, value):
		self._ManfctrMdlId = value if type(value) != base_types.auto else self.make_default("ManfctrMdlId")

	@ManfctrMdlId.deleter
	def ManfctrMdlId(self):
		del self._ManfctrMdlId
		self._ManfctrMdlId = None

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
	def OprgSysBld(self):
		return self._OprgSysBld

	@OprgSysBld.setter
	def OprgSysBld(self, value):
		self._OprgSysBld = value if type(value) != base_types.auto else self.make_default("OprgSysBld")

	@OprgSysBld.deleter
	def OprgSysBld(self):
		del self._OprgSysBld
		self._OprgSysBld = None

	@property
	def OprgSysId(self):
		return self._OprgSysId

	@OprgSysId.setter
	def OprgSysId(self, value):
		self._OprgSysId = value if type(value) != base_types.auto else self.make_default("OprgSysId")

	@OprgSysId.deleter
	def OprgSysId(self):
		del self._OprgSysId
		self._OprgSysId = None

	@property
	def OprgSysTp(self):
		return self._OprgSysTp

	@OprgSysTp.setter
	def OprgSysTp(self, value):
		self._OprgSysTp = value if type(value) != base_types.auto else self.make_default("OprgSysTp")

	@OprgSysTp.deleter
	def OprgSysTp(self):
		del self._OprgSysTp
		self._OprgSysTp = None

	@property
	def OprgSysVrsn(self):
		return self._OprgSysVrsn

	@OprgSysVrsn.setter
	def OprgSysVrsn(self, value):
		self._OprgSysVrsn = value if type(value) != base_types.auto else self.make_default("OprgSysVrsn")

	@OprgSysVrsn.deleter
	def OprgSysVrsn(self):
		del self._OprgSysVrsn
		self._OprgSysVrsn = None

	@property
	def Phne(self):
		return self._Phne

	@Phne.setter
	def Phne(self, value):
		self._Phne = value if type(value) != base_types.auto else self.make_default("Phne")

	@Phne.deleter
	def Phne(self):
		del self._Phne
		self._Phne = None

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if type(value) != base_types.auto else self.make_default("Prvdr")

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = None

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DvcId', type=DeviceIdentification2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DvcNm', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcNmNrmlzd', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcTmZone', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcTmZoneSrc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcLctn', type=GeographicPointInDecimalDegreesText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcLctnSrc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IPAdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LctnCtryCd', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Manfctr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ManfctrMdlId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OprgSysBld', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgSysId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgSysTp', type=ExternalDeviceOperatingSystemType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgSysVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Phne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=ExternalCustomerDeviceType1Code, min=0, max=1, mutex_group=None, array=False),
	))