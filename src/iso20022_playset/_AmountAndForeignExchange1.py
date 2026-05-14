# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ForeignExchangeTerms24 import ForeignExchangeTerms24

class AmountAndForeignExchange1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_FX"]
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
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if type(value) != base_types.auto else self.make_default("FX")

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FX', type=ForeignExchangeTerms24, min=0, max=1, mutex_group=None, array=False),
	))