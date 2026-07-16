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

class Fund4(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Id", "_LglNttyIdr", "_Nm", "_PctgOfFndTtlNAV", "_PrvsTtlNAV", "_PrvsTtlUnitsNb", "_TtlNAV", "_TtlUnitsNb"]
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
	def PctgOfFndTtlNAV(self):
		return self._PctgOfFndTtlNAV

	@PctgOfFndTtlNAV.setter
	def PctgOfFndTtlNAV(self, value):
		self._PctgOfFndTtlNAV = value if value is not None else base_types.UninitialisedField(self, 'PctgOfFndTtlNAV', PercentageRate, False)

	@PctgOfFndTtlNAV.deleter
	def PctgOfFndTtlNAV(self):
		del self._PctgOfFndTtlNAV
		self._PctgOfFndTtlNAV = base_types.UninitialisedField(self, 'PctgOfFndTtlNAV', PercentageRate, False)

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

	@property
	def TtlNAV(self):
		return self._TtlNAV

	@TtlNAV.setter
	def TtlNAV(self, value):
		self._TtlNAV = value if value is not None else base_types.UninitialisedField(self, 'TtlNAV', ActiveOrHistoricCurrencyAndAmount, False)

	@TtlNAV.deleter
	def TtlNAV(self):
		del self._TtlNAV
		self._TtlNAV = base_types.UninitialisedField(self, 'TtlNAV', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TtlUnitsNb(self):
		return self._TtlUnitsNb

	@TtlUnitsNb.setter
	def TtlUnitsNb(self, value):
		self._TtlUnitsNb = value if value is not None else base_types.UninitialisedField(self, 'TtlUnitsNb', FinancialInstrumentQuantity1, False)

	@TtlUnitsNb.deleter
	def TtlUnitsNb(self):
		del self._TtlUnitsNb
		self._TtlUnitsNb = base_types.UninitialisedField(self, 'TtlUnitsNb', FinancialInstrumentQuantity1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=OtherIdentification4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PctgOfFndTtlNAV', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsTtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNAV', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlUnitsNb', type=FinancialInstrumentQuantity1, min=0, max=1, mutex_group=None, array=False),
	))