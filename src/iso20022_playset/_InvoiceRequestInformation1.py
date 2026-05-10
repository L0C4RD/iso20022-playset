from . import base_types
from ._PaymentInformation15 import PaymentInformation15
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._FinancingRateOrAmountChoice import FinancingRateOrAmountChoice
from ._DocumentGeneralInformation1 import DocumentGeneralInformation1
from ._ReferredDocumentInformation2 import ReferredDocumentInformation2
from ._InvoiceTotals1 import InvoiceTotals1
from ._PartyIdentificationAndContactInformation1 import PartyIdentificationAndContactInformation1
from ._Instalment1 import Instalment1
from ._PartyAndAccountIdentificationAndContactInformation1 import PartyAndAccountIdentificationAndContactInformation1

class InvoiceRequestInformation1(base_types._BaseFieldType):

	__slots__ = ["_RfrdDoc", "_CdtDbtNoteAmt", "_InstlmtInf", "_InvcGnlInf", "_Spplr", "_InvcTtlsInf", "_ReqdAmt", "_Buyr", "_InvcPmtInf"]
	@property
	def RfrdDoc(self):
		return self._RfrdDoc

	@RfrdDoc.setter
	def RfrdDoc(self, value):
		self._RfrdDoc = value if type(value) != base_types.auto else self.make_default("RfrdDoc")

	@RfrdDoc.deleter
	def RfrdDoc(self):
		del self._RfrdDoc
		self._RfrdDoc = None

	@property
	def CdtDbtNoteAmt(self):
		return self._CdtDbtNoteAmt

	@CdtDbtNoteAmt.setter
	def CdtDbtNoteAmt(self, value):
		self._CdtDbtNoteAmt = value if type(value) != base_types.auto else self.make_default("CdtDbtNoteAmt")

	@CdtDbtNoteAmt.deleter
	def CdtDbtNoteAmt(self):
		del self._CdtDbtNoteAmt
		self._CdtDbtNoteAmt = None

	@property
	def InstlmtInf(self):
		return self._InstlmtInf

	@InstlmtInf.setter
	def InstlmtInf(self, value):
		self._InstlmtInf = value if type(value) != base_types.auto else self.make_default("InstlmtInf")

	@InstlmtInf.deleter
	def InstlmtInf(self):
		del self._InstlmtInf
		self._InstlmtInf = None

	@property
	def InvcGnlInf(self):
		return self._InvcGnlInf

	@InvcGnlInf.setter
	def InvcGnlInf(self, value):
		self._InvcGnlInf = value if type(value) != base_types.auto else self.make_default("InvcGnlInf")

	@InvcGnlInf.deleter
	def InvcGnlInf(self):
		del self._InvcGnlInf
		self._InvcGnlInf = None

	@property
	def Spplr(self):
		return self._Spplr

	@Spplr.setter
	def Spplr(self, value):
		self._Spplr = value if type(value) != base_types.auto else self.make_default("Spplr")

	@Spplr.deleter
	def Spplr(self):
		del self._Spplr
		self._Spplr = None

	@property
	def InvcTtlsInf(self):
		return self._InvcTtlsInf

	@InvcTtlsInf.setter
	def InvcTtlsInf(self, value):
		self._InvcTtlsInf = value if type(value) != base_types.auto else self.make_default("InvcTtlsInf")

	@InvcTtlsInf.deleter
	def InvcTtlsInf(self):
		del self._InvcTtlsInf
		self._InvcTtlsInf = None

	@property
	def ReqdAmt(self):
		return self._ReqdAmt

	@ReqdAmt.setter
	def ReqdAmt(self, value):
		self._ReqdAmt = value if type(value) != base_types.auto else self.make_default("ReqdAmt")

	@ReqdAmt.deleter
	def ReqdAmt(self):
		del self._ReqdAmt
		self._ReqdAmt = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != base_types.auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def InvcPmtInf(self):
		return self._InvcPmtInf

	@InvcPmtInf.setter
	def InvcPmtInf(self, value):
		self._InvcPmtInf = value if type(value) != base_types.auto else self.make_default("InvcPmtInf")

	@InvcPmtInf.deleter
	def InvcPmtInf(self):
		del self._InvcPmtInf
		self._InvcPmtInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RfrdDoc', type=ReferredDocumentInformation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtDbtNoteAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtInf', type=Instalment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvcGnlInf', type=DocumentGeneralInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Spplr', type=PartyAndAccountIdentificationAndContactInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcTtlsInf', type=InvoiceTotals1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdAmt', type=FinancingRateOrAmountChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=PartyIdentificationAndContactInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcPmtInf', type=PaymentInformation15, min=1, max=1, mutex_group=None, array=False),
	))

