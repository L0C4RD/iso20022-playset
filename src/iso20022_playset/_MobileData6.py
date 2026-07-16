# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContentInformationType40
from . import Geolocation1
from . import Max35Text
from . import Min2Max3AlphaText
from . import Min2Max3NumericText
from . import SensitiveMobileData1

class MobileData6(base_types._BaseFieldType):

	__slots__ = ["_Glctn", "_MobCtryCd", "_MobMskdMSISDN", "_MobNtwkCd", "_PrtctdMobData", "_SnstvMobData"]
	@property
	def Glctn(self):
		return self._Glctn

	@Glctn.setter
	def Glctn(self, value):
		self._Glctn = value if value is not None else base_types.UninitialisedField(self, 'Glctn', Geolocation1, False)

	@Glctn.deleter
	def Glctn(self):
		del self._Glctn
		self._Glctn = base_types.UninitialisedField(self, 'Glctn', Geolocation1, False)

	@property
	def MobCtryCd(self):
		return self._MobCtryCd

	@MobCtryCd.setter
	def MobCtryCd(self, value):
		self._MobCtryCd = value if value is not None else base_types.UninitialisedField(self, 'MobCtryCd', Min2Max3AlphaText, False)

	@MobCtryCd.deleter
	def MobCtryCd(self):
		del self._MobCtryCd
		self._MobCtryCd = base_types.UninitialisedField(self, 'MobCtryCd', Min2Max3AlphaText, False)

	@property
	def MobMskdMSISDN(self):
		return self._MobMskdMSISDN

	@MobMskdMSISDN.setter
	def MobMskdMSISDN(self, value):
		self._MobMskdMSISDN = value if value is not None else base_types.UninitialisedField(self, 'MobMskdMSISDN', Max35Text, False)

	@MobMskdMSISDN.deleter
	def MobMskdMSISDN(self):
		del self._MobMskdMSISDN
		self._MobMskdMSISDN = base_types.UninitialisedField(self, 'MobMskdMSISDN', Max35Text, False)

	@property
	def MobNtwkCd(self):
		return self._MobNtwkCd

	@MobNtwkCd.setter
	def MobNtwkCd(self, value):
		self._MobNtwkCd = value if value is not None else base_types.UninitialisedField(self, 'MobNtwkCd', Min2Max3NumericText, False)

	@MobNtwkCd.deleter
	def MobNtwkCd(self):
		del self._MobNtwkCd
		self._MobNtwkCd = base_types.UninitialisedField(self, 'MobNtwkCd', Min2Max3NumericText, False)

	@property
	def PrtctdMobData(self):
		return self._PrtctdMobData

	@PrtctdMobData.setter
	def PrtctdMobData(self, value):
		self._PrtctdMobData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdMobData', ContentInformationType40, False)

	@PrtctdMobData.deleter
	def PrtctdMobData(self):
		del self._PrtctdMobData
		self._PrtctdMobData = base_types.UninitialisedField(self, 'PrtctdMobData', ContentInformationType40, False)

	@property
	def SnstvMobData(self):
		return self._SnstvMobData

	@SnstvMobData.setter
	def SnstvMobData(self, value):
		self._SnstvMobData = value if value is not None else base_types.UninitialisedField(self, 'SnstvMobData', SensitiveMobileData1, False)

	@SnstvMobData.deleter
	def SnstvMobData(self):
		del self._SnstvMobData
		self._SnstvMobData = base_types.UninitialisedField(self, 'SnstvMobData', SensitiveMobileData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Glctn', type=Geolocation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobCtryCd', type=Min2Max3AlphaText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobMskdMSISDN', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobNtwkCd', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdMobData', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnstvMobData', type=SensitiveMobileData1, min=0, max=1, mutex_group=None, array=False),
	))