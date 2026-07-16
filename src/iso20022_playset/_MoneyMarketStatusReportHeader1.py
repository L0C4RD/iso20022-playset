# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod1
from . import GenericValidationRuleIdentification1
from . import LEIIdentifier
from . import StatisticalReportingStatus1Code

class MoneyMarketStatusReportHeader1(base_types._BaseFieldType):

	__slots__ = ["_RptSts", "_RptgAgt", "_RptgPrd", "_VldtnRule"]
	@property
	def RptSts(self):
		return self._RptSts

	@RptSts.setter
	def RptSts(self, value):
		self._RptSts = value if value is not None else base_types.UninitialisedField(self, 'RptSts', StatisticalReportingStatus1Code, False)

	@RptSts.deleter
	def RptSts(self):
		del self._RptSts
		self._RptSts = base_types.UninitialisedField(self, 'RptSts', StatisticalReportingStatus1Code, False)

	@property
	def RptgAgt(self):
		return self._RptgAgt

	@RptgAgt.setter
	def RptgAgt(self, value):
		self._RptgAgt = value if value is not None else base_types.UninitialisedField(self, 'RptgAgt', LEIIdentifier, False)

	@RptgAgt.deleter
	def RptgAgt(self):
		del self._RptgAgt
		self._RptgAgt = base_types.UninitialisedField(self, 'RptgAgt', LEIIdentifier, False)

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if value is not None else base_types.UninitialisedField(self, 'RptgPrd', DateTimePeriod1, False)

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = base_types.UninitialisedField(self, 'RptgPrd', DateTimePeriod1, False)

	@property
	def VldtnRule(self):
		return self._VldtnRule

	@VldtnRule.setter
	def VldtnRule(self, value):
		self._VldtnRule = value if value is not None else base_types.UninitialisedField(self, 'VldtnRule', GenericValidationRuleIdentification1, True)

	@VldtnRule.deleter
	def VldtnRule(self):
		del self._VldtnRule
		self._VldtnRule = base_types.UninitialisedField(self, 'VldtnRule', GenericValidationRuleIdentification1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptSts', type=StatisticalReportingStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgAgt', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=DateTimePeriod1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnRule', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
	))