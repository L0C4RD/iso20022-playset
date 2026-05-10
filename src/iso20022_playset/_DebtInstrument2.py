from . import base_types
from ._DebtInstrumentSeniorityType1Code import DebtInstrumentSeniorityType1Code
from ._ISODate import ISODate
from ._InterestRate6Choice import InterestRate6Choice
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount

class DebtInstrument2(base_types._BaseFieldType):

	__slots__ = ["_DebtSnrty", "_NmnlValPerUnit", "_MtrtyDt", "_TtlIssdNmnlAmt", "_IntrstRate"]
	@property
	def DebtSnrty(self):
		return self._DebtSnrty

	@DebtSnrty.setter
	def DebtSnrty(self, value):
		self._DebtSnrty = value if type(value) != base_types.auto else self.make_default("DebtSnrty")

	@DebtSnrty.deleter
	def DebtSnrty(self):
		del self._DebtSnrty
		self._DebtSnrty = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != base_types.auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def NmnlValPerUnit(self):
		return self._NmnlValPerUnit

	@NmnlValPerUnit.setter
	def NmnlValPerUnit(self, value):
		self._NmnlValPerUnit = value if type(value) != base_types.auto else self.make_default("NmnlValPerUnit")

	@NmnlValPerUnit.deleter
	def NmnlValPerUnit(self):
		del self._NmnlValPerUnit
		self._NmnlValPerUnit = None

	@property
	def TtlIssdNmnlAmt(self):
		return self._TtlIssdNmnlAmt

	@TtlIssdNmnlAmt.setter
	def TtlIssdNmnlAmt(self, value):
		self._TtlIssdNmnlAmt = value if type(value) != base_types.auto else self.make_default("TtlIssdNmnlAmt")

	@TtlIssdNmnlAmt.deleter
	def TtlIssdNmnlAmt(self):
		del self._TtlIssdNmnlAmt
		self._TtlIssdNmnlAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DebtSnrty', type=DebtInstrumentSeniorityType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=InterestRate6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmnlValPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlIssdNmnlAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

