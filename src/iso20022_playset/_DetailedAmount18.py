# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max70Text import Max70Text
from ._TrueFalseIndicator import TrueFalseIndicator

class DetailedAmount18(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ccy", "_ChrgAcctTo", "_Labl"]
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
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def ChrgAcctTo(self):
		return self._ChrgAcctTo

	@ChrgAcctTo.setter
	def ChrgAcctTo(self, value):
		self._ChrgAcctTo = value if type(value) != base_types.auto else self.make_default("ChrgAcctTo")

	@ChrgAcctTo.deleter
	def ChrgAcctTo(self):
		del self._ChrgAcctTo
		self._ChrgAcctTo = None

	@property
	def Labl(self):
		return self._Labl

	@Labl.setter
	def Labl(self, value):
		self._Labl = value if type(value) != base_types.auto else self.make_default("Labl")

	@Labl.deleter
	def Labl(self):
		del self._Labl
		self._Labl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgAcctTo', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Labl', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))