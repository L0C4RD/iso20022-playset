import base_types
import ActiveCurrencyAndAmount

class Amount3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlAmt", "_RptgAmt"]
	@property
	def OrgnlAmt(self):
		return self._OrgnlAmt

	@OrgnlAmt.setter
	def OrgnlAmt(self, value):
		self._OrgnlAmt = value if type(value) != auto else self.make_default("OrgnlAmt")

	@OrgnlAmt.deleter
	def OrgnlAmt(self):
		del self._OrgnlAmt
		self._OrgnlAmt = None

	@property
	def RptgAmt(self):
		return self._RptgAmt

	@RptgAmt.setter
	def RptgAmt(self, value):
		self._RptgAmt = value if type(value) != auto else self.make_default("RptgAmt")

	@RptgAmt.deleter
	def RptgAmt(self):
		del self._RptgAmt
		self._RptgAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

