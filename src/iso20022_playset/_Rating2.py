# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarketIdentification89
from . import Max10Text

class Rating2(base_types._BaseFieldType):

	__slots__ = ["_Ratg", "_SrcOfRatg"]
	@property
	def Ratg(self):
		return self._Ratg

	@Ratg.setter
	def Ratg(self, value):
		self._Ratg = value if value is not None else base_types.UninitialisedField(self, 'Ratg', Max10Text, False)

	@Ratg.deleter
	def Ratg(self):
		del self._Ratg
		self._Ratg = base_types.UninitialisedField(self, 'Ratg', Max10Text, False)

	@property
	def SrcOfRatg(self):
		return self._SrcOfRatg

	@SrcOfRatg.setter
	def SrcOfRatg(self, value):
		self._SrcOfRatg = value if value is not None else base_types.UninitialisedField(self, 'SrcOfRatg', MarketIdentification89, False)

	@SrcOfRatg.deleter
	def SrcOfRatg(self):
		del self._SrcOfRatg
		self._SrcOfRatg = base_types.UninitialisedField(self, 'SrcOfRatg', MarketIdentification89, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ratg', type=Max10Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfRatg', type=MarketIdentification89, min=1, max=1, mutex_group=None, array=False),
	))