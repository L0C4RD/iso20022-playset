# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccountAndEntry5
from . import CreditDebitCode
from . import PaymentInstruction47
from . import SecuritiesTransactionReferences1
from . import System3

class Transaction159(base_types._BaseFieldType):

	__slots__ = ["_AcctNtry", "_CdtDbtInd", "_Pmt", "_PmtFr", "_PmtTo", "_SctiesTxRefs"]
	@property
	def AcctNtry(self):
		return self._AcctNtry

	@AcctNtry.setter
	def AcctNtry(self, value):
		self._AcctNtry = value if value is not None else base_types.UninitialisedField(self, 'AcctNtry', CashAccountAndEntry5, False)

	@AcctNtry.deleter
	def AcctNtry(self):
		del self._AcctNtry
		self._AcctNtry = base_types.UninitialisedField(self, 'AcctNtry', CashAccountAndEntry5, False)

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
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if value is not None else base_types.UninitialisedField(self, 'Pmt', PaymentInstruction47, False)

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = base_types.UninitialisedField(self, 'Pmt', PaymentInstruction47, False)

	@property
	def PmtFr(self):
		return self._PmtFr

	@PmtFr.setter
	def PmtFr(self, value):
		self._PmtFr = value if value is not None else base_types.UninitialisedField(self, 'PmtFr', System3, False)

	@PmtFr.deleter
	def PmtFr(self):
		del self._PmtFr
		self._PmtFr = base_types.UninitialisedField(self, 'PmtFr', System3, False)

	@property
	def PmtTo(self):
		return self._PmtTo

	@PmtTo.setter
	def PmtTo(self, value):
		self._PmtTo = value if value is not None else base_types.UninitialisedField(self, 'PmtTo', System3, False)

	@PmtTo.deleter
	def PmtTo(self):
		del self._PmtTo
		self._PmtTo = base_types.UninitialisedField(self, 'PmtTo', System3, False)

	@property
	def SctiesTxRefs(self):
		return self._SctiesTxRefs

	@SctiesTxRefs.setter
	def SctiesTxRefs(self, value):
		self._SctiesTxRefs = value if value is not None else base_types.UninitialisedField(self, 'SctiesTxRefs', SecuritiesTransactionReferences1, False)

	@SctiesTxRefs.deleter
	def SctiesTxRefs(self):
		del self._SctiesTxRefs
		self._SctiesTxRefs = base_types.UninitialisedField(self, 'SctiesTxRefs', SecuritiesTransactionReferences1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctNtry', type=CashAccountAndEntry5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=PaymentInstruction47, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFr', type=System3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTo', type=System3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesTxRefs', type=SecuritiesTransactionReferences1, min=0, max=1, mutex_group=None, array=False),
	))