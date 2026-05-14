# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class TotalValueInPageAndStatement5(base_types._BaseFieldType):

	__slots__ = ["_TtlCollHeldValOfPg", "_TtlXpsrValOfPg"]
	@property
	def TtlCollHeldValOfPg(self):
		return self._TtlCollHeldValOfPg

	@TtlCollHeldValOfPg.setter
	def TtlCollHeldValOfPg(self, value):
		self._TtlCollHeldValOfPg = value if type(value) != base_types.auto else self.make_default("TtlCollHeldValOfPg")

	@TtlCollHeldValOfPg.deleter
	def TtlCollHeldValOfPg(self):
		del self._TtlCollHeldValOfPg
		self._TtlCollHeldValOfPg = None

	@property
	def TtlXpsrValOfPg(self):
		return self._TtlXpsrValOfPg

	@TtlXpsrValOfPg.setter
	def TtlXpsrValOfPg(self, value):
		self._TtlXpsrValOfPg = value if type(value) != base_types.auto else self.make_default("TtlXpsrValOfPg")

	@TtlXpsrValOfPg.deleter
	def TtlXpsrValOfPg(self):
		del self._TtlXpsrValOfPg
		self._TtlXpsrValOfPg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlCollHeldValOfPg', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlXpsrValOfPg', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))