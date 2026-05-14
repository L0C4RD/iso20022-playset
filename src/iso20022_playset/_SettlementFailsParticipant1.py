# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LEIIdentifier import LEIIdentifier
from ._Max2NumericText import Max2NumericText
from ._SettlementTotalData1 import SettlementTotalData1

class SettlementFailsParticipant1(base_types._BaseFieldType):

	__slots__ = ["_Aggt", "_LEI", "_Rank"]
	@property
	def Aggt(self):
		return self._Aggt

	@Aggt.setter
	def Aggt(self, value):
		self._Aggt = value if type(value) != base_types.auto else self.make_default("Aggt")

	@Aggt.deleter
	def Aggt(self):
		del self._Aggt
		self._Aggt = None

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
	def Rank(self):
		return self._Rank

	@Rank.setter
	def Rank(self, value):
		self._Rank = value if type(value) != base_types.auto else self.make_default("Rank")

	@Rank.deleter
	def Rank(self):
		del self._Rank
		self._Rank = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Aggt', type=SettlementTotalData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rank', type=Max2NumericText, min=1, max=1, mutex_group=None, array=False),
	))