# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import DebtInstrumentSeniorityType1Code
from . import ISODate
from . import InterestRate6Choice

class DebtInstrument2(base_types._BaseFieldType):

	__slots__ = ["_DebtSnrty", "_IntrstRate", "_MtrtyDt", "_NmnlValPerUnit", "_TtlIssdNmnlAmt"]
	@property
	def DebtSnrty(self):
		return self._DebtSnrty

	@DebtSnrty.setter
	def DebtSnrty(self, value):
		self._DebtSnrty = value if value is not None else base_types.UninitialisedField(self, 'DebtSnrty', DebtInstrumentSeniorityType1Code, False)

	@DebtSnrty.deleter
	def DebtSnrty(self):
		del self._DebtSnrty
		self._DebtSnrty = base_types.UninitialisedField(self, 'DebtSnrty', DebtInstrumentSeniorityType1Code, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', InterestRate6Choice, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', InterestRate6Choice, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@property
	def NmnlValPerUnit(self):
		return self._NmnlValPerUnit

	@NmnlValPerUnit.setter
	def NmnlValPerUnit(self, value):
		self._NmnlValPerUnit = value if value is not None else base_types.UninitialisedField(self, 'NmnlValPerUnit', ActiveOrHistoricCurrencyAndAmount, False)

	@NmnlValPerUnit.deleter
	def NmnlValPerUnit(self):
		del self._NmnlValPerUnit
		self._NmnlValPerUnit = base_types.UninitialisedField(self, 'NmnlValPerUnit', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlIssdNmnlAmt(self):
		return self._TtlIssdNmnlAmt

	@TtlIssdNmnlAmt.setter
	def TtlIssdNmnlAmt(self, value):
		self._TtlIssdNmnlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlIssdNmnlAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlIssdNmnlAmt.deleter
	def TtlIssdNmnlAmt(self):
		del self._TtlIssdNmnlAmt
		self._TtlIssdNmnlAmt = base_types.UninitialisedField(self, 'TtlIssdNmnlAmt', ActiveOrHistoricCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DebtSnrty', type=DebtInstrumentSeniorityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRate6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmnlValPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlIssdNmnlAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))