import base_types
import SecuritiesPosition1
import SecurityIdentification19
import ActiveCurrencyAndAmount
import AmountPricePerFinancialInstrumentQuantity9

class SecurityCharacteristics3(base_types._BaseFieldType):

	__slots__ = ["_Id", "_ValtnPric", "_CollVal", "_Pos"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def ValtnPric(self):
		return self._ValtnPric

	@ValtnPric.setter
	def ValtnPric(self, value):
		self._ValtnPric = value if type(value) != auto else self.make_default("ValtnPric")

	@ValtnPric.deleter
	def ValtnPric(self):
		del self._ValtnPric
		self._ValtnPric = None

	@property
	def CollVal(self):
		return self._CollVal

	@CollVal.setter
	def CollVal(self, value):
		self._CollVal = value if type(value) != auto else self.make_default("CollVal")

	@CollVal.deleter
	def CollVal(self):
		del self._CollVal
		self._CollVal = None

	@property
	def Pos(self):
		return self._Pos

	@Pos.setter
	def Pos(self, value):
		self._Pos = value if type(value) != auto else self.make_default("Pos")

	@Pos.deleter
	def Pos(self):
		del self._Pos
		self._Pos = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=SecurityIdentification19, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ValtnPric', type=AmountPricePerFinancialInstrumentQuantity9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pos', type=SecuritiesPosition1, min=0, max=None, mutex_group=None, array=True),
	))

