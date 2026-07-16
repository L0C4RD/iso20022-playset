# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import ActiveOrHistoricCurrencyCode
from . import FinancialInstrumentQuantity1
from . import LEIIdentifier
from . import Max350Text
from . import OtherIdentification4
from . import PercentageRate

class Fund3(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_EstmtdPctgOfFndTtlNAV", "_EstmtdTtlNAV", "_EstmtdTtlUnitsNb", "_Id", "_LglNttyIdr", "_Nm", "_PrvsTtlNAV", "_PrvsTtlUnitsNb"]
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
	def EstmtdPctgOfFndTtlNAV(self):
		return self._EstmtdPctgOfFndTtlNAV

	@EstmtdPctgOfFndTtlNAV.setter
	def EstmtdPctgOfFndTtlNAV(self, value):
		self._EstmtdPctgOfFndTtlNAV = value if value is not None else base_types.UninitialisedField(self, 'EstmtdPctgOfFndTtlNAV', PercentageRate, False)

	@EstmtdPctgOfFndTtlNAV.deleter
	def EstmtdPctgOfFndTtlNAV(self):
		del self._EstmtdPctgOfFndTtlNAV
		self._EstmtdPctgOfFndTtlNAV = base_types.UninitialisedField(self, 'EstmtdPctgOfFndTtlNAV', PercentageRate, False)

	@property
	def EstmtdTtlNAV(self):
		return self._EstmtdTtlNAV

	@EstmtdTtlNAV.setter
	def EstmtdTtlNAV(self, value):
		self._EstmtdTtlNAV = value if value is not None else base_types.UninitialisedField(self, 'EstmtdTtlNAV', ActiveOrHistoricCurrencyAndAmount, False)

	@EstmtdTtlNAV.deleter
	def EstmtdTtlNAV(self):
		del self._EstmtdTtlNAV
		self._EstmtdTtlNAV = base_types.UninitialisedField(self, 'EstmtdTtlNAV', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def EstmtdTtlUnitsNb(self):
		return self._EstmtdTtlUnitsNb

	@EstmtdTtlUnitsNb.setter
	def EstmtdTtlUnitsNb(self, value):
		self._EstmtdTtlUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'EstmtdTtlUnitsNb', FinancialInstrumentQuantity1, False)

	@EstmtdTtlUnitsNb.deleter
	def EstmtdTtlUnitsNb(self):
		del self._EstmtdTtlUnitsNb
		self._EstmtdTtlUnitsNb = base_types.UninitialisedField(self, 'EstmtdTtlUnitsNb', FinancialInstrumentQuantity1, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', OtherIdentification4, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', OtherIdentification4, False)

	@property
	def LglNttyIdr(self):
		return self._LglNttyIdr

	@LglNttyIdr.setter
	def LglNttyIdr(self, value):
		self._LglNttyIdr = value if value is not None else base_types.UninitialisedField(self, 'LglNttyIdr', LEIIdentifier, False)

	@LglNttyIdr.deleter
	def LglNttyIdr(self):
		del self._LglNttyIdr
		self._LglNttyIdr = base_types.UninitialisedField(self, 'LglNttyIdr', LEIIdentifier, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@property
	def PrvsTtlNAV(self):
		return self._PrvsTtlNAV

	@PrvsTtlNAV.setter
	def PrvsTtlNAV(self, value):
		self._PrvsTtlNAV = value if value is not None else base_types.UninitialisedField(self, 'PrvsTtlNAV', ActiveOrHistoricCurrencyAndAmount, False)

	@PrvsTtlNAV.deleter
	def PrvsTtlNAV(self):
		del self._PrvsTtlNAV
		self._PrvsTtlNAV = base_types.UninitialisedField(self, 'PrvsTtlNAV', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def PrvsTtlUnitsNb(self):
		return self._PrvsTtlUnitsNb

	@PrvsTtlUnitsNb.setter
	def PrvsTtlUnitsNb(self, value):
		self._PrvsTtlUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'PrvsTtlUnitsNb', FinancialInstrumentQuantity1, False)

	@PrvsTtlUnitsNb.deleter
	def PrvsTtlUnitsNb(self):
		del self._PrvsTtlUnitsNb
		self._PrvsTtlUnitsNb = base_types.UninitialisedField(self, 'PrvsTtlUnitsNb', FinancialInstrumentQuantity1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdPctgOfFndTtlNAV', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstmtdTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=OtherIdentification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
	))