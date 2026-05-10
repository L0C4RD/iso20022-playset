from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .ISODateTime import ISODateTime

class PayInScheduleItems1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ddln"]
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
	def Ddln(self):
		return self._Ddln

	@Ddln.setter
	def Ddln(self, value):
		self._Ddln = value if type(value) != base_types.auto else self.make_default("Ddln")

	@Ddln.deleter
	def Ddln(self):
		del self._Ddln
		self._Ddln = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ddln', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

