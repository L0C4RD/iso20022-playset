import base_types
import ExposureConventionType1Code
import MarginTerms1Choice
import CollateralBalance1Choice
import AggregatedIndependentAmount1
import ActiveCurrencyAndAmount

class MarginCall1(base_types._BaseFieldType):

	__slots__ = ["_IndpdntAmtPtyA", "_XpsdAmtPtyB", "_XpsdAmtPtyA", "_IndpdntAmtPtyB", "_MrgnTerms", "_XpsrCnvntn", "_CollBal"]
	@property
	def IndpdntAmtPtyA(self):
		return self._IndpdntAmtPtyA

	@IndpdntAmtPtyA.setter
	def IndpdntAmtPtyA(self, value):
		self._IndpdntAmtPtyA = value if type(value) != auto else self.make_default("IndpdntAmtPtyA")

	@IndpdntAmtPtyA.deleter
	def IndpdntAmtPtyA(self):
		del self._IndpdntAmtPtyA
		self._IndpdntAmtPtyA = None

	@property
	def XpsdAmtPtyB(self):
		return self._XpsdAmtPtyB

	@XpsdAmtPtyB.setter
	def XpsdAmtPtyB(self, value):
		self._XpsdAmtPtyB = value if type(value) != auto else self.make_default("XpsdAmtPtyB")

	@XpsdAmtPtyB.deleter
	def XpsdAmtPtyB(self):
		del self._XpsdAmtPtyB
		self._XpsdAmtPtyB = None

	@property
	def XpsdAmtPtyA(self):
		return self._XpsdAmtPtyA

	@XpsdAmtPtyA.setter
	def XpsdAmtPtyA(self, value):
		self._XpsdAmtPtyA = value if type(value) != auto else self.make_default("XpsdAmtPtyA")

	@XpsdAmtPtyA.deleter
	def XpsdAmtPtyA(self):
		del self._XpsdAmtPtyA
		self._XpsdAmtPtyA = None

	@property
	def IndpdntAmtPtyB(self):
		return self._IndpdntAmtPtyB

	@IndpdntAmtPtyB.setter
	def IndpdntAmtPtyB(self, value):
		self._IndpdntAmtPtyB = value if type(value) != auto else self.make_default("IndpdntAmtPtyB")

	@IndpdntAmtPtyB.deleter
	def IndpdntAmtPtyB(self):
		del self._IndpdntAmtPtyB
		self._IndpdntAmtPtyB = None

	@property
	def MrgnTerms(self):
		return self._MrgnTerms

	@MrgnTerms.setter
	def MrgnTerms(self, value):
		self._MrgnTerms = value if type(value) != auto else self.make_default("MrgnTerms")

	@MrgnTerms.deleter
	def MrgnTerms(self):
		del self._MrgnTerms
		self._MrgnTerms = None

	@property
	def XpsrCnvntn(self):
		return self._XpsrCnvntn

	@XpsrCnvntn.setter
	def XpsrCnvntn(self, value):
		self._XpsrCnvntn = value if type(value) != auto else self.make_default("XpsrCnvntn")

	@XpsrCnvntn.deleter
	def XpsrCnvntn(self):
		del self._XpsrCnvntn
		self._XpsrCnvntn = None

	@property
	def CollBal(self):
		return self._CollBal

	@CollBal.setter
	def CollBal(self, value):
		self._CollBal = value if type(value) != auto else self.make_default("CollBal")

	@CollBal.deleter
	def CollBal(self):
		del self._CollBal
		self._CollBal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndpdntAmtPtyA', type=AggregatedIndependentAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsdAmtPtyB', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsdAmtPtyA', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndpdntAmtPtyB', type=AggregatedIndependentAmount1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnTerms', type=MarginTerms1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpsrCnvntn', type=ExposureConventionType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollBal', type=CollateralBalance1Choice, min=0, max=1, mutex_group=None, array=False),
	))

