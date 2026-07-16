# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import AllOtherCash1
from . import CashAll1
from . import FinancialInstrument102
from . import FundPortfolio8Choice
from . import ISODate
from . import Max35Text
from . import PaymentInstrument14
from . import ResidualCash2

class PortfolioTransfer11(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AllOthrCsh", "_CshAll", "_FinInstrmAsstForTrf", "_MstrRef", "_PmtDtls", "_Prtfl", "_ReqdTrfDt", "_RsdlCsh", "_TrfConfId", "_TrfId"]
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
		self._FinInstrmAsstForTrf = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAsstForTrf', FinancialInstrument102, True)

	@FinInstrmAsstForTrf.deleter
	def FinInstrmAsstForTrf(self):
		del self._FinInstrmAsstForTrf
		self._FinInstrmAsstForTrf = base_types.UninitialisedField(self, 'FinInstrmAsstForTrf', FinancialInstrument102, True)

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
		self._PmtDtls = value if value is not None else base_types.UninitialisedField(self, 'PmtDtls', PaymentInstrument14, False)

	@PmtDtls.deleter
	def PmtDtls(self):
		del self._PmtDtls
		self._PmtDtls = base_types.UninitialisedField(self, 'PmtDtls', PaymentInstrument14, False)

	@property
	def Prtfl(self):
		return self._Prtfl

	@Prtfl.setter
	def Prtfl(self, value):
		self._Prtfl = value if value is not None else base_types.UninitialisedField(self, 'Prtfl', FundPortfolio8Choice, False)

	@Prtfl.deleter
	def Prtfl(self):
		del self._Prtfl
		self._Prtfl = base_types.UninitialisedField(self, 'Prtfl', FundPortfolio8Choice, False)

	@property
	def ReqdTrfDt(self):
		return self._ReqdTrfDt

	@ReqdTrfDt.setter
	def ReqdTrfDt(self, value):
		self._ReqdTrfDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdTrfDt', ISODate, False)

	@ReqdTrfDt.deleter
	def ReqdTrfDt(self):
		del self._ReqdTrfDt
		self._ReqdTrfDt = base_types.UninitialisedField(self, 'ReqdTrfDt', ISODate, False)

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
	def TrfConfId(self):
		return self._TrfConfId

	@TrfConfId.setter
	def TrfConfId(self, value):
		self._TrfConfId = value if value is not None else base_types.UninitialisedField(self, 'TrfConfId', Max35Text, False)

	@TrfConfId.deleter
	def TrfConfId(self):
		del self._TrfConfId
		self._TrfConfId = base_types.UninitialisedField(self, 'TrfConfId', Max35Text, False)

	@property
	def TrfId(self):
		return self._TrfId

	@TrfId.setter
	def TrfId(self, value):
		self._TrfId = value if value is not None else base_types.UninitialisedField(self, 'TrfId', Max35Text, False)

	@TrfId.deleter
	def TrfId(self):
		del self._TrfId
		self._TrfId = base_types.UninitialisedField(self, 'TrfId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllOthrCsh', type=AllOtherCash1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshAll', type=CashAll1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmAsstForTrf', type=FinancialInstrument102, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDtls', type=PaymentInstrument14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtfl', type=FundPortfolio8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdTrfDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsdlCsh', type=ResidualCash2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TrfConfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))