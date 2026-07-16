# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CreditDebitCode
from . import FinancialItemParameters1
from . import FinancingInformationAndStatus1
from . import Instalment2
from . import InvoiceTotals1
from . import Max2000Text
from . import SupplementaryData1
from . import ValidationStatusInformation1
from . import xs:IDREF

class FinancialItem1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AssoctdDoc", "_CdtDbtInd", "_DueAmt", "_FinDocRef", "_FincgSts", "_InstlmtInf", "_ItmCntxt", "_PrtryDtls", "_TtlAmt", "_VldtnStsInf"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, False)

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if value is not None else base_types.UninitialisedField(self, 'AssoctdDoc', xs:IDREF, True)

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = base_types.UninitialisedField(self, 'AssoctdDoc', xs:IDREF, True)

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
	def DueAmt(self):
		return self._DueAmt

	@DueAmt.setter
	def DueAmt(self, value):
		self._DueAmt = value if value is not None else base_types.UninitialisedField(self, 'DueAmt', ActiveCurrencyAndAmount, False)

	@DueAmt.deleter
	def DueAmt(self):
		del self._DueAmt
		self._DueAmt = base_types.UninitialisedField(self, 'DueAmt', ActiveCurrencyAndAmount, False)

	@property
	def FinDocRef(self):
		return self._FinDocRef

	@FinDocRef.setter
	def FinDocRef(self, value):
		self._FinDocRef = value if value is not None else base_types.UninitialisedField(self, 'FinDocRef', xs:IDREF, True)

	@FinDocRef.deleter
	def FinDocRef(self):
		del self._FinDocRef
		self._FinDocRef = base_types.UninitialisedField(self, 'FinDocRef', xs:IDREF, True)

	@property
	def FincgSts(self):
		return self._FincgSts

	@FincgSts.setter
	def FincgSts(self, value):
		self._FincgSts = value if value is not None else base_types.UninitialisedField(self, 'FincgSts', FinancingInformationAndStatus1, False)

	@FincgSts.deleter
	def FincgSts(self):
		del self._FincgSts
		self._FincgSts = base_types.UninitialisedField(self, 'FincgSts', FinancingInformationAndStatus1, False)

	@property
	def InstlmtInf(self):
		return self._InstlmtInf

	@InstlmtInf.setter
	def InstlmtInf(self, value):
		self._InstlmtInf = value if value is not None else base_types.UninitialisedField(self, 'InstlmtInf', Instalment2, True)

	@InstlmtInf.deleter
	def InstlmtInf(self):
		del self._InstlmtInf
		self._InstlmtInf = base_types.UninitialisedField(self, 'InstlmtInf', Instalment2, True)

	@property
	def ItmCntxt(self):
		return self._ItmCntxt

	@ItmCntxt.setter
	def ItmCntxt(self, value):
		self._ItmCntxt = value if value is not None else base_types.UninitialisedField(self, 'ItmCntxt', FinancialItemParameters1, False)

	@ItmCntxt.deleter
	def ItmCntxt(self):
		del self._ItmCntxt
		self._ItmCntxt = base_types.UninitialisedField(self, 'ItmCntxt', FinancialItemParameters1, False)

	@property
	def PrtryDtls(self):
		return self._PrtryDtls

	@PrtryDtls.setter
	def PrtryDtls(self, value):
		self._PrtryDtls = value if value is not None else base_types.UninitialisedField(self, 'PrtryDtls', SupplementaryData1, False)

	@PrtryDtls.deleter
	def PrtryDtls(self):
		del self._PrtryDtls
		self._PrtryDtls = base_types.UninitialisedField(self, 'PrtryDtls', SupplementaryData1, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', InvoiceTotals1, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', InvoiceTotals1, False)

	@property
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if value is not None else base_types.UninitialisedField(self, 'VldtnStsInf', ValidationStatusInformation1, False)

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = base_types.UninitialisedField(self, 'VldtnStsInf', ValidationStatusInformation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AssoctdDoc', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DueAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinDocRef', type=XS_IDREF, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FincgSts', type=FinancingInformationAndStatus1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstlmtInf', type=Instalment2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ItmCntxt', type=FinancialItemParameters1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryDtls', type=SupplementaryData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=InvoiceTotals1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
	))