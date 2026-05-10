from . import base_types
from ._CashAccountAndEntry5 import CashAccountAndEntry5
from ._CreditDebitCode import CreditDebitCode
from ._PaymentInstruction47 import PaymentInstruction47
from ._SecuritiesTransactionReferences1 import SecuritiesTransactionReferences1
from ._System3 import System3

class Transaction159(base_types._BaseFieldType):

	__slots__ = ["_AcctNtry", "_CdtDbtInd", "_Pmt", "_PmtFr", "_PmtTo", "_SctiesTxRefs"]
	@property
	def AcctNtry(self):
		return self._AcctNtry

	@AcctNtry.setter
	def AcctNtry(self, value):
		self._AcctNtry = value if type(value) != base_types.auto else self.make_default("AcctNtry")

	@AcctNtry.deleter
	def AcctNtry(self):
		del self._AcctNtry
		self._AcctNtry = None

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
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != base_types.auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def PmtFr(self):
		return self._PmtFr

	@PmtFr.setter
	def PmtFr(self, value):
		self._PmtFr = value if type(value) != base_types.auto else self.make_default("PmtFr")

	@PmtFr.deleter
	def PmtFr(self):
		del self._PmtFr
		self._PmtFr = None

	@property
	def PmtTo(self):
		return self._PmtTo

	@PmtTo.setter
	def PmtTo(self, value):
		self._PmtTo = value if type(value) != base_types.auto else self.make_default("PmtTo")

	@PmtTo.deleter
	def PmtTo(self):
		del self._PmtTo
		self._PmtTo = None

	@property
	def SctiesTxRefs(self):
		return self._SctiesTxRefs

	@SctiesTxRefs.setter
	def SctiesTxRefs(self, value):
		self._SctiesTxRefs = value if type(value) != base_types.auto else self.make_default("SctiesTxRefs")

	@SctiesTxRefs.deleter
	def SctiesTxRefs(self):
		del self._SctiesTxRefs
		self._SctiesTxRefs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctNtry', type=CashAccountAndEntry5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=PaymentInstruction47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFr', type=System3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTo', type=System3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesTxRefs', type=SecuritiesTransactionReferences1, min=0, max=1, mutex_group=None, array=False),
	))

