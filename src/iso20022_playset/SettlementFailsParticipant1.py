import base_types
import SettlementTotalData1
import Max2NumericText
import LEIIdentifier

class SettlementFailsParticipant1(base_types._BaseFieldType):

	__slots__ = ["_Rank", "_LEI", "_Aggt"]
	@property
	def Rank(self):
		return self._Rank

	@Rank.setter
	def Rank(self, value):
		self._Rank = value if type(value) != auto else self.make_default("Rank")

	@Rank.deleter
	def Rank(self):
		del self._Rank
		self._Rank = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def Aggt(self):
		return self._Aggt

	@Aggt.setter
	def Aggt(self, value):
		self._Aggt = value if type(value) != auto else self.make_default("Aggt")

	@Aggt.deleter
	def Aggt(self):
		del self._Aggt
		self._Aggt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rank', type=Max2NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Aggt', type=SettlementTotalData1, min=1, max=1, mutex_group=None, array=False),
	))

