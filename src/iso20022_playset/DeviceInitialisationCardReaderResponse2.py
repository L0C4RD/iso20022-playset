from . import base_types
from .Max10000Binary import Max10000Binary
from .ICCResetData1 import ICCResetData1
from .CardDataReading8Code import CardDataReading8Code

class DeviceInitialisationCardReaderResponse2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ICCRstData", "_CardNtryMd"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ICCRstData(self):
		return self._ICCRstData

	@ICCRstData.setter
	def ICCRstData(self, value):
		self._ICCRstData = value if type(value) != base_types.auto else self.make_default("ICCRstData")

	@ICCRstData.deleter
	def ICCRstData(self):
		del self._ICCRstData
		self._ICCRstData = None

	@property
	def CardNtryMd(self):
		return self._CardNtryMd

	@CardNtryMd.setter
	def CardNtryMd(self, value):
		self._CardNtryMd = value if type(value) != base_types.auto else self.make_default("CardNtryMd")

	@CardNtryMd.deleter
	def CardNtryMd(self):
		del self._CardNtryMd
		self._CardNtryMd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRstData', type=ICCResetData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardNtryMd', type=CardDataReading8Code, min=0, max=1, mutex_group=None, array=False),
	))

