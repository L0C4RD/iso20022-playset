import base_types
import Max20PositiveDecimalNumber
import SettlementDataRate1Choice

class SettlementFailsJustification1(base_types._BaseFieldType):

	__slots__ = ["_Val", "_Rate"]
	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val', type=Max20PositiveDecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=SettlementDataRate1Choice, min=1, max=1, mutex_group=None, array=False),
	))

