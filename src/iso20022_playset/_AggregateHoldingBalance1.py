# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentAggregateBalance1
from . import FormOfSecurity1Code
from . import PhysicalTransferType1Code
from . import SecurityIdentification19
from . import SupplementaryData1

class AggregateHoldingBalance1(base_types._BaseFieldType):

	__slots__ = ["_BalForFinInstrm", "_FinInstrmId", "_HldgForm", "_HldgPhysTp", "_SplmtryData"]
	@property
	def BalForFinInstrm(self):
		return self._BalForFinInstrm

	@BalForFinInstrm.setter
	def BalForFinInstrm(self, value):
		self._BalForFinInstrm = value if value is not None else base_types.UninitialisedField(self, 'BalForFinInstrm', FinancialInstrumentAggregateBalance1, True)

	@BalForFinInstrm.deleter
	def BalForFinInstrm(self):
		del self._BalForFinInstrm
		self._BalForFinInstrm = base_types.UninitialisedField(self, 'BalForFinInstrm', FinancialInstrumentAggregateBalance1, True)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', SecurityIdentification19, False)

	@property
	def HldgForm(self):
		return self._HldgForm

	@HldgForm.setter
	def HldgForm(self, value):
		self._HldgForm = value if value is not None else base_types.UninitialisedField(self, 'HldgForm', FormOfSecurity1Code, False)

	@HldgForm.deleter
	def HldgForm(self):
		del self._HldgForm
		self._HldgForm = base_types.UninitialisedField(self, 'HldgForm', FormOfSecurity1Code, False)

	@property
	def HldgPhysTp(self):
		return self._HldgPhysTp

	@HldgPhysTp.setter
	def HldgPhysTp(self, value):
		self._HldgPhysTp = value if value is not None else base_types.UninitialisedField(self, 'HldgPhysTp', PhysicalTransferType1Code, False)

	@HldgPhysTp.deleter
	def HldgPhysTp(self):
		del self._HldgPhysTp
		self._HldgPhysTp = base_types.UninitialisedField(self, 'HldgPhysTp', PhysicalTransferType1Code, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalForFinInstrm', type=FinancialInstrumentAggregateBalance1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgPhysTp', type=PhysicalTransferType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))