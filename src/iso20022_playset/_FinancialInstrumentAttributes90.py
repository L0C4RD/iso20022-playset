from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._GenericIdentification168 import GenericIdentification168
from ._InterestComputationMethod2Code import InterestComputationMethod2Code
from ._Max35Text import Max35Text

class FinancialInstrumentAttributes90(base_types._BaseFieldType):

	__slots__ = ["_IndxId", "_IndxUnit", "_IntrstRateTerms", "_Ntnl", "_UnitVal"]
	@property
	def IndxId(self):
		return self._IndxId

	@IndxId.setter
	def IndxId(self, value):
		self._IndxId = value if type(value) != base_types.auto else self.make_default("IndxId")

	@IndxId.deleter
	def IndxId(self):
		del self._IndxId
		self._IndxId = None

	@property
	def IndxUnit(self):
		return self._IndxUnit

	@IndxUnit.setter
	def IndxUnit(self, value):
		self._IndxUnit = value if type(value) != base_types.auto else self.make_default("IndxUnit")

	@IndxUnit.deleter
	def IndxUnit(self):
		del self._IndxUnit
		self._IndxUnit = None

	@property
	def IntrstRateTerms(self):
		return self._IntrstRateTerms

	@IntrstRateTerms.setter
	def IntrstRateTerms(self, value):
		self._IntrstRateTerms = value if type(value) != base_types.auto else self.make_default("IntrstRateTerms")

	@IntrstRateTerms.deleter
	def IntrstRateTerms(self):
		del self._IntrstRateTerms
		self._IntrstRateTerms = None

	@property
	def Ntnl(self):
		return self._Ntnl

	@Ntnl.setter
	def Ntnl(self, value):
		self._Ntnl = value if type(value) != base_types.auto else self.make_default("Ntnl")

	@Ntnl.deleter
	def Ntnl(self):
		del self._Ntnl
		self._Ntnl = None

	@property
	def UnitVal(self):
		return self._UnitVal

	@UnitVal.setter
	def UnitVal(self, value):
		self._UnitVal = value if type(value) != base_types.auto else self.make_default("UnitVal")

	@UnitVal.deleter
	def UnitVal(self):
		del self._UnitVal
		self._UnitVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndxId', type=GenericIdentification168, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxUnit', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRateTerms', type=InterestComputationMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntnl', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

