# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardDataReading5Code
from . import Max104Text
from . import Max35Text
from . import Max37Text
from . import Max76Text
from . import Min8Max28NumericText

class PlainCardData17(base_types._BaseFieldType):

	__slots__ = ["_AddtlCardData", "_NtryMd", "_PAN", "_Trck1", "_Trck2", "_Trck3"]
	@property
	def AddtlCardData(self):
		return self._AddtlCardData

	@AddtlCardData.setter
	def AddtlCardData(self, value):
		self._AddtlCardData = value if value is not None else base_types.UninitialisedField(self, 'AddtlCardData', Max35Text, True)

	@AddtlCardData.deleter
	def AddtlCardData(self):
		del self._AddtlCardData
		self._AddtlCardData = base_types.UninitialisedField(self, 'AddtlCardData', Max35Text, True)

	@property
	def NtryMd(self):
		return self._NtryMd

	@NtryMd.setter
	def NtryMd(self, value):
		self._NtryMd = value if value is not None else base_types.UninitialisedField(self, 'NtryMd', CardDataReading5Code, False)

	@NtryMd.deleter
	def NtryMd(self):
		del self._NtryMd
		self._NtryMd = base_types.UninitialisedField(self, 'NtryMd', CardDataReading5Code, False)

	@property
	def PAN(self):
		return self._PAN

	@PAN.setter
	def PAN(self, value):
		self._PAN = value if value is not None else base_types.UninitialisedField(self, 'PAN', Min8Max28NumericText, False)

	@PAN.deleter
	def PAN(self):
		del self._PAN
		self._PAN = base_types.UninitialisedField(self, 'PAN', Min8Max28NumericText, False)

	@property
	def Trck1(self):
		return self._Trck1

	@Trck1.setter
	def Trck1(self, value):
		self._Trck1 = value if value is not None else base_types.UninitialisedField(self, 'Trck1', Max76Text, False)

	@Trck1.deleter
	def Trck1(self):
		del self._Trck1
		self._Trck1 = base_types.UninitialisedField(self, 'Trck1', Max76Text, False)

	@property
	def Trck2(self):
		return self._Trck2

	@Trck2.setter
	def Trck2(self, value):
		self._Trck2 = value if value is not None else base_types.UninitialisedField(self, 'Trck2', Max37Text, False)

	@Trck2.deleter
	def Trck2(self):
		del self._Trck2
		self._Trck2 = base_types.UninitialisedField(self, 'Trck2', Max37Text, False)

	@property
	def Trck3(self):
		return self._Trck3

	@Trck3.setter
	def Trck3(self, value):
		self._Trck3 = value if value is not None else base_types.UninitialisedField(self, 'Trck3', Max104Text, False)

	@Trck3.deleter
	def Trck3(self):
		del self._Trck3
		self._Trck3 = base_types.UninitialisedField(self, 'Trck3', Max104Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlCardData', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtryMd', type=CardDataReading5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PAN', type=Min8Max28NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck1', type=Max76Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck2', type=Max37Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck3', type=Max104Text, min=0, max=1, mutex_group=None, array=False),
	))