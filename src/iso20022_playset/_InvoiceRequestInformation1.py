# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import DocumentGeneralInformation1
from . import FinancingRateOrAmountChoice
from . import Instalment1
from . import InvoiceTotals1
from . import PartyAndAccountIdentificationAndContactInformation1
from . import PartyIdentificationAndContactInformation1
from . import PaymentInformation15
from . import ReferredDocumentInformation2

class InvoiceRequestInformation1(base_types._BaseFieldType):

	__slots__ = ["_Buyr", "_CdtDbtNoteAmt", "_InstlmtInf", "_InvcGnlInf", "_InvcPmtInf", "_InvcTtlsInf", "_ReqdAmt", "_RfrdDoc", "_Spplr"]
	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', PartyIdentificationAndContactInformation1, False)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', PartyIdentificationAndContactInformation1, False)

	@property
	def CdtDbtNoteAmt(self):
		return self._CdtDbtNoteAmt

	@CdtDbtNoteAmt.setter
	def CdtDbtNoteAmt(self, value):
		self._CdtDbtNoteAmt = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtNoteAmt', ActiveCurrencyAndAmount, False)

	@CdtDbtNoteAmt.deleter
	def CdtDbtNoteAmt(self):
		del self._CdtDbtNoteAmt
		self._CdtDbtNoteAmt = base_types.UninitialisedField(self, 'CdtDbtNoteAmt', ActiveCurrencyAndAmount, False)

	@property
	def InstlmtInf(self):
		return self._InstlmtInf

	@InstlmtInf.setter
	def InstlmtInf(self, value):
		self._InstlmtInf = value if value is not None else base_types.UninitialisedField(self, 'InstlmtInf', Instalment1, True)

	@InstlmtInf.deleter
	def InstlmtInf(self):
		del self._InstlmtInf
		self._InstlmtInf = base_types.UninitialisedField(self, 'InstlmtInf', Instalment1, True)

	@property
	def InvcGnlInf(self):
		return self._InvcGnlInf

	@InvcGnlInf.setter
	def InvcGnlInf(self, value):
		self._InvcGnlInf = value if value is not None else base_types.UninitialisedField(self, 'InvcGnlInf', DocumentGeneralInformation1, False)

	@InvcGnlInf.deleter
	def InvcGnlInf(self):
		del self._InvcGnlInf
		self._InvcGnlInf = base_types.UninitialisedField(self, 'InvcGnlInf', DocumentGeneralInformation1, False)

	@property
	def InvcPmtInf(self):
		return self._InvcPmtInf

	@InvcPmtInf.setter
	def InvcPmtInf(self, value):
		self._InvcPmtInf = value if value is not None else base_types.UninitialisedField(self, 'InvcPmtInf', PaymentInformation15, False)

	@InvcPmtInf.deleter
	def InvcPmtInf(self):
		del self._InvcPmtInf
		self._InvcPmtInf = base_types.UninitialisedField(self, 'InvcPmtInf', PaymentInformation15, False)

	@property
	def InvcTtlsInf(self):
		return self._InvcTtlsInf

	@InvcTtlsInf.setter
	def InvcTtlsInf(self, value):
		self._InvcTtlsInf = value if value is not None else base_types.UninitialisedField(self, 'InvcTtlsInf', InvoiceTotals1, False)

	@InvcTtlsInf.deleter
	def InvcTtlsInf(self):
		del self._InvcTtlsInf
		self._InvcTtlsInf = base_types.UninitialisedField(self, 'InvcTtlsInf', InvoiceTotals1, False)

	@property
	def ReqdAmt(self):
		return self._ReqdAmt

	@ReqdAmt.setter
	def ReqdAmt(self, value):
		self._ReqdAmt = value if value is not None else base_types.UninitialisedField(self, 'ReqdAmt', FinancingRateOrAmountChoice, False)

	@ReqdAmt.deleter
	def ReqdAmt(self):
		del self._ReqdAmt
		self._ReqdAmt = base_types.UninitialisedField(self, 'ReqdAmt', FinancingRateOrAmountChoice, False)

	@property
	def RfrdDoc(self):
		return self._RfrdDoc

	@RfrdDoc.setter
	def RfrdDoc(self, value):
		self._RfrdDoc = value if value is not None else base_types.UninitialisedField(self, 'RfrdDoc', ReferredDocumentInformation2, True)

	@RfrdDoc.deleter
	def RfrdDoc(self):
		del self._RfrdDoc
		self._RfrdDoc = base_types.UninitialisedField(self, 'RfrdDoc', ReferredDocumentInformation2, True)

	@property
	def Spplr(self):
		return self._Spplr

	@Spplr.setter
	def Spplr(self, value):
		self._Spplr = value if value is not None else base_types.UninitialisedField(self, 'Spplr', PartyAndAccountIdentificationAndContactInformation1, False)

	@Spplr.deleter
	def Spplr(self):
		del self._Spplr
		self._Spplr = base_types.UninitialisedField(self, 'Spplr', PartyAndAccountIdentificationAndContactInformation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Buyr', type=PartyIdentificationAndContactInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtNoteAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtInf', type=Instalment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvcGnlInf', type=DocumentGeneralInformation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcPmtInf', type=PaymentInformation15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcTtlsInf', type=InvoiceTotals1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdAmt', type=FinancingRateOrAmountChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdDoc', type=ReferredDocumentInformation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Spplr', type=PartyAndAccountIdentificationAndContactInformation1, min=1, max=1, mutex_group=None, array=False),
	))