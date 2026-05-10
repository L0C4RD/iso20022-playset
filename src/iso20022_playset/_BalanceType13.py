from . import base_types
from .BalanceType10Choice import BalanceType10Choice
from .BalanceSubType1Choice import BalanceSubType1Choice

class BalanceType13(base_types._BaseFieldType):

	__slots__ = ["_SubTp", "_CdOrPrtry"]
	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if type(value) != base_types.auto else self.make_default("SubTp")

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = None

	@property
	def CdOrPrtry(self):
		return self._CdOrPrtry

	@CdOrPrtry.setter
	def CdOrPrtry(self, value):
		self._CdOrPrtry = value if type(value) != base_types.auto else self.make_default("CdOrPrtry")

	@CdOrPrtry.deleter
	def CdOrPrtry(self):
		del self._CdOrPrtry
		self._CdOrPrtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SubTp', type=BalanceSubType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdOrPrtry', type=BalanceType10Choice, min=1, max=1, mutex_group=None, array=False),
	))

