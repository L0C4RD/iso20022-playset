import base_types
import ActiveCurrencyAndAmount

class Amount1Choice(base_types._BaseFieldType):

	__slots__ = ["_IncrAmt", "_DcrAmt"]
	@property
	def IncrAmt(self):
		return self._IncrAmt

	@IncrAmt.setter
	def IncrAmt(self, value):
		self._IncrAmt = value if type(value) != auto else self.make_default("IncrAmt")

	@IncrAmt.deleter
	def IncrAmt(self):
		del self._IncrAmt
		self._IncrAmt = None

	@property
	def DcrAmt(self):
		return self._DcrAmt

	@DcrAmt.setter
	def DcrAmt(self, value):
		self._DcrAmt = value if type(value) != auto else self.make_default("DcrAmt")

	@DcrAmt.deleter
	def DcrAmt(self):
		del self._DcrAmt
		self._DcrAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncrAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DcrAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))

