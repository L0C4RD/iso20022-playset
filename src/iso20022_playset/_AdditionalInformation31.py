# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import Max35NumericText

class AdditionalInformation31(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AlphaNmrc", "_Nmrc"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', Max350Text, False)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', Max350Text, False)

	@property
	def AlphaNmrc(self):
		return self._AlphaNmrc

	@AlphaNmrc.setter
	def AlphaNmrc(self, value):
		self._AlphaNmrc = value if value is not None else base_types.UninitialisedField(self, 'AlphaNmrc', Max350Text, False)

	@AlphaNmrc.deleter
	def AlphaNmrc(self):
		del self._AlphaNmrc
		self._AlphaNmrc = base_types.UninitialisedField(self, 'AlphaNmrc', Max350Text, False)

	@property
	def Nmrc(self):
		return self._Nmrc

	@Nmrc.setter
	def Nmrc(self, value):
		self._Nmrc = value if value is not None else base_types.UninitialisedField(self, 'Nmrc', Max35NumericText, False)

	@Nmrc.deleter
	def Nmrc(self):
		del self._Nmrc
		self._Nmrc = base_types.UninitialisedField(self, 'Nmrc', Max35NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AlphaNmrc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nmrc', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
	))