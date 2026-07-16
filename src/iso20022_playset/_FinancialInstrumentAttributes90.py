# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import GenericIdentification168
from . import InterestComputationMethod2Code
from . import Max35Text

class FinancialInstrumentAttributes90(base_types._BaseFieldType):

	__slots__ = ["_IndxId", "_IndxUnit", "_IntrstRateTerms", "_Ntnl", "_UnitVal"]
	@property
	def IndxId(self):
		return self._IndxId

	@IndxId.setter
	def IndxId(self, value):
		self._IndxId = value if value is not None else base_types.UninitialisedField(self, 'IndxId', GenericIdentification168, False)

	@IndxId.deleter
	def IndxId(self):
		del self._IndxId
		self._IndxId = base_types.UninitialisedField(self, 'IndxId', GenericIdentification168, False)

	@property
	def IndxUnit(self):
		return self._IndxUnit

	@IndxUnit.setter
	def IndxUnit(self, value):
		self._IndxUnit = value if value is not None else base_types.UninitialisedField(self, 'IndxUnit', Max35Text, False)

	@IndxUnit.deleter
	def IndxUnit(self):
		del self._IndxUnit
		self._IndxUnit = base_types.UninitialisedField(self, 'IndxUnit', Max35Text, False)

	@property
	def IntrstRateTerms(self):
		return self._IntrstRateTerms

	@IntrstRateTerms.setter
	def IntrstRateTerms(self, value):
		self._IntrstRateTerms = value if value is not None else base_types.UninitialisedField(self, 'IntrstRateTerms', InterestComputationMethod2Code, False)

	@IntrstRateTerms.deleter
	def IntrstRateTerms(self):
		del self._IntrstRateTerms
		self._IntrstRateTerms = base_types.UninitialisedField(self, 'IntrstRateTerms', InterestComputationMethod2Code, False)

	@property
	def Ntnl(self):
		return self._Ntnl

	@Ntnl.setter
	def Ntnl(self, value):
		self._Ntnl = value if value is not None else base_types.UninitialisedField(self, 'Ntnl', ActiveCurrencyAndAmount, False)

	@Ntnl.deleter
	def Ntnl(self):
		del self._Ntnl
		self._Ntnl = base_types.UninitialisedField(self, 'Ntnl', ActiveCurrencyAndAmount, False)

	@property
	def UnitVal(self):
		return self._UnitVal

	@UnitVal.setter
	def UnitVal(self, value):
		self._UnitVal = value if value is not None else base_types.UninitialisedField(self, 'UnitVal', ActiveCurrencyAndAmount, False)

	@UnitVal.deleter
	def UnitVal(self):
		del self._UnitVal
		self._UnitVal = base_types.UninitialisedField(self, 'UnitVal', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndxId', type=GenericIdentification168, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndxUnit', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRateTerms', type=InterestComputationMethod2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntnl', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))