# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommodityDerivative4
from . import ContractForDifference2
from . import CreditDefaultSwapsDerivative4Choice
from . import EmissionAllowanceProductType1Code
from . import EquityDerivative2
from . import ForeignExchangeDerivative2
from . import InterestRateDerivative5

class Derivative3Choice(base_types._BaseFieldType):

	__slots__ = ["_Cdt", "_Cmmdty", "_CtrctForDiff", "_EmssnAllwnc", "_Eqty", "_FX", "_IntrstRate"]
	@property
	def Cdt(self):
		return self._Cdt

	@Cdt.setter
	def Cdt(self, value):
		self._Cdt = value if value is not None else base_types.UninitialisedField(self, 'Cdt', CreditDefaultSwapsDerivative4Choice, False)

	@Cdt.deleter
	def Cdt(self):
		del self._Cdt
		self._Cdt = base_types.UninitialisedField(self, 'Cdt', CreditDefaultSwapsDerivative4Choice, False)

	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if value is not None else base_types.UninitialisedField(self, 'Cmmdty', CommodityDerivative4, False)

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = base_types.UninitialisedField(self, 'Cmmdty', CommodityDerivative4, False)

	@property
	def CtrctForDiff(self):
		return self._CtrctForDiff

	@CtrctForDiff.setter
	def CtrctForDiff(self, value):
		self._CtrctForDiff = value if value is not None else base_types.UninitialisedField(self, 'CtrctForDiff', ContractForDifference2, False)

	@CtrctForDiff.deleter
	def CtrctForDiff(self):
		del self._CtrctForDiff
		self._CtrctForDiff = base_types.UninitialisedField(self, 'CtrctForDiff', ContractForDifference2, False)

	@property
	def EmssnAllwnc(self):
		return self._EmssnAllwnc

	@EmssnAllwnc.setter
	def EmssnAllwnc(self, value):
		self._EmssnAllwnc = value if value is not None else base_types.UninitialisedField(self, 'EmssnAllwnc', EmissionAllowanceProductType1Code, False)

	@EmssnAllwnc.deleter
	def EmssnAllwnc(self):
		del self._EmssnAllwnc
		self._EmssnAllwnc = base_types.UninitialisedField(self, 'EmssnAllwnc', EmissionAllowanceProductType1Code, False)

	@property
	def Eqty(self):
		return self._Eqty

	@Eqty.setter
	def Eqty(self, value):
		self._Eqty = value if value is not None else base_types.UninitialisedField(self, 'Eqty', EquityDerivative2, False)

	@Eqty.deleter
	def Eqty(self):
		del self._Eqty
		self._Eqty = base_types.UninitialisedField(self, 'Eqty', EquityDerivative2, False)

	@property
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if value is not None else base_types.UninitialisedField(self, 'FX', ForeignExchangeDerivative2, False)

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = base_types.UninitialisedField(self, 'FX', ForeignExchangeDerivative2, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', InterestRateDerivative5, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', InterestRateDerivative5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdt', type=CreditDefaultSwapsDerivative4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cmmdty', type=CommodityDerivative4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CtrctForDiff', type=ContractForDifference2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EmssnAllwnc', type=EmissionAllowanceProductType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Eqty', type=EquityDerivative2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FX', type=ForeignExchangeDerivative2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRateDerivative5, min=0, max=1, mutex_group=1, array=False),
	))