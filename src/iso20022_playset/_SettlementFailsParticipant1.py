# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LEIIdentifier
from . import Max2NumericText
from . import SettlementTotalData1

class SettlementFailsParticipant1(base_types._BaseFieldType):

	__slots__ = ["_Aggt", "_LEI", "_Rank"]
	@property
	def Aggt(self):
		return self._Aggt

	@Aggt.setter
	def Aggt(self, value):
		self._Aggt = value if value is not None else base_types.UninitialisedField(self, 'Aggt', SettlementTotalData1, False)

	@Aggt.deleter
	def Aggt(self):
		del self._Aggt
		self._Aggt = base_types.UninitialisedField(self, 'Aggt', SettlementTotalData1, False)

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
	def Rank(self):
		return self._Rank

	@Rank.setter
	def Rank(self, value):
		self._Rank = value if value is not None else base_types.UninitialisedField(self, 'Rank', Max2NumericText, False)

	@Rank.deleter
	def Rank(self):
		del self._Rank
		self._Rank = base_types.UninitialisedField(self, 'Rank', Max2NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Aggt', type=SettlementTotalData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rank', type=Max2NumericText, min=1, max=1, mutex_group=None, array=False),
	))