# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AmountPricePerFinancialInstrumentQuantity9
from . import SecuritiesPosition1
from . import SecurityIdentification19

class SecurityCharacteristics3(base_types._BaseFieldType):

	__slots__ = ["_CollVal", "_Id", "_Pos", "_ValtnPric"]
	@property
	def CollVal(self):
		return self._CollVal

	@CollVal.setter
	def CollVal(self, value):
		self._CollVal = value if value is not None else base_types.UninitialisedField(self, 'CollVal', ActiveCurrencyAndAmount, False)

	@CollVal.deleter
	def CollVal(self):
		del self._CollVal
		self._CollVal = base_types.UninitialisedField(self, 'CollVal', ActiveCurrencyAndAmount, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', SecurityIdentification19, True)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', SecurityIdentification19, True)

	@property
	def Pos(self):
		return self._Pos

	@Pos.setter
	def Pos(self, value):
		self._Pos = value if value is not None else base_types.UninitialisedField(self, 'Pos', SecuritiesPosition1, True)

	@Pos.deleter
	def Pos(self):
		del self._Pos
		self._Pos = base_types.UninitialisedField(self, 'Pos', SecuritiesPosition1, True)

	@property
	def ValtnPric(self):
		return self._ValtnPric

	@ValtnPric.setter
	def ValtnPric(self, value):
		self._ValtnPric = value if value is not None else base_types.UninitialisedField(self, 'ValtnPric', AmountPricePerFinancialInstrumentQuantity9, False)

	@ValtnPric.deleter
	def ValtnPric(self):
		del self._ValtnPric
		self._ValtnPric = base_types.UninitialisedField(self, 'ValtnPric', AmountPricePerFinancialInstrumentQuantity9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pos', type=SecuritiesPosition1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValtnPric', type=AmountPricePerFinancialInstrumentQuantity9, min=1, max=1, mutex_group=None, array=False),
	))