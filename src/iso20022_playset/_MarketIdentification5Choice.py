# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MICIdentifier
from . import Max140Text

class MarketIdentification5Choice(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_MktIdrCd"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@property
	def MktIdrCd(self):
		return self._MktIdrCd

	@MktIdrCd.setter
	def MktIdrCd(self, value):
		self._MktIdrCd = value if value is not None else base_types.UninitialisedField(self, 'MktIdrCd', MICIdentifier, False)

	@MktIdrCd.deleter
	def MktIdrCd(self):
		del self._MktIdrCd
		self._MktIdrCd = base_types.UninitialisedField(self, 'MktIdrCd', MICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MktIdrCd', type=MICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))