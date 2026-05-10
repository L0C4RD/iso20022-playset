from . import base_types
from ._Max76Text import Max76Text
from ._CardDataReading5Code import CardDataReading5Code
from ._Min8Max28NumericText import Min8Max28NumericText
from ._Max35Text import Max35Text
from ._Max37Text import Max37Text
from ._Max104Text import Max104Text

class PlainCardData17(base_types._BaseFieldType):

	__slots__ = ["_PAN", "_NtryMd", "_Trck2", "_AddtlCardData", "_Trck3", "_Trck1"]
	@property
	def AddtlCardData(self):
		return self._AddtlCardData

	@AddtlCardData.setter
	def AddtlCardData(self, value):
		self._AddtlCardData = value if type(value) != base_types.auto else self.make_default("AddtlCardData")

	@AddtlCardData.deleter
	def AddtlCardData(self):
		del self._AddtlCardData
		self._AddtlCardData = None

	@property
	def NtryMd(self):
		return self._NtryMd

	@NtryMd.setter
	def NtryMd(self, value):
		self._NtryMd = value if type(value) != base_types.auto else self.make_default("NtryMd")

	@NtryMd.deleter
	def NtryMd(self):
		del self._NtryMd
		self._NtryMd = None

	@property
	def PAN(self):
		return self._PAN

	@PAN.setter
	def PAN(self, value):
		self._PAN = value if type(value) != base_types.auto else self.make_default("PAN")

	@PAN.deleter
	def PAN(self):
		del self._PAN
		self._PAN = None

	@property
	def Trck1(self):
		return self._Trck1

	@Trck1.setter
	def Trck1(self, value):
		self._Trck1 = value if type(value) != base_types.auto else self.make_default("Trck1")

	@Trck1.deleter
	def Trck1(self):
		del self._Trck1
		self._Trck1 = None

	@property
	def Trck2(self):
		return self._Trck2

	@Trck2.setter
	def Trck2(self, value):
		self._Trck2 = value if type(value) != base_types.auto else self.make_default("Trck2")

	@Trck2.deleter
	def Trck2(self):
		del self._Trck2
		self._Trck2 = None

	@property
	def Trck3(self):
		return self._Trck3

	@Trck3.setter
	def Trck3(self, value):
		self._Trck3 = value if type(value) != base_types.auto else self.make_default("Trck3")

	@Trck3.deleter
	def Trck3(self):
		del self._Trck3
		self._Trck3 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlCardData', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtryMd', type=CardDataReading5Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PAN', type=Min8Max28NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck1', type=Max76Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck2', type=Max37Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trck3', type=Max104Text, min=0, max=1, mutex_group=None, array=False),
	))

