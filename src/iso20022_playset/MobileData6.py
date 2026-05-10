from . import base_types
from .Min2Max3AlphaText import Min2Max3AlphaText
from .ContentInformationType40 import ContentInformationType40
from .Geolocation1 import Geolocation1
from .SensitiveMobileData1 import SensitiveMobileData1
from .Min2Max3NumericText import Min2Max3NumericText
from .Max35Text import Max35Text

class MobileData6(base_types._BaseFieldType):

	__slots__ = ["_MobNtwkCd", "_MobMskdMSISDN", "_PrtctdMobData", "_SnstvMobData", "_Glctn", "_MobCtryCd"]
	@property
	def MobNtwkCd(self):
		return self._MobNtwkCd

	@MobNtwkCd.setter
	def MobNtwkCd(self, value):
		self._MobNtwkCd = value if type(value) != base_types.auto else self.make_default("MobNtwkCd")

	@MobNtwkCd.deleter
	def MobNtwkCd(self):
		del self._MobNtwkCd
		self._MobNtwkCd = None

	@property
	def MobMskdMSISDN(self):
		return self._MobMskdMSISDN

	@MobMskdMSISDN.setter
	def MobMskdMSISDN(self, value):
		self._MobMskdMSISDN = value if type(value) != base_types.auto else self.make_default("MobMskdMSISDN")

	@MobMskdMSISDN.deleter
	def MobMskdMSISDN(self):
		del self._MobMskdMSISDN
		self._MobMskdMSISDN = None

	@property
	def PrtctdMobData(self):
		return self._PrtctdMobData

	@PrtctdMobData.setter
	def PrtctdMobData(self, value):
		self._PrtctdMobData = value if type(value) != base_types.auto else self.make_default("PrtctdMobData")

	@PrtctdMobData.deleter
	def PrtctdMobData(self):
		del self._PrtctdMobData
		self._PrtctdMobData = None

	@property
	def SnstvMobData(self):
		return self._SnstvMobData

	@SnstvMobData.setter
	def SnstvMobData(self, value):
		self._SnstvMobData = value if type(value) != base_types.auto else self.make_default("SnstvMobData")

	@SnstvMobData.deleter
	def SnstvMobData(self):
		del self._SnstvMobData
		self._SnstvMobData = None

	@property
	def Glctn(self):
		return self._Glctn

	@Glctn.setter
	def Glctn(self, value):
		self._Glctn = value if type(value) != base_types.auto else self.make_default("Glctn")

	@Glctn.deleter
	def Glctn(self):
		del self._Glctn
		self._Glctn = None

	@property
	def MobCtryCd(self):
		return self._MobCtryCd

	@MobCtryCd.setter
	def MobCtryCd(self, value):
		self._MobCtryCd = value if type(value) != base_types.auto else self.make_default("MobCtryCd")

	@MobCtryCd.deleter
	def MobCtryCd(self):
		del self._MobCtryCd
		self._MobCtryCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MobNtwkCd', type=Min2Max3NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobMskdMSISDN', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdMobData', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnstvMobData', type=SensitiveMobileData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Glctn', type=Geolocation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobCtryCd', type=Min2Max3AlphaText, min=0, max=1, mutex_group=None, array=False),
	))

