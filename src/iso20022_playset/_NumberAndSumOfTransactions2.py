# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebitCode
from . import DecimalNumber
from . import Max15NumericText

class NumberAndSumOfTransactions2(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_NbOfNtries", "_Sum", "_TtlNetNtryAmt"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def NbOfNtries(self):
		return self._NbOfNtries

	@NbOfNtries.setter
	def NbOfNtries(self, value):
		self._NbOfNtries = value if value is not None else base_types.UninitialisedField(self, 'NbOfNtries', Max15NumericText, False)

	@NbOfNtries.deleter
	def NbOfNtries(self):
		del self._NbOfNtries
		self._NbOfNtries = base_types.UninitialisedField(self, 'NbOfNtries', Max15NumericText, False)

	@property
	def Sum(self):
		return self._Sum

	@Sum.setter
	def Sum(self, value):
		self._Sum = value if value is not None else base_types.UninitialisedField(self, 'Sum', DecimalNumber, False)

	@Sum.deleter
	def Sum(self):
		del self._Sum
		self._Sum = base_types.UninitialisedField(self, 'Sum', DecimalNumber, False)

	@property
	def TtlNetNtryAmt(self):
		return self._TtlNetNtryAmt

	@TtlNetNtryAmt.setter
	def TtlNetNtryAmt(self, value):
		self._TtlNetNtryAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlNetNtryAmt', DecimalNumber, False)

	@TtlNetNtryAmt.deleter
	def TtlNetNtryAmt(self):
		del self._TtlNetNtryAmt
		self._TtlNetNtryAmt = base_types.UninitialisedField(self, 'TtlNetNtryAmt', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfNtries', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNetNtryAmt', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))