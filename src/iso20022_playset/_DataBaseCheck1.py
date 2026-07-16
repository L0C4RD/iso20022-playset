# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import YesNoIndicator

class DataBaseCheck1(base_types._BaseFieldType):

	__slots__ = ["_DBChck", "_Id"]
	@property
	def DBChck(self):
		return self._DBChck

	@DBChck.setter
	def DBChck(self, value):
		self._DBChck = value if value is not None else base_types.UninitialisedField(self, 'DBChck', YesNoIndicator, False)

	@DBChck.deleter
	def DBChck(self):
		del self._DBChck
		self._DBChck = base_types.UninitialisedField(self, 'DBChck', YesNoIndicator, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DBChck', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))