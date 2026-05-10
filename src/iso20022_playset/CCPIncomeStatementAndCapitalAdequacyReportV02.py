import base_types
import IncomeStatement2
import HypotheticalCapitalMeasure1
import ActiveCurrencyAndAmount
import SupplementaryData1
import CapitalRequirement1

class CCPIncomeStatementAndCapitalAdequacyReportV02(base_types._BaseFieldType):

	__slots__ = ["_CptlRqrmnts", "_SplmtryData", "_HpthtclCptlMeasr", "_LqdFinRsrcs", "_TtlCptl", "_IncmStmt"]
	@property
	def CptlRqrmnts(self):
		return self._CptlRqrmnts

	@CptlRqrmnts.setter
	def CptlRqrmnts(self, value):
		self._CptlRqrmnts = value if type(value) != auto else self.make_default("CptlRqrmnts")

	@CptlRqrmnts.deleter
	def CptlRqrmnts(self):
		del self._CptlRqrmnts
		self._CptlRqrmnts = None

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
	def HpthtclCptlMeasr(self):
		return self._HpthtclCptlMeasr

	@HpthtclCptlMeasr.setter
	def HpthtclCptlMeasr(self, value):
		self._HpthtclCptlMeasr = value if type(value) != auto else self.make_default("HpthtclCptlMeasr")

	@HpthtclCptlMeasr.deleter
	def HpthtclCptlMeasr(self):
		del self._HpthtclCptlMeasr
		self._HpthtclCptlMeasr = None

	@property
	def LqdFinRsrcs(self):
		return self._LqdFinRsrcs

	@LqdFinRsrcs.setter
	def LqdFinRsrcs(self, value):
		self._LqdFinRsrcs = value if type(value) != auto else self.make_default("LqdFinRsrcs")

	@LqdFinRsrcs.deleter
	def LqdFinRsrcs(self):
		del self._LqdFinRsrcs
		self._LqdFinRsrcs = None

	@property
	def TtlCptl(self):
		return self._TtlCptl

	@TtlCptl.setter
	def TtlCptl(self, value):
		self._TtlCptl = value if type(value) != auto else self.make_default("TtlCptl")

	@TtlCptl.deleter
	def TtlCptl(self):
		del self._TtlCptl
		self._TtlCptl = None

	@property
	def IncmStmt(self):
		return self._IncmStmt

	@IncmStmt.setter
	def IncmStmt(self, value):
		self._IncmStmt = value if type(value) != auto else self.make_default("IncmStmt")

	@IncmStmt.deleter
	def IncmStmt(self):
		del self._IncmStmt
		self._IncmStmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CptlRqrmnts', type=CapitalRequirement1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HpthtclCptlMeasr', type=HypotheticalCapitalMeasure1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LqdFinRsrcs', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCptl', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmStmt', type=IncomeStatement2, min=1, max=1, mutex_group=None, array=False),
	))

