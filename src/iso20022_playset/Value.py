from . import base_types
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class Value(base_types._BaseFieldType):

	__slots__ = ["_BaseCcyItm", "_AltrnCcyItm"]
	@property
	def BaseCcyItm(self):
		return self._BaseCcyItm

	@BaseCcyItm.setter
	def BaseCcyItm(self, value):
		self._BaseCcyItm = value if type(value) != base_types.auto else self.make_default("BaseCcyItm")

	@BaseCcyItm.deleter
	def BaseCcyItm(self):
		del self._BaseCcyItm
		self._BaseCcyItm = None

	@property
	def AltrnCcyItm(self):
		return self._AltrnCcyItm

	@AltrnCcyItm.setter
	def AltrnCcyItm(self, value):
		self._AltrnCcyItm = value if type(value) != base_types.auto else self.make_default("AltrnCcyItm")

	@AltrnCcyItm.deleter
	def AltrnCcyItm(self):
		del self._AltrnCcyItm
		self._AltrnCcyItm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BaseCcyItm', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrnCcyItm', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=None, mutex_group=None, array=True),
	))

