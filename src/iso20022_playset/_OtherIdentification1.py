# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IdentificationSource3Choice
from . import Max16Text
from . import Max35Text

class OtherIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Sfx", "_Tp"]
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

	@property
	def Sfx(self):
		return self._Sfx

	@Sfx.setter
	def Sfx(self, value):
		self._Sfx = value if value is not None else base_types.UninitialisedField(self, 'Sfx', Max16Text, False)

	@Sfx.deleter
	def Sfx(self):
		del self._Sfx
		self._Sfx = base_types.UninitialisedField(self, 'Sfx', Max16Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', IdentificationSource3Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', IdentificationSource3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sfx', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=IdentificationSource3Choice, min=1, max=1, mutex_group=None, array=False),
	))