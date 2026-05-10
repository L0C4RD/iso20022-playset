from . import base_types
from .SecuritiesTransactionPrice23Choice import SecuritiesTransactionPrice23Choice

class OptionMultipleBarrierLevels1(base_types._BaseFieldType):

	__slots__ = ["_LwrLvl", "_UpperLvl"]
	@property
	def LwrLvl(self):
		return self._LwrLvl

	@LwrLvl.setter
	def LwrLvl(self, value):
		self._LwrLvl = value if type(value) != base_types.auto else self.make_default("LwrLvl")

	@LwrLvl.deleter
	def LwrLvl(self):
		del self._LwrLvl
		self._LwrLvl = None

	@property
	def UpperLvl(self):
		return self._UpperLvl

	@UpperLvl.setter
	def UpperLvl(self, value):
		self._UpperLvl = value if type(value) != base_types.auto else self.make_default("UpperLvl")

	@UpperLvl.deleter
	def UpperLvl(self):
		del self._UpperLvl
		self._UpperLvl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LwrLvl', type=SecuritiesTransactionPrice23Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpperLvl', type=SecuritiesTransactionPrice23Choice, min=1, max=1, mutex_group=None, array=False),
	))

