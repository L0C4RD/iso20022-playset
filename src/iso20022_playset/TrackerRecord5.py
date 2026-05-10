from . import base_types
import BranchAndFinancialInstitutionIdentification8
import CurrencyExchange13
import ChargeBearerType1Code
import ActiveCurrencyAndAmount

class TrackerRecord5(base_types._BaseFieldType):

	__slots__ = ["_XchgRateData", "_ChrgBr", "_ChrgsAmt", "_Agt"]
	@property
	def XchgRateData(self):
		return self._XchgRateData

	@XchgRateData.setter
	def XchgRateData(self, value):
		self._XchgRateData = value if type(value) != auto else self.make_default("XchgRateData")

	@XchgRateData.deleter
	def XchgRateData(self):
		del self._XchgRateData
		self._XchgRateData = None

	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

	@property
	def ChrgsAmt(self):
		return self._ChrgsAmt

	@ChrgsAmt.setter
	def ChrgsAmt(self, value):
		self._ChrgsAmt = value if type(value) != auto else self.make_default("ChrgsAmt")

	@ChrgsAmt.deleter
	def ChrgsAmt(self):
		del self._ChrgsAmt
		self._ChrgsAmt = None

	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if type(value) != auto else self.make_default("Agt")

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XchgRateData', type=CurrencyExchange13, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
	))

