# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import AmountAndDirection34
from . import BillingChargeMethod1Code
from . import Max20Text

class BillingPrice1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Mtd", "_Rule", "_UnitPric"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@property
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if value is not None else base_types.UninitialisedField(self, 'Mtd', BillingChargeMethod1Code, False)

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = base_types.UninitialisedField(self, 'Mtd', BillingChargeMethod1Code, False)

	@property
	def Rule(self):
		return self._Rule

	@Rule.setter
	def Rule(self, value):
		self._Rule = value if value is not None else base_types.UninitialisedField(self, 'Rule', Max20Text, False)

	@Rule.deleter
	def Rule(self):
		del self._Rule
		self._Rule = base_types.UninitialisedField(self, 'Rule', Max20Text, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', AmountAndDirection34, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', AmountAndDirection34, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtd', type=BillingChargeMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rule', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
	))