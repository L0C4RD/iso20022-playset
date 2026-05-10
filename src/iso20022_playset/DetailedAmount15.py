from . import base_types
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .DetailedAmount4 import DetailedAmount4

class DetailedAmount15(base_types._BaseFieldType):

	__slots__ = ["_Grtty", "_Fees", "_Rbt", "_AmtGoodsAndSvcs", "_CshBck", "_Srchrg", "_ValAddedTax"]
	@property
	def Grtty(self):
		return self._Grtty

	@Grtty.setter
	def Grtty(self, value):
		self._Grtty = value if type(value) != auto else self.make_default("Grtty")

	@Grtty.deleter
	def Grtty(self):
		del self._Grtty
		self._Grtty = None

	@property
	def Fees(self):
		return self._Fees

	@Fees.setter
	def Fees(self, value):
		self._Fees = value if type(value) != auto else self.make_default("Fees")

	@Fees.deleter
	def Fees(self):
		del self._Fees
		self._Fees = None

	@property
	def Rbt(self):
		return self._Rbt

	@Rbt.setter
	def Rbt(self, value):
		self._Rbt = value if type(value) != auto else self.make_default("Rbt")

	@Rbt.deleter
	def Rbt(self):
		del self._Rbt
		self._Rbt = None

	@property
	def AmtGoodsAndSvcs(self):
		return self._AmtGoodsAndSvcs

	@AmtGoodsAndSvcs.setter
	def AmtGoodsAndSvcs(self, value):
		self._AmtGoodsAndSvcs = value if type(value) != auto else self.make_default("AmtGoodsAndSvcs")

	@AmtGoodsAndSvcs.deleter
	def AmtGoodsAndSvcs(self):
		del self._AmtGoodsAndSvcs
		self._AmtGoodsAndSvcs = None

	@property
	def CshBck(self):
		return self._CshBck

	@CshBck.setter
	def CshBck(self, value):
		self._CshBck = value if type(value) != auto else self.make_default("CshBck")

	@CshBck.deleter
	def CshBck(self):
		del self._CshBck
		self._CshBck = None

	@property
	def Srchrg(self):
		return self._Srchrg

	@Srchrg.setter
	def Srchrg(self, value):
		self._Srchrg = value if type(value) != auto else self.make_default("Srchrg")

	@Srchrg.deleter
	def Srchrg(self):
		del self._Srchrg
		self._Srchrg = None

	@property
	def ValAddedTax(self):
		return self._ValAddedTax

	@ValAddedTax.setter
	def ValAddedTax(self, value):
		self._ValAddedTax = value if type(value) != auto else self.make_default("ValAddedTax")

	@ValAddedTax.deleter
	def ValAddedTax(self):
		del self._ValAddedTax
		self._ValAddedTax = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Grtty', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fees', type=DetailedAmount4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rbt', type=DetailedAmount4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtGoodsAndSvcs', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshBck', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Srchrg', type=DetailedAmount4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValAddedTax', type=DetailedAmount4, min=0, max=None, mutex_group=None, array=True),
	))

