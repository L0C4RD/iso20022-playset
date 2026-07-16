# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max35Text

class DocumentIdentification22(base_types._BaseFieldType):

	__slots__ = ["_DtOfIsse", "_Id"]
	@property
	def DtOfIsse(self):
		return self._DtOfIsse

	@DtOfIsse.setter
	def DtOfIsse(self, value):
		self._DtOfIsse = value if value is not None else base_types.UninitialisedField(self, 'DtOfIsse', ISODate, False)

	@DtOfIsse.deleter
	def DtOfIsse(self):
		del self._DtOfIsse
		self._DtOfIsse = base_types.UninitialisedField(self, 'DtOfIsse', ISODate, False)

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
		base_types.FieldEntry(name='DtOfIsse', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))