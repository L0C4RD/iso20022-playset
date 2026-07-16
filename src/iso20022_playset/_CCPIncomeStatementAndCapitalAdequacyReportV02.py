# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CapitalRequirement1
from . import HypotheticalCapitalMeasure1
from . import IncomeStatement2
from . import SupplementaryData1

class CCPIncomeStatementAndCapitalAdequacyReportV02(base_types._BaseFieldType):

	__slots__ = ["_CptlRqrmnts", "_HpthtclCptlMeasr", "_IncmStmt", "_LqdFinRsrcs", "_SplmtryData", "_TtlCptl"]
	@property
	def CptlRqrmnts(self):
		return self._CptlRqrmnts

	@CptlRqrmnts.setter
	def CptlRqrmnts(self, value):
		self._CptlRqrmnts = value if value is not None else base_types.UninitialisedField(self, 'CptlRqrmnts', CapitalRequirement1, False)

	@CptlRqrmnts.deleter
	def CptlRqrmnts(self):
		del self._CptlRqrmnts
		self._CptlRqrmnts = base_types.UninitialisedField(self, 'CptlRqrmnts', CapitalRequirement1, False)

	@property
	def HpthtclCptlMeasr(self):
		return self._HpthtclCptlMeasr

	@HpthtclCptlMeasr.setter
	def HpthtclCptlMeasr(self, value):
		self._HpthtclCptlMeasr = value if value is not None else base_types.UninitialisedField(self, 'HpthtclCptlMeasr', HypotheticalCapitalMeasure1, True)

	@HpthtclCptlMeasr.deleter
	def HpthtclCptlMeasr(self):
		del self._HpthtclCptlMeasr
		self._HpthtclCptlMeasr = base_types.UninitialisedField(self, 'HpthtclCptlMeasr', HypotheticalCapitalMeasure1, True)

	@property
	def IncmStmt(self):
		return self._IncmStmt

	@IncmStmt.setter
	def IncmStmt(self, value):
		self._IncmStmt = value if value is not None else base_types.UninitialisedField(self, 'IncmStmt', IncomeStatement2, False)

	@IncmStmt.deleter
	def IncmStmt(self):
		del self._IncmStmt
		self._IncmStmt = base_types.UninitialisedField(self, 'IncmStmt', IncomeStatement2, False)

	@property
	def LqdFinRsrcs(self):
		return self._LqdFinRsrcs

	@LqdFinRsrcs.setter
	def LqdFinRsrcs(self, value):
		self._LqdFinRsrcs = value if value is not None else base_types.UninitialisedField(self, 'LqdFinRsrcs', ActiveCurrencyAndAmount, False)

	@LqdFinRsrcs.deleter
	def LqdFinRsrcs(self):
		del self._LqdFinRsrcs
		self._LqdFinRsrcs = base_types.UninitialisedField(self, 'LqdFinRsrcs', ActiveCurrencyAndAmount, False)

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

	@property
	def TtlCptl(self):
		return self._TtlCptl

	@TtlCptl.setter
	def TtlCptl(self, value):
		self._TtlCptl = value if value is not None else base_types.UninitialisedField(self, 'TtlCptl', ActiveCurrencyAndAmount, False)

	@TtlCptl.deleter
	def TtlCptl(self):
		del self._TtlCptl
		self._TtlCptl = base_types.UninitialisedField(self, 'TtlCptl', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CptlRqrmnts', type=CapitalRequirement1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HpthtclCptlMeasr', type=HypotheticalCapitalMeasure1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IncmStmt', type=IncomeStatement2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdFinRsrcs', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlCptl', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))