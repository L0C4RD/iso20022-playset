# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import CustomerDeviceType2Code
from . import DeviceIdentification1
from . import ExternalDeviceOperatingSystemType1Code
from . import GeographicPointInDecimalDegrees
from . import ISO2ALanguageCode
from . import ISO3NumericCountryCode
from . import Max100Text
from . import Max256Text
from . import Max35Text
from . import Max70Text
from . import PhoneNumber

class CustomerDevice5(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_DvcId", "_DvcNm", "_DvcNmNrmlzd", "_Email", "_GeogcLctn", "_IPAdr", "_Lang", "_LctnCtryCd", "_Manfctr", "_ManfctrMdlId", "_OprgSysBld", "_OprgSysId", "_OprgSysTp", "_OprgSysVrsn", "_OthrOprgSysTp", "_OthrTp", "_Phne", "_Prvdr", "_Tp"]
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
	def DvcId(self):
		return self._DvcId

	@DvcId.setter
	def DvcId(self, value):
		self._DvcId = value if value is not None else base_types.UninitialisedField(self, 'DvcId', DeviceIdentification1, True)

	@DvcId.deleter
	def DvcId(self):
		del self._DvcId
		self._DvcId = base_types.UninitialisedField(self, 'DvcId', DeviceIdentification1, True)

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
	def OthrOprgSysTp(self):
		return self._OthrOprgSysTp

	@OthrOprgSysTp.setter
	def OthrOprgSysTp(self, value):
		self._OthrOprgSysTp = value if value is not None else base_types.UninitialisedField(self, 'OthrOprgSysTp', Max35Text, False)

	@OthrOprgSysTp.deleter
	def OthrOprgSysTp(self):
		del self._OthrOprgSysTp
		self._OthrOprgSysTp = base_types.UninitialisedField(self, 'OthrOprgSysTp', Max35Text, False)

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CustomerDeviceType2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CustomerDeviceType2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DvcId', type=DeviceIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DvcNm', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvcNmNrmlzd', type=Max100Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcLctn', type=GeographicPointInDecimalDegrees, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IPAdr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LctnCtryCd', type=ISO3NumericCountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Manfctr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ManfctrMdlId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgSysBld', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgSysId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgSysTp', type=ExternalDeviceOperatingSystemType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgSysVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrOprgSysTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Phne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prvdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CustomerDeviceType2Code, min=0, max=1, mutex_group=None, array=False),
	))