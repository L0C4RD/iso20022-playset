from . import base_types
from .Number import Number
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class InitialAmount1Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_InitlNbOfInstlmts"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def InitlNbOfInstlmts(self):
		return self._InitlNbOfInstlmts

	@InitlNbOfInstlmts.setter
	def InitlNbOfInstlmts(self, value):
		self._InitlNbOfInstlmts = value if type(value) != base_types.auto else self.make_default("InitlNbOfInstlmts")

	@InitlNbOfInstlmts.deleter
	def InitlNbOfInstlmts(self):
		del self._InitlNbOfInstlmts
		self._InitlNbOfInstlmts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InitlNbOfInstlmts', type=Number, min=0, max=1, mutex_group=1, array=False),
	))

