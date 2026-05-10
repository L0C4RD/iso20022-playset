from . import base_types
from ._SettlementFailsDailyInstructionType1Choice import SettlementFailsDailyInstructionType1Choice

class SettlementFailsDailyCSD3(base_types._BaseFieldType):

	__slots__ = ["_CrossCSD", "_IntraCSD"]
	@property
	def CrossCSD(self):
		return self._CrossCSD

	@CrossCSD.setter
	def CrossCSD(self, value):
		self._CrossCSD = value if type(value) != base_types.auto else self.make_default("CrossCSD")

	@CrossCSD.deleter
	def CrossCSD(self):
		del self._CrossCSD
		self._CrossCSD = None

	@property
	def IntraCSD(self):
		return self._IntraCSD

	@IntraCSD.setter
	def IntraCSD(self, value):
		self._IntraCSD = value if type(value) != base_types.auto else self.make_default("IntraCSD")

	@IntraCSD.deleter
	def IntraCSD(self):
		del self._IntraCSD
		self._IntraCSD = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CrossCSD', type=SettlementFailsDailyInstructionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraCSD', type=SettlementFailsDailyInstructionType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

