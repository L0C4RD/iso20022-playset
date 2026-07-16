# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2048Text
from . import Max350Text

class ImplementationSpecification1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Regy"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max2048Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max2048Text, False)

	@property
	def Regy(self):
		return self._Regy

	@Regy.setter
	def Regy(self, value):
		self._Regy = value if value is not None else base_types.UninitialisedField(self, 'Regy', Max350Text, False)

	@Regy.deleter
	def Regy(self):
		del self._Regy
		self._Regy = base_types.UninitialisedField(self, 'Regy', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regy', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))