from . import base_types
import Max2NumericText
import SecurityIdentification19

class SettlementFailsSecurities1(base_types._BaseFieldType):

	__slots__ = ["_Rank", "_FinInstrmId"]
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
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rank', type=Max2NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
	))

