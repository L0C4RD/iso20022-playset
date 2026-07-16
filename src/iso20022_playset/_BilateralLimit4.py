# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2Choice
from . import BranchAndFinancialInstitutionIdentification8
from . import CashBalance11
from . import CreditDebitCode

class BilateralLimit4(base_types._BaseFieldType):

	__slots__ = ["_BilBal", "_CdtDbtInd", "_CtrPtyId", "_LmtAmt"]
	@property
	def BilBal(self):
		return self._BilBal

	@BilBal.setter
	def BilBal(self, value):
		self._BilBal = value if value is not None else base_types.UninitialisedField(self, 'BilBal', CashBalance11, True)

	@BilBal.deleter
	def BilBal(self):
		del self._BilBal
		self._BilBal = base_types.UninitialisedField(self, 'BilBal', CashBalance11, True)

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
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyId', BranchAndFinancialInstitutionIdentification8, False)

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = base_types.UninitialisedField(self, 'CtrPtyId', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def LmtAmt(self):
		return self._LmtAmt

	@LmtAmt.setter
	def LmtAmt(self, value):
		self._LmtAmt = value if value is not None else base_types.UninitialisedField(self, 'LmtAmt', Amount2Choice, False)

	@LmtAmt.deleter
	def LmtAmt(self):
		del self._LmtAmt
		self._LmtAmt = base_types.UninitialisedField(self, 'LmtAmt', Amount2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BilBal', type=CashBalance11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyId', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtAmt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
	))