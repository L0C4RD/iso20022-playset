# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardDataReading8Code
from . import ICCResetData1
from . import Max10000Binary

class DeviceInitialisationCardReaderResponse2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CardNtryMd", "_ICCRstData"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max10000Binary, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max10000Binary, False)

	@property
	def CardNtryMd(self):
		return self._CardNtryMd

	@CardNtryMd.setter
	def CardNtryMd(self, value):
		self._CardNtryMd = value if value is not None else base_types.UninitialisedField(self, 'CardNtryMd', CardDataReading8Code, False)

	@CardNtryMd.deleter
	def CardNtryMd(self):
		del self._CardNtryMd
		self._CardNtryMd = base_types.UninitialisedField(self, 'CardNtryMd', CardDataReading8Code, False)

	@property
	def ICCRstData(self):
		return self._ICCRstData

	@ICCRstData.setter
	def ICCRstData(self, value):
		self._ICCRstData = value if value is not None else base_types.UninitialisedField(self, 'ICCRstData', ICCResetData1, False)

	@ICCRstData.deleter
	def ICCRstData(self):
		del self._ICCRstData
		self._ICCRstData = base_types.UninitialisedField(self, 'ICCRstData', ICCResetData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardNtryMd', type=CardDataReading8Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRstData', type=ICCResetData1, min=0, max=1, mutex_group=None, array=False),
	))