# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BankRole1Code import BankRole1Code
from ._CurrencyAndAmount import CurrencyAndAmount
from ._Max35Text import Max35Text
from ._PercentageRate import PercentageRate

class Charges5(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_ChrgsPyee", "_ChrgsPyer", "_Pctg", "_Tp"]
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
	def ChrgsPyee(self):
		return self._ChrgsPyee

	@ChrgsPyee.setter
	def ChrgsPyee(self, value):
		self._ChrgsPyee = value if type(value) != base_types.auto else self.make_default("ChrgsPyee")

	@ChrgsPyee.deleter
	def ChrgsPyee(self):
		del self._ChrgsPyee
		self._ChrgsPyee = None

	@property
	def ChrgsPyer(self):
		return self._ChrgsPyer

	@ChrgsPyer.setter
	def ChrgsPyer(self, value):
		self._ChrgsPyer = value if type(value) != base_types.auto else self.make_default("ChrgsPyer")

	@ChrgsPyer.deleter
	def ChrgsPyer(self):
		del self._ChrgsPyer
		self._ChrgsPyer = None

	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if type(value) != base_types.auto else self.make_default("Pctg")

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=CurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsPyee', type=BankRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsPyer', type=BankRole1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))