from . import base_types
from .YesNoIndicator import YesNoIndicator
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class DerivativeBasicAttributes1(base_types._BaseFieldType):

	__slots__ = ["_IntrstInclInPric", "_NtnlCcyAndAmt"]
	@property
	def IntrstInclInPric(self):
		return self._IntrstInclInPric

	@IntrstInclInPric.setter
	def IntrstInclInPric(self, value):
		self._IntrstInclInPric = value if type(value) != base_types.auto else self.make_default("IntrstInclInPric")

	@IntrstInclInPric.deleter
	def IntrstInclInPric(self):
		del self._IntrstInclInPric
		self._IntrstInclInPric = None

	@property
	def NtnlCcyAndAmt(self):
		return self._NtnlCcyAndAmt

	@NtnlCcyAndAmt.setter
	def NtnlCcyAndAmt(self, value):
		self._NtnlCcyAndAmt = value if type(value) != base_types.auto else self.make_default("NtnlCcyAndAmt")

	@NtnlCcyAndAmt.deleter
	def NtnlCcyAndAmt(self):
		del self._NtnlCcyAndAmt
		self._NtnlCcyAndAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrstInclInPric', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtnlCcyAndAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

