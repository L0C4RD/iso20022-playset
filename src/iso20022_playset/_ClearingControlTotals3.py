# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CreditDebit3Code import CreditDebit3Code
from ._ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Number import Number

class ClearingControlTotals3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Ccy", "_CdtDbt", "_Cnt"]
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
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if type(value) != base_types.auto else self.make_default("CdtDbt")

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = None

	@property
	def Cnt(self):
		return self._Cnt

	@Cnt.setter
	def Cnt(self, value):
		self._Cnt = value if type(value) != base_types.auto else self.make_default("Cnt")

	@Cnt.deleter
	def Cnt(self):
		del self._Cnt
		self._Cnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnt', type=Number, min=1, max=1, mutex_group=None, array=False),
	))