# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ActiveOrHistoricCurrencyCode

class EquivalentAmount2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CcyOfTrf"]
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
	def CcyOfTrf(self):
		return self._CcyOfTrf

	@CcyOfTrf.setter
	def CcyOfTrf(self, value):
		self._CcyOfTrf = value if value is not None else base_types.UninitialisedField(self, 'CcyOfTrf', ActiveOrHistoricCurrencyCode, False)

	@CcyOfTrf.deleter
	def CcyOfTrf(self):
		del self._CcyOfTrf
		self._CcyOfTrf = base_types.UninitialisedField(self, 'CcyOfTrf', ActiveOrHistoricCurrencyCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyOfTrf', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))