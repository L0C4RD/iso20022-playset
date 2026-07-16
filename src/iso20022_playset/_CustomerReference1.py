# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import Max70Text

class CustomerReference1(base_types._BaseFieldType):

	__slots__ = ["_Dtl", "_Id"]
	@property
	def Dtl(self):
		return self._Dtl

	@Dtl.setter
	def Dtl(self, value):
		self._Dtl = value if value is not None else base_types.UninitialisedField(self, 'Dtl', Max70Text, False)

	@Dtl.deleter
	def Dtl(self):
		del self._Dtl
		self._Dtl = base_types.UninitialisedField(self, 'Dtl', Max70Text, False)

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
		base_types.FieldEntry(name='Dtl', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))