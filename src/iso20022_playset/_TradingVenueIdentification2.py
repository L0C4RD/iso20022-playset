# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max50Text
from . import TradingVenue2Code

class TradingVenueIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Tp"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max50Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max50Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TradingVenue2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TradingVenue2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max50Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TradingVenue2Code, min=1, max=1, mutex_group=None, array=False),
	))