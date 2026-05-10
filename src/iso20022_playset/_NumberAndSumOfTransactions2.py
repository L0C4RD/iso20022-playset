from . import base_types
from ._Max15NumericText import Max15NumericText
from ._CreditDebitCode import CreditDebitCode
from ._DecimalNumber import DecimalNumber

class NumberAndSumOfTransactions2(base_types._BaseFieldType):

	__slots__ = ["_TtlNetNtryAmt", "_Sum", "_CdtDbtInd", "_NbOfNtries"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if type(value) != base_types.auto else self.make_default("NbOfNtries")

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = None

	@property
	def Sum(self):
		return self._Sum

	@Sum.setter
	def Sum(self, value):
		self._Sum = value if type(value) != base_types.auto else self.make_default("Sum")

	@Sum.deleter
	def Sum(self):
		del self._Sum
		self._Sum = None

	@property
	def TtlNetNtryAmt(self):
		return self._TtlNetNtryAmt

	@TtlNetNtryAmt.setter
	def TtlNetNtryAmt(self, value):
		self._TtlNetNtryAmt = value if type(value) != base_types.auto else self.make_default("TtlNetNtryAmt")

	@TtlNetNtryAmt.deleter
	def TtlNetNtryAmt(self):
		del self._TtlNetNtryAmt
		self._TtlNetNtryAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfNtries', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNetNtryAmt', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

