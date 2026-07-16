# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import DeviceIdentification2
from . import ExternalCustomerDeviceType1Code
from . import ExternalDeviceOperatingSystemType1Code
from . import GeographicPointInDecimalDegreesText
from . import ISO2ALanguageCode
from . import ISO3NumericCountryCode
from . import Max100Text
from . import Max256Text
from . import Max35Text
from . import Max70Text
from . import PhoneNumber

class CustomerDevice6(base_types._BaseFieldType):

	__slots__ = ["_DvcId", "_DvcNm", "_DvcNmNrmlzd", "_DvcTmZone", "_DvcTmZoneSrc", "_Email", "_GeogcLctn", "_GeogcLctnSrc", "_IPAdr", "_Lang", "_LctnCtryCd", "_Manfctr", "_ManfctrMdlId", "_NtlData", "_OprgSysBld", "_OprgSysId", "_OprgSysTp", "_OprgSysVrsn", "_Phne", "_Prvdr", "_PrvtData", "_Tp"]
	@property
	def DvcId(self):
		return self._DvcId

	@DvcId.setter
	def DvcId(self, value):
		self._DvcId = value if value is not None else base_types.UninitialisedField(self, 'DvcId', DeviceIdentification2, True)

	@DvcId.deleter
	def DvcId(self):
		del self._DvcId
		self._DvcId = base_types.UninitialisedField(self, 'DvcId', DeviceIdentification2, True)

	@property
	def DvcNm(self):
		return self._DvcNm

	@DvcNm.setter
	def DvcNm(self, value):
		self._DvcNm = value if value is not None else base_types.UninitialisedField(self, 'DvcNm', Max100Text, False)

	@DvcNm.deleter
	def DvcNm(self):
		del self._DvcNm
		self._DvcNm = base_types.UninitialisedField(self, 'DvcNm', Max100Text, False)

	@property
	def DvcNmNrmlzd(self):
		return self._DvcNmNrmlzd

	@DvcNmNrmlzd.setter
	def DvcNmNrmlzd(self, value):
		self._DvcNmNrmlzd = value if value is not None else base_types.UninitialisedField(self, 'DvcNmNrmlzd', Max100Text, False)

	@DvcNmNrmlzd.deleter
	def DvcNmNrmlzd(self):
		del self._DvcNmNrmlzd
		self._DvcNmNrmlzd = base_types.UninitialisedField(self, 'DvcNmNrmlzd', Max100Text, False)

	@property
	def DvcTmZone(self):
		return self._DvcTmZone

	@DvcTmZone.setter
	def DvcTmZone(self, value):
		self._DvcTmZone = value if value is not None else base_types.UninitialisedField(self, 'DvcTmZone', Max70Text, False)

	@DvcTmZone.deleter
	def DvcTmZone(self):
		del self._DvcTmZone
		self._DvcTmZone = base_types.UninitialisedField(self, 'DvcTmZone', Max70Text, False)

	@property
	def DvcTmZoneSrc(self):
		return self._DvcTmZoneSrc

	@DvcTmZoneSrc.setter
	def DvcTmZoneSrc(self, value):
		self._DvcTmZoneSrc = value if value is not None else base_types.UninitialisedField(self, 'DvcTmZoneSrc', Max35Text, False)

	@DvcTmZoneSrc.deleter
	def DvcTmZoneSrc(self):
		del self._DvcTmZoneSrc
		self._DvcTmZoneSrc = base_types.UninitialisedField(self, 'DvcTmZoneSrc', Max35Text, False)

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
		self._GeogcLctn = value if value is not None else base_types.UninitialisedField(self, 'GeogcLctn', GeographicPointInDecimalDegreesText, False)

	@GeogcLctn.deleter
	def GeogcLctn(self):
		del self._GeogcLctn
		self._GeogcLctn = base_types.UninitialisedField(self, 'GeogcLctn', GeographicPointInDecimalDegreesText, False)

	@property
	def GeogcLctnSrc(self):
		return self._GeogcLctnSrc

	@GeogcLctnSrc.setter
	def GeogcLctnSrc(self, value):
		self._GeogcLctnSrc = value if value is not None else base_types.UninitialisedField(self, 'GeogcLctnSrc', Max35Text, False)

	@GeogcLctnSrc.deleter
	def GeogcLctnSrc(self):
		del self._GeogcLctnSrc
		self._GeogcLctnSrc = base_types.UninitialisedField(self, 'GeogcLctnSrc', Max35Text, False)

	@property
	def IPAdr(self):
		return self._IPAdr

	@IPAdr.setter
	def IPAdr(self, value):
		self._IPAdr = value if value is not None else base_types.UninitialisedField(self, 'IPAdr', Max70Text, False)

	@IPAdr.deleter
	def IPAdr(self):
		del self._IPAdr
		self._IPAdr = base_types.UninitialisedField(self, 'IPAdr', Max70Text, False)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', ISO2ALanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', ISO2ALanguageCode, False)

	@property
	def LctnCtryCd(self):
		return self._LctnCtryCd

	@LctnCtryCd.setter
	def LctnCtryCd(self, value):
		self._LctnCtryCd = value if value is not None else base_types.UninitialisedField(self, 'LctnCtryCd', ISO3NumericCountryCode, False)

	@LctnCtryCd.deleter
	def LctnCtryCd(self):
		del self._LctnCtryCd
		self._LctnCtryCd = base_types.UninitialisedField(self, 'LctnCtryCd', ISO3NumericCountryCode, False)

	@property
	def Manfctr(self):
		return self._Manfctr

	@Manfctr.setter
	def Manfctr(self, value):
		self._Manfctr = value if value is not None else base_types.UninitialisedField(self, 'Manfctr', Max70Text, False)

	@Manfctr.deleter
	def Manfctr(self):
		del self._Manfctr
		self._Manfctr = base_types.UninitialisedField(self, 'Manfctr', Max70Text, False)

	@property
	def ManfctrMdlId(self):
		return self._ManfctrMdlId

	@ManfctrMdlId.setter
	def ManfctrMdlId(self, value):
		self._ManfctrMdlId = value if value is not None else base_types.UninitialisedField(self, 'ManfctrMdlId', Max70Text, False)

	@ManfctrMdlId.deleter
	def ManfctrMdlId(self):
		del self._ManfctrMdlId
		self._ManfctrMdlId = base_types.UninitialisedField(self, 'ManfctrMdlId', Max70Text, False)

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
	def OprgSysBld(self):
		return self._OprgSysBld

	@OprgSysBld.setter
	def OprgSysBld(self, value):
		self._OprgSysBld = value if value is not None else base_types.UninitialisedField(self, 'OprgSysBld', Max70Text, False)

	@OprgSysBld.deleter
	def OprgSysBld(self):
		del self._OprgSysBld
		self._OprgSysBld = base_types.UninitialisedField(self, 'OprgSysBld', Max70Text, False)

	@property
	def OprgSysId(self):
		return self._OprgSysId

	@OprgSysId.setter
	def OprgSysId(self, value):
		self._OprgSysId = value if value is not None else base_types.UninitialisedField(self, 'OprgSysId', Max70Text, False)

	@OprgSysId.deleter
	def OprgSysId(self):
		del self._OprgSysId
		self._OprgSysId = base_types.UninitialisedField(self, 'OprgSysId', Max70Text, False)

	@property
	def OprgSysTp(self):
		return self._OprgSysTp

	@OprgSysTp.setter
	def OprgSysTp(self, value):
		self._OprgSysTp = value if value is not None else base_types.UninitialisedField(self, 'OprgSysTp', ExternalDeviceOperatingSystemType1Code, False)

	@OprgSysTp.deleter
	def OprgSysTp(self):
		del self._OprgSysTp
		self._OprgSysTp = base_types.UninitialisedField(self, 'OprgSysTp', ExternalDeviceOperatingSystemType1Code, False)

	@property
	def OprgSysVrsn(self):
		return self._OprgSysVrsn

	@OprgSysVrsn.setter
	def OprgSysVrsn(self, value):
		self._OprgSysVrsn = value if value is not None else base_types.UninitialisedField(self, 'OprgSysVrsn', Max35Text, False)

	@OprgSysVrsn.deleter
	def OprgSysVrsn(self):
		del self._OprgSysVrsn
		self._OprgSysVrsn = base_types.UninitialisedField(self, 'OprgSysVrsn', Max35Text, False)

	@property
	def Phne(self):
		return self._Phne

	@Phne.setter
	def Phne(self, value):
		self._Phne = value if value is not None else base_types.UninitialisedField(self, 'Phne', PhoneNumber, False)

	@Phne.deleter
	def Phne(self):
		del self._Phne
		self._Phne = base_types.UninitialisedField(self, 'Phne', PhoneNumber, False)

	@property
	def Prvdr(self):
		return self._Prvdr

	@Prvdr.setter
	def Prvdr(self, value):
		self._Prvdr = value if value is not None else base_types.UninitialisedField(self, 'Prvdr', Max35Text, False)

	@Prvdr.deleter
	def Prvdr(self):
		del self._Prvdr
		self._Prvdr = base_types.UninitialisedField(self, 'Prvdr', Max35Text, False)

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ExternalCustomerDeviceType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ExternalCustomerDeviceType1Code, False)

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