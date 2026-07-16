# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max70Text

class Jurisdiction1(base_types._BaseFieldType):

	__slots__ = ["_Ctry", "_Id"]
	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if value is not None else base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = base_types.UninitialisedField(self, 'Ctry', CountryCode, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max70Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))