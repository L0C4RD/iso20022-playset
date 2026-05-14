# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LEIIdentifier import LEIIdentifier
from ._MarketIdentification90 import MarketIdentification90

class PlaceOfTradeIdentification2(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_MktTpAndId"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def MktTpAndId(self):
		return self._MktTpAndId

	@MktTpAndId.setter
	def MktTpAndId(self, value):
		self._MktTpAndId = value if type(value) != base_types.auto else self.make_default("MktTpAndId")

	@MktTpAndId.deleter
	def MktTpAndId(self):
		del self._MktTpAndId
		self._MktTpAndId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktTpAndId', type=MarketIdentification90, min=0, max=1, mutex_group=None, array=False),
	))