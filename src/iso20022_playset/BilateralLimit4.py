from . import base_types
from .Amount2Choice import Amount2Choice
from .CashBalance11 import CashBalance11
from .CreditDebitCode import CreditDebitCode
from .BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8

class BilateralLimit4(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_BilBal", "_CtrPtyId", "_LmtAmt"]
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
	def BilBal(self):
		return self._BilBal

	@BilBal.setter
	def BilBal(self, value):
		self._BilBal = value if type(value) != auto else self.make_default("BilBal")

	@BilBal.deleter
	def BilBal(self):
		del self._BilBal
		self._BilBal = None

	@property
	def CtrPtyId(self):
		return self._CtrPtyId

	@CtrPtyId.setter
	def CtrPtyId(self, value):
		self._CtrPtyId = value if type(value) != auto else self.make_default("CtrPtyId")

	@CtrPtyId.deleter
	def CtrPtyId(self):
		del self._CtrPtyId
		self._CtrPtyId = None

	@property
	def LmtAmt(self):
		return self._LmtAmt

	@LmtAmt.setter
	def LmtAmt(self, value):
		self._LmtAmt = value if type(value) != auto else self.make_default("LmtAmt")

	@LmtAmt.deleter
	def LmtAmt(self):
		del self._LmtAmt
		self._LmtAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BilBal', type=CashBalance11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrPtyId', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LmtAmt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
	))

