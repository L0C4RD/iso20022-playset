# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._FinancialInstrumentQuantity1 import FinancialInstrumentQuantity1
from ._FlowDirectionType1Code import FlowDirectionType1Code

class NetCashForecast3(base_types._BaseFieldType):

	__slots__ = ["_FlowDrctn", "_NetAmt", "_NetUnitsNb"]
	@property
	def FlowDrctn(self):
		return self._FlowDrctn

	@FlowDrctn.setter
	def FlowDrctn(self, value):
		self._FlowDrctn = value if type(value) != base_types.auto else self.make_default("FlowDrctn")

	@FlowDrctn.deleter
	def FlowDrctn(self):
		del self._FlowDrctn
		self._FlowDrctn = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != base_types.auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def NetUnitsNb(self):
		return self._NetUnitsNb

	@NetUnitsNb.setter
	def NetUnitsNb(self, value):
		self._NetUnitsNb = value if type(value) != base_types.auto else self.make_default("NetUnitsNb")

	@NetUnitsNb.deleter
	def NetUnitsNb(self):
		del self._NetUnitsNb
		self._NetUnitsNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FlowDrctn', type=FlowDirectionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
	))