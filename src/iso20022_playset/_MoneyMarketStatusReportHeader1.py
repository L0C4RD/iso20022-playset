from . import base_types
from .StatisticalReportingStatus1Code import StatisticalReportingStatus1Code
from .DateTimePeriod1 import DateTimePeriod1
from .GenericValidationRuleIdentification1 import GenericValidationRuleIdentification1
from .LEIIdentifier import LEIIdentifier

class MoneyMarketStatusReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_RptgPrd", "_VldtnRule", "_RptgAgt", "_RptSts"]
	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if type(value) != base_types.auto else self.make_default("RptgPrd")

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = None

	@property
	def VldtnRule(self):
		return self._VldtnRule

	@VldtnRule.setter
	def VldtnRule(self, value):
		self._VldtnRule = value if type(value) != base_types.auto else self.make_default("VldtnRule")

	@VldtnRule.deleter
	def VldtnRule(self):
		del self._VldtnRule
		self._VldtnRule = None

	@property
	def RptgAgt(self):
		return self._RptgAgt

	@RptgAgt.setter
	def RptgAgt(self, value):
		self._RptgAgt = value if type(value) != base_types.auto else self.make_default("RptgAgt")

	@RptgAgt.deleter
	def RptgAgt(self):
		del self._RptgAgt
		self._RptgAgt = None

	@property
	def RptSts(self):
		return self._RptSts

	@RptSts.setter
	def RptSts(self, value):
		self._RptSts = value if type(value) != base_types.auto else self.make_default("RptSts")

	@RptSts.deleter
	def RptSts(self):
		del self._RptSts
		self._RptSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptgPrd', type=DateTimePeriod1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnRule', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgAgt', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptSts', type=StatisticalReportingStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

