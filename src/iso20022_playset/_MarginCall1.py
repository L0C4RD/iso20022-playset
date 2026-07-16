# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AggregatedIndependentAmount1
from . import CollateralBalance1Choice
from . import ExposureConventionType1Code
from . import MarginTerms1Choice

class MarginCall1(base_types._BaseFieldType):

	__slots__ = ["_CollBal", "_IndpdntAmtPtyA", "_IndpdntAmtPtyB", "_MrgnTerms", "_XpsdAmtPtyA", "_XpsdAmtPtyB", "_XpsrCnvntn"]
	@property
	def CollBal(self):
		return self._CollBal

	@CollBal.setter
	def CollBal(self, value):
		self._CollBal = value if value is not None else base_types.UninitialisedField(self, 'CollBal', CollateralBalance1Choice, False)

	@CollBal.deleter
	def CollBal(self):
		del self._CollBal
		self._CollBal = base_types.UninitialisedField(self, 'CollBal', CollateralBalance1Choice, False)

	@property
	def IndpdntAmtPtyA(self):
		return self._IndpdntAmtPtyA

	@IndpdntAmtPtyA.setter
	def IndpdntAmtPtyA(self, value):
		self._IndpdntAmtPtyA = value if value is not None else base_types.UninitialisedField(self, 'IndpdntAmtPtyA', AggregatedIndependentAmount1, False)

	@IndpdntAmtPtyA.deleter
	def IndpdntAmtPtyA(self):
		del self._IndpdntAmtPtyA
		self._IndpdntAmtPtyA = base_types.UninitialisedField(self, 'IndpdntAmtPtyA', AggregatedIndependentAmount1, False)

	@property
	def IndpdntAmtPtyB(self):
		return self._IndpdntAmtPtyB

	@IndpdntAmtPtyB.setter
	def IndpdntAmtPtyB(self, value):
		self._IndpdntAmtPtyB = value if value is not None else base_types.UninitialisedField(self, 'IndpdntAmtPtyB', AggregatedIndependentAmount1, False)

	@IndpdntAmtPtyB.deleter
	def IndpdntAmtPtyB(self):
		del self._IndpdntAmtPtyB
		self._IndpdntAmtPtyB = base_types.UninitialisedField(self, 'IndpdntAmtPtyB', AggregatedIndependentAmount1, False)

	@property
	def MrgnTerms(self):
		return self._MrgnTerms

	@MrgnTerms.setter
	def MrgnTerms(self, value):
		self._MrgnTerms = value if value is not None else base_types.UninitialisedField(self, 'MrgnTerms', MarginTerms1Choice, False)

	@MrgnTerms.deleter
	def MrgnTerms(self):
		del self._MrgnTerms
		self._MrgnTerms = base_types.UninitialisedField(self, 'MrgnTerms', MarginTerms1Choice, False)

	@property
	def XpsdAmtPtyA(self):
		return self._XpsdAmtPtyA

	@XpsdAmtPtyA.setter
	def XpsdAmtPtyA(self, value):
		self._XpsdAmtPtyA = value if value is not None else base_types.UninitialisedField(self, 'XpsdAmtPtyA', ActiveCurrencyAndAmount, False)

	@XpsdAmtPtyA.deleter
	def XpsdAmtPtyA(self):
		del self._XpsdAmtPtyA
		self._XpsdAmtPtyA = base_types.UninitialisedField(self, 'XpsdAmtPtyA', ActiveCurrencyAndAmount, False)

	@property
	def XpsdAmtPtyB(self):
		return self._XpsdAmtPtyB

	@XpsdAmtPtyB.setter
	def XpsdAmtPtyB(self, value):
		self._XpsdAmtPtyB = value if value is not None else base_types.UninitialisedField(self, 'XpsdAmtPtyB', ActiveCurrencyAndAmount, False)

	@XpsdAmtPtyB.deleter
	def XpsdAmtPtyB(self):
		del self._XpsdAmtPtyB
		self._XpsdAmtPtyB = base_types.UninitialisedField(self, 'XpsdAmtPtyB', ActiveCurrencyAndAmount, False)

	@property
	def XpsrCnvntn(self):
		return self._XpsrCnvntn

	@XpsrCnvntn.setter
	def XpsrCnvntn(self, value):
		self._XpsrCnvntn = value if value is not None else base_types.UninitialisedField(self, 'XpsrCnvntn', ExposureConventionType1Code, False)

	@XpsrCnvntn.deleter
	def XpsrCnvntn(self):
		del self._XpsrCnvntn
		self._XpsrCnvntn = base_types.UninitialisedField(self, 'XpsrCnvntn', ExposureConventionType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollBal', type=CollateralBalance1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndpdntAmtPtyA', type=AggregatedIndependentAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndpdntAmtPtyB', type=AggregatedIndependentAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnTerms', type=MarginTerms1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsdAmtPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsdAmtPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrCnvntn', type=ExposureConventionType1Code, min=0, max=1, mutex_group=None, array=False),
	))