import base_types
import PhysicalTransferType1Code
import SupplementaryData1
import SecurityIdentification19
import FormOfSecurity1Code
import FinancialInstrumentAggregateBalance1

class AggregateHoldingBalance1(base_types._BaseFieldType):

	__slots__ = ["_HldgPhysTp", "_HldgForm", "_SplmtryData", "_FinInstrmId", "_BalForFinInstrm"]
	@property
	def HldgPhysTp(self):
		return self._HldgPhysTp

	@HldgPhysTp.setter
	def HldgPhysTp(self, value):
		self._HldgPhysTp = value if type(value) != auto else self.make_default("HldgPhysTp")

	@HldgPhysTp.deleter
	def HldgPhysTp(self):
		del self._HldgPhysTp
		self._HldgPhysTp = None

	@property
	def HldgForm(self):
		return self._HldgForm

	@HldgForm.setter
	def HldgForm(self, value):
		self._HldgForm = value if type(value) != auto else self.make_default("HldgForm")

	@HldgForm.deleter
	def HldgForm(self):
		del self._HldgForm
		self._HldgForm = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def BalForFinInstrm(self):
		return self._BalForFinInstrm

	@BalForFinInstrm.setter
	def BalForFinInstrm(self, value):
		self._BalForFinInstrm = value if type(value) != auto else self.make_default("BalForFinInstrm")

	@BalForFinInstrm.deleter
	def BalForFinInstrm(self):
		del self._BalForFinInstrm
		self._BalForFinInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HldgPhysTp', type=PhysicalTransferType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalForFinInstrm', type=FinancialInstrumentAggregateBalance1, min=1, max=None, mutex_group=None, array=True),
	))

