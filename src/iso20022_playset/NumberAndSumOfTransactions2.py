from . import base_types
import DecimalNumber
import Max15NumericText
import CreditDebitCode

class NumberAndSumOfTransactions2(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_TtlNetNtryAmt", "_Sum", "_NbOfNtries"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def TtlNetNtryAmt(self):
		return self._TtlNetNtryAmt

	@TtlNetNtryAmt.setter
	def TtlNetNtryAmt(self, value):
		self._TtlNetNtryAmt = value if type(value) != auto else self.make_default("TtlNetNtryAmt")

	@TtlNetNtryAmt.deleter
	def TtlNetNtryAmt(self):
		del self._TtlNetNtryAmt
		self._TtlNetNtryAmt = None

	@property
	def Sum(self):
		return self._Sum

	@Sum.setter
	def Sum(self, value):
		self._Sum = value if type(value) != auto else self.make_default("Sum")

	@Sum.deleter
	def Sum(self):
		del self._Sum
		self._Sum = None

	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if type(value) != auto else self.make_default("NbOfNtries")

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNetNtryAmt', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfNtries', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))

