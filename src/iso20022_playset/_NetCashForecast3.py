# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import FinancialInstrumentQuantity1
from . import FlowDirectionType1Code

class NetCashForecast3(base_types._BaseFieldType):

	__slots__ = ["_FlowDrctn", "_NetAmt", "_NetUnitsNb"]
	@property
	def FlowDrctn(self):
		return self._FlowDrctn

	@FlowDrctn.setter
	def FlowDrctn(self, value):
		self._FlowDrctn = value if value is not None else base_types.UninitialisedField(self, 'FlowDrctn', FlowDirectionType1Code, False)

	@FlowDrctn.deleter
	def FlowDrctn(self):
		del self._FlowDrctn
		self._FlowDrctn = base_types.UninitialisedField(self, 'FlowDrctn', FlowDirectionType1Code, False)

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if value is not None else base_types.UninitialisedField(self, 'NetAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = base_types.UninitialisedField(self, 'NetAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def NetUnitsNb(self):
		return self._NetUnitsNb

	@NetUnitsNb.setter
	def NetUnitsNb(self, value):
		self._NetUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'NetUnitsNb', FinancialInstrumentQuantity1, False)

	@NetUnitsNb.deleter
	def NetUnitsNb(self):
		del self._NetUnitsNb
		self._NetUnitsNb = base_types.UninitialisedField(self, 'NetUnitsNb', FinancialInstrumentQuantity1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FlowDrctn', type=FlowDirectionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
	))