# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import DigitalTokenAmount3

class CurrencyOrDigitalTokenAmount2Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_DgtlTknAmt"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def DgtlTknAmt(self):
		return self._DgtlTknAmt

	@DgtlTknAmt.setter
	def DgtlTknAmt(self, value):
		self._DgtlTknAmt = value if value is not None else base_types.UninitialisedField(self, 'DgtlTknAmt', DigitalTokenAmount3, False)

	@DgtlTknAmt.deleter
	def DgtlTknAmt(self):
		del self._DgtlTknAmt
		self._DgtlTknAmt = base_types.UninitialisedField(self, 'DgtlTknAmt', DigitalTokenAmount3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DgtlTknAmt', type=DigitalTokenAmount3, min=0, max=1, mutex_group=1, array=False),
	))