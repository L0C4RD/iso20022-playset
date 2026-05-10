from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._ChargeBearerType1Code import ChargeBearerType1Code
from ._CurrencyExchange13 import CurrencyExchange13

class TrackerRecord5(base_types._BaseFieldType):

	__slots__ = ["_Agt", "_ChrgBr", "_ChrgsAmt", "_XchgRateData"]
	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if type(value) != base_types.auto else self.make_default("Agt")

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = None

	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != base_types.auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

	@property
	def ChrgsAmt(self):
		return self._ChrgsAmt

	@ChrgsAmt.setter
	def ChrgsAmt(self, value):
		self._ChrgsAmt = value if type(value) != base_types.auto else self.make_default("ChrgsAmt")

	@ChrgsAmt.deleter
	def ChrgsAmt(self):
		del self._ChrgsAmt
		self._ChrgsAmt = None

	@property
	def XchgRateData(self):
		return self._XchgRateData

	@XchgRateData.setter
	def XchgRateData(self, value):
		self._XchgRateData = value if type(value) != base_types.auto else self.make_default("XchgRateData")

	@XchgRateData.deleter
	def XchgRateData(self):
		del self._XchgRateData
		self._XchgRateData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateData', type=CurrencyExchange13, min=0, max=1, mutex_group=None, array=False),
	))

