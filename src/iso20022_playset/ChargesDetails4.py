import base_types
import CurrencyAndAmount
import ChargesType1Choice

class ChargesDetails4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_ChrgsTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def ChrgsTp(self):
		return self._ChrgsTp

	@ChrgsTp.setter
	def ChrgsTp(self, value):
		self._ChrgsTp = value if type(value) != auto else self.make_default("ChrgsTp")

	@ChrgsTp.deleter
	def ChrgsTp(self):
		del self._ChrgsTp
		self._ChrgsTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsTp', type=ChargesType1Choice, min=1, max=1, mutex_group=None, array=False),
	))

