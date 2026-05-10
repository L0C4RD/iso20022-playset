from . import base_types
from ._Max35NumericText import Max35NumericText
from ._Max350Text import Max350Text

class AdditionalInformation31(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AlphaNmrc", "_Nmrc"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def AlphaNmrc(self):
		return self._AlphaNmrc

	@AlphaNmrc.setter
	def AlphaNmrc(self, value):
		self._AlphaNmrc = value if type(value) != base_types.auto else self.make_default("AlphaNmrc")

	@AlphaNmrc.deleter
	def AlphaNmrc(self):
		del self._AlphaNmrc
		self._AlphaNmrc = None

	@property
	def Nmrc(self):
		return self._Nmrc

	@Nmrc.setter
	def Nmrc(self, value):
		self._Nmrc = value if type(value) != base_types.auto else self.make_default("Nmrc")

	@Nmrc.deleter
	def Nmrc(self):
		del self._Nmrc
		self._Nmrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AlphaNmrc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nmrc', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
	))

