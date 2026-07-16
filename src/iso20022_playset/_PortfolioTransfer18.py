# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import AllOtherCash1
from . import CashAll1
from . import FinancialInstrument112
from . import FundPortfolio7Choice
from . import ISODate
from . import Max35Text
from . import PaymentInstrument21
from . import ResidualCash2

class PortfolioTransfer18(base_types._BaseFieldType):

	__slots__ = ["_ActlTrfDt", "_AddtlInf", "_AllOthrCsh", "_CshAll", "_FinInstrmAsstForTrf", "_MstrRef", "_PmtDtls", "_Prtfl", "_RsdlCsh", "_TaxDt", "_TrfCmpltnId", "_TrfInstrRef"]
	@property
	def ActlTrfDt(self):
		return self._ActlTrfDt

	@ActlTrfDt.setter
	def ActlTrfDt(self, value):
		self._ActlTrfDt = value if value is not None else base_types.UninitialisedField(self, 'ActlTrfDt', ISODate, False)

	@ActlTrfDt.deleter
	def ActlTrfDt(self):
		del self._ActlTrfDt
		self._ActlTrfDt = base_types.UninitialisedField(self, 'ActlTrfDt', ISODate, False)

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def AllOthrCsh(self):
		return self._AllOthrCsh

	@AllOthrCsh.setter
	def AllOthrCsh(self, value):
		self._AllOthrCsh = value if value is not None else base_types.UninitialisedField(self, 'AllOthrCsh', AllOtherCash1, True)

	@AllOthrCsh.deleter
	def AllOthrCsh(self):
		del self._AllOthrCsh
		self._AllOthrCsh = base_types.UninitialisedField(self, 'AllOthrCsh', AllOtherCash1, True)

	@property
	def CshAll(self):
		return self._CshAll

	@CshAll.setter
	def CshAll(self, value):
		self._CshAll = value if value is not None else base_types.UninitialisedField(self, 'CshAll', CashAll1, True)

	@CshAll.deleter
	def CshAll(self):
		del self._CshAll
		self._CshAll = base_types.UninitialisedField(self, 'CshAll', CashAll1, True)

	@property
	def FinInstrmAsstForTrf(self):
		return self._FinInstrmAsstForTrf

	@FinInstrmAsstForTrf.setter
	def FinInstrmAsstForTrf(self, value):
		self._FinInstrmAsstForTrf = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAsstForTrf', FinancialInstrument112, True)

	@FinInstrmAsstForTrf.deleter
	def FinInstrmAsstForTrf(self):
		del self._FinInstrmAsstForTrf
		self._FinInstrmAsstForTrf = base_types.UninitialisedField(self, 'FinInstrmAsstForTrf', FinancialInstrument112, True)

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if value is not None else base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@property
	def PmtDtls(self):
		return self._PmtDtls

	@PmtDtls.setter
	def PmtDtls(self, value):
		self._PmtDtls = value if value is not None else base_types.UninitialisedField(self, 'PmtDtls', PaymentInstrument21, False)

	@PmtDtls.deleter
	def PmtDtls(self):
		del self._PmtDtls
		self._PmtDtls = base_types.UninitialisedField(self, 'PmtDtls', PaymentInstrument21, False)

	@property
	def Prtfl(self):
		return self._Prtfl

	@Prtfl.setter
	def Prtfl(self, value):
		self._Prtfl = value if value is not None else base_types.UninitialisedField(self, 'Prtfl', FundPortfolio7Choice, False)

	@Prtfl.deleter
	def Prtfl(self):
		del self._Prtfl
		self._Prtfl = base_types.UninitialisedField(self, 'Prtfl', FundPortfolio7Choice, False)

	@property
	def RsdlCsh(self):
		return self._RsdlCsh

	@RsdlCsh.setter
	def RsdlCsh(self, value):
		self._RsdlCsh = value if value is not None else base_types.UninitialisedField(self, 'RsdlCsh', ResidualCash2, True)

	@RsdlCsh.deleter
	def RsdlCsh(self):
		del self._RsdlCsh
		self._RsdlCsh = base_types.UninitialisedField(self, 'RsdlCsh', ResidualCash2, True)

	@property
	def TaxDt(self):
		return self._TaxDt

	@TaxDt.setter
	def TaxDt(self, value):
		self._TaxDt = value if value is not None else base_types.UninitialisedField(self, 'TaxDt', ISODate, False)

	@TaxDt.deleter
	def TaxDt(self):
		del self._TaxDt
		self._TaxDt = base_types.UninitialisedField(self, 'TaxDt', ISODate, False)

	@property
	def TrfCmpltnId(self):
		return self._TrfCmpltnId

	@TrfCmpltnId.setter
	def TrfCmpltnId(self, value):
		self._TrfCmpltnId = value if value is not None else base_types.UninitialisedField(self, 'TrfCmpltnId', Max35Text, False)

	@TrfCmpltnId.deleter
	def TrfCmpltnId(self):
		del self._TrfCmpltnId
		self._TrfCmpltnId = base_types.UninitialisedField(self, 'TrfCmpltnId', Max35Text, False)

	@property
	def TrfInstrRef(self):
		return self._TrfInstrRef

	@TrfInstrRef.setter
	def TrfInstrRef(self, value):
		self._TrfInstrRef = value if value is not None else base_types.UninitialisedField(self, 'TrfInstrRef', Max35Text, False)

	@TrfInstrRef.deleter
	def TrfInstrRef(self):
		del self._TrfInstrRef
		self._TrfInstrRef = base_types.UninitialisedField(self, 'TrfInstrRef', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActlTrfDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllOthrCsh', type=AllOtherCash1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshAll', type=CashAll1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmAsstForTrf', type=FinancialInstrument112, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDtls', type=PaymentInstrument21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtfl', type=FundPortfolio7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsdlCsh', type=ResidualCash2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfCmpltnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfInstrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))