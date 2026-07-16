# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import FinancialInstrument99
from . import FundPortfolio7Choice
from . import ISODate
from . import Max35Text
from . import ResidualCash1
from . import YesNoIndicator

class PortfolioTransfer9(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_FinInstrmAsstForTrf", "_MstrRef", "_Prtfl", "_PrtlDscvry", "_RsdlCsh", "_TaxDt", "_TrfConfId", "_TrfId"]
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
	def FinInstrmAsstForTrf(self):
		return self._FinInstrmAsstForTrf

	@FinInstrmAsstForTrf.setter
	def FinInstrmAsstForTrf(self, value):
		self._FinInstrmAsstForTrf = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmAsstForTrf', FinancialInstrument99, True)

	@FinInstrmAsstForTrf.deleter
	def FinInstrmAsstForTrf(self):
		del self._FinInstrmAsstForTrf
		self._FinInstrmAsstForTrf = base_types.UninitialisedField(self, 'FinInstrmAsstForTrf', FinancialInstrument99, True)

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
	def PrtlDscvry(self):
		return self._PrtlDscvry

	@PrtlDscvry.setter
	def PrtlDscvry(self, value):
		self._PrtlDscvry = value if value is not None else base_types.UninitialisedField(self, 'PrtlDscvry', YesNoIndicator, False)

	@PrtlDscvry.deleter
	def PrtlDscvry(self):
		del self._PrtlDscvry
		self._PrtlDscvry = base_types.UninitialisedField(self, 'PrtlDscvry', YesNoIndicator, False)

	@property
	def RsdlCsh(self):
		return self._RsdlCsh

	@RsdlCsh.setter
	def RsdlCsh(self, value):
		self._RsdlCsh = value if value is not None else base_types.UninitialisedField(self, 'RsdlCsh', ResidualCash1, True)

	@RsdlCsh.deleter
	def RsdlCsh(self):
		del self._RsdlCsh
		self._RsdlCsh = base_types.UninitialisedField(self, 'RsdlCsh', ResidualCash1, True)

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
		base_types.FieldEntry(name='FinInstrmAsstForTrf', type=FinancialInstrument99, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtfl', type=FundPortfolio7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlDscvry', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsdlCsh', type=ResidualCash1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfConfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))