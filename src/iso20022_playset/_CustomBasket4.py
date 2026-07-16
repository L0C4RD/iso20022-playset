# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BasketConstituents3
from . import LEIIdentifier
from . import Max52Text

class CustomBasket4(base_types._BaseFieldType):

	__slots__ = ["_Cnsttnts", "_Id", "_Strr"]
	@property
	def Cnsttnts(self):
		return self._Cnsttnts

	@Cnsttnts.setter
	def Cnsttnts(self, value):
		self._Cnsttnts = value if value is not None else base_types.UninitialisedField(self, 'Cnsttnts', BasketConstituents3, True)

	@Cnsttnts.deleter
	def Cnsttnts(self):
		del self._Cnsttnts
		self._Cnsttnts = base_types.UninitialisedField(self, 'Cnsttnts', BasketConstituents3, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max52Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max52Text, False)

	@property
	def Strr(self):
		return self._Strr

	@Strr.setter
	def Strr(self, value):
		self._Strr = value if value is not None else base_types.UninitialisedField(self, 'Strr', LEIIdentifier, False)

	@Strr.deleter
	def Strr(self):
		del self._Strr
		self._Strr = base_types.UninitialisedField(self, 'Strr', LEIIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cnsttnts', type=BasketConstituents3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Strr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))