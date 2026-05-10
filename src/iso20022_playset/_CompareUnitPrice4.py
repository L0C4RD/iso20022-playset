from . import base_types
from .SecuritiesTransactionPrice17Choice import SecuritiesTransactionPrice17Choice

class CompareUnitPrice4(base_types._BaseFieldType):

	__slots__ = ["_Val2", "_Val1"]
	@property
	def Val2(self):
		return self._Val2

	@Val2.setter
	def Val2(self, value):
		self._Val2 = value if type(value) != base_types.auto else self.make_default("Val2")

	@Val2.deleter
	def Val2(self):
		del self._Val2
		self._Val2 = None

	@property
	def Val1(self):
		return self._Val1

	@Val1.setter
	def Val1(self, value):
		self._Val1 = value if type(value) != base_types.auto else self.make_default("Val1")

	@Val1.deleter
	def Val1(self):
		del self._Val1
		self._Val1 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val2', type=SecuritiesTransactionPrice17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val1', type=SecuritiesTransactionPrice17Choice, min=0, max=1, mutex_group=None, array=False),
	))

