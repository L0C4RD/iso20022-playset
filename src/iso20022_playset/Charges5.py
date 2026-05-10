import base_types
import Max35Text
import CurrencyAndAmount
import PercentageRate
import BankRole1Code

class Charges5(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Pctg", "_Amt", "_ChrgsPyer", "_ChrgsPyee"]
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
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if type(value) != auto else self.make_default("Pctg")

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = None

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
	def ChrgsPyer(self):
		return self._ChrgsPyer

	@ChrgsPyer.setter
	def ChrgsPyer(self, value):
		self._ChrgsPyer = value if type(value) != auto else self.make_default("ChrgsPyer")

	@ChrgsPyer.deleter
	def ChrgsPyer(self):
		del self._ChrgsPyer
		self._ChrgsPyer = None

	@property
	def ChrgsPyee(self):
		return self._ChrgsPyee

	@ChrgsPyee.setter
	def ChrgsPyee(self, value):
		self._ChrgsPyee = value if type(value) != auto else self.make_default("ChrgsPyee")

	@ChrgsPyee.deleter
	def ChrgsPyee(self):
		del self._ChrgsPyee
		self._ChrgsPyee = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsPyer', type=BankRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsPyee', type=BankRole1Code, min=1, max=1, mutex_group=None, array=False),
	))

