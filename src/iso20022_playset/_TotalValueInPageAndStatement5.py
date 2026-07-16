# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount

class TotalValueInPageAndStatement5(base_types._BaseFieldType):

	__slots__ = ["_TtlCollHeldValOfPg", "_TtlXpsrValOfPg"]
	@property
	def TtlCollHeldValOfPg(self):
		return self._TtlCollHeldValOfPg

	@TtlCollHeldValOfPg.setter
	def TtlCollHeldValOfPg(self, value):
		self._TtlCollHeldValOfPg = value if value is not None else base_types.UninitialisedField(self, 'TtlCollHeldValOfPg', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlCollHeldValOfPg.deleter
	def TtlCollHeldValOfPg(self):
		del self._TtlCollHeldValOfPg
		self._TtlCollHeldValOfPg = base_types.UninitialisedField(self, 'TtlCollHeldValOfPg', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlXpsrValOfPg(self):
		return self._TtlXpsrValOfPg

	@TtlXpsrValOfPg.setter
	def TtlXpsrValOfPg(self, value):
		self._TtlXpsrValOfPg = value if value is not None else base_types.UninitialisedField(self, 'TtlXpsrValOfPg', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlXpsrValOfPg.deleter
	def TtlXpsrValOfPg(self):
		del self._TtlXpsrValOfPg
		self._TtlXpsrValOfPg = base_types.UninitialisedField(self, 'TtlXpsrValOfPg', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlCollHeldValOfPg', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlXpsrValOfPg', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))