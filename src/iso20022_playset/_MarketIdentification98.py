# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarketIdentification5Choice
from . import MarketType19Choice

class MarketIdentification98(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Tp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', MarketIdentification5Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', MarketIdentification5Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', MarketType19Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', MarketType19Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=MarketIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MarketType19Choice, min=1, max=1, mutex_group=None, array=False),
	))