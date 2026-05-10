from . import base_types
from .CardDataReading8Code import CardDataReading8Code
from .ICCResetData1 import ICCResetData1
from .Max10000Binary import Max10000Binary

class DeviceInitialisationCardReaderResponse2(base_types._BaseFieldType):

	__slots__ = ["_ICCRstData", "_AddtlInf", "_CardNtryMd"]
	@property
	def ICCRstData(self):
		return self._ICCRstData

	@ICCRstData.setter
	def ICCRstData(self, value):
		self._ICCRstData = value if type(value) != auto else self.make_default("ICCRstData")

	@ICCRstData.deleter
	def ICCRstData(self):
		del self._ICCRstData
		self._ICCRstData = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def CardNtryMd(self):
		return self._CardNtryMd

	@CardNtryMd.setter
	def CardNtryMd(self, value):
		self._CardNtryMd = value if type(value) != auto else self.make_default("CardNtryMd")

	@CardNtryMd.deleter
	def CardNtryMd(self):
		del self._CardNtryMd
		self._CardNtryMd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ICCRstData', type=ICCResetData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardNtryMd', type=CardDataReading8Code, min=0, max=1, mutex_group=None, array=False),
	))

