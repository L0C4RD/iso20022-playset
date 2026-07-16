# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LEIIdentifier
from . import MarketIdentification90

class PlaceOfTradeIdentification2(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_MktTpAndId"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if value is not None else base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@property
	def MktTpAndId(self):
		return self._MktTpAndId

	@MktTpAndId.setter
	def MktTpAndId(self, value):
		self._MktTpAndId = value if value is not None else base_types.UninitialisedField(self, 'MktTpAndId', MarketIdentification90, False)

	@MktTpAndId.deleter
	def MktTpAndId(self):
		del self._MktTpAndId
		self._MktTpAndId = base_types.UninitialisedField(self, 'MktTpAndId', MarketIdentification90, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktTpAndId', type=MarketIdentification90, min=0, max=1, mutex_group=None, array=False),
	))