# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._CreditDebitCode import CreditDebitCode
from ._FinancialItemParameters1 import FinancialItemParameters1
from ._FinancingInformationAndStatus1 import FinancingInformationAndStatus1
from ._Instalment2 import Instalment2
from ._InvoiceTotals1 import InvoiceTotals1
from ._Max2000Text import Max2000Text
from ._SupplementaryData1 import SupplementaryData1
from ._ValidationStatusInformation1 import ValidationStatusInformation1
from ._xs:IDREF import xs:IDREF

class FinancialItem1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AssoctdDoc", "_CdtDbtInd", "_DueAmt", "_FinDocRef", "_FincgSts", "_InstlmtInf", "_ItmCntxt", "_PrtryDtls", "_TtlAmt", "_VldtnStsInf"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def AssoctdDoc(self):
		return self._AssoctdDoc

	@AssoctdDoc.setter
	def AssoctdDoc(self, value):
		self._AssoctdDoc = value if type(value) != base_types.auto else self.make_default("AssoctdDoc")

	@AssoctdDoc.deleter
	def AssoctdDoc(self):
		del self._AssoctdDoc
		self._AssoctdDoc = None

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
	def DueAmt(self):
		return self._DueAmt

	@DueAmt.setter
	def DueAmt(self, value):
		self._DueAmt = value if type(value) != base_types.auto else self.make_default("DueAmt")

	@DueAmt.deleter
	def DueAmt(self):
		del self._DueAmt
		self._DueAmt = None

	@property
	def FinDocRef(self):
		return self._FinDocRef

	@FinDocRef.setter
	def FinDocRef(self, value):
		self._FinDocRef = value if type(value) != base_types.auto else self.make_default("FinDocRef")

	@FinDocRef.deleter
	def FinDocRef(self):
		del self._FinDocRef
		self._FinDocRef = None

	@property
	def FincgSts(self):
		return self._FincgSts

	@FincgSts.setter
	def FincgSts(self, value):
		self._FincgSts = value if type(value) != base_types.auto else self.make_default("FincgSts")

	@FincgSts.deleter
	def FincgSts(self):
		del self._FincgSts
		self._FincgSts = None

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
	def ItmCntxt(self):
		return self._ItmCntxt

	@ItmCntxt.setter
	def ItmCntxt(self, value):
		self._ItmCntxt = value if type(value) != base_types.auto else self.make_default("ItmCntxt")

	@ItmCntxt.deleter
	def ItmCntxt(self):
		del self._ItmCntxt
		self._ItmCntxt = None

	@property
	def PrtryDtls(self):
		return self._PrtryDtls

	@PrtryDtls.setter
	def PrtryDtls(self, value):
		self._PrtryDtls = value if type(value) != base_types.auto else self.make_default("PrtryDtls")

	@PrtryDtls.deleter
	def PrtryDtls(self):
		del self._PrtryDtls
		self._PrtryDtls = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if type(value) != base_types.auto else self.make_default("VldtnStsInf")

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = None

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