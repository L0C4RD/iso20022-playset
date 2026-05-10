import base_types
import CurrencyAndAmount
import AdjustmentDirection1Code
import AdjustmentType1Choice

class Adjustment6(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Amt", "_Drctn"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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
	def Drctn(self):
		return self._Drctn

	@Drctn.setter
	def Drctn(self, value):
		self._Drctn = value if type(value) != auto else self.make_default("Drctn")

	@Drctn.deleter
	def Drctn(self):
		del self._Drctn
		self._Drctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=AdjustmentType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drctn', type=AdjustmentDirection1Code, min=1, max=1, mutex_group=None, array=False),
	))

