from . import base_types
from ._AdditionalInformation15 import AdditionalInformation15
from ._FinancialInstrument99 import FinancialInstrument99
from ._FundPortfolio7Choice import FundPortfolio7Choice
from ._ISODate import ISODate
from ._Max35Text import Max35Text
from ._ResidualCash1 import ResidualCash1
from ._YesNoIndicator import YesNoIndicator

class PortfolioTransfer9(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_FinInstrmAsstForTrf", "_MstrRef", "_Prtfl", "_PrtlDscvry", "_RsdlCsh", "_TaxDt", "_TrfConfId", "_TrfId"]
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
	def FinInstrmAsstForTrf(self):
		return self._FinInstrmAsstForTrf

	@FinInstrmAsstForTrf.setter
	def FinInstrmAsstForTrf(self, value):
		self._FinInstrmAsstForTrf = value if type(value) != base_types.auto else self.make_default("FinInstrmAsstForTrf")

	@FinInstrmAsstForTrf.deleter
	def FinInstrmAsstForTrf(self):
		del self._FinInstrmAsstForTrf
		self._FinInstrmAsstForTrf = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != base_types.auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def Prtfl(self):
		return self._Prtfl

	@Prtfl.setter
	def Prtfl(self, value):
		self._Prtfl = value if type(value) != base_types.auto else self.make_default("Prtfl")

	@Prtfl.deleter
	def Prtfl(self):
		del self._Prtfl
		self._Prtfl = None

	@property
	def PrtlDscvry(self):
		return self._PrtlDscvry

	@PrtlDscvry.setter
	def PrtlDscvry(self, value):
		self._PrtlDscvry = value if type(value) != base_types.auto else self.make_default("PrtlDscvry")

	@PrtlDscvry.deleter
	def PrtlDscvry(self):
		del self._PrtlDscvry
		self._PrtlDscvry = None

	@property
	def RsdlCsh(self):
		return self._RsdlCsh

	@RsdlCsh.setter
	def RsdlCsh(self, value):
		self._RsdlCsh = value if type(value) != base_types.auto else self.make_default("RsdlCsh")

	@RsdlCsh.deleter
	def RsdlCsh(self):
		del self._RsdlCsh
		self._RsdlCsh = None

	@property
	def TaxDt(self):
		return self._TaxDt

	@TaxDt.setter
	def TaxDt(self, value):
		self._TaxDt = value if type(value) != base_types.auto else self.make_default("TaxDt")

	@TaxDt.deleter
	def TaxDt(self):
		del self._TaxDt
		self._TaxDt = None

	@property
	def TrfConfId(self):
		return self._TrfConfId

	@TrfConfId.setter
	def TrfConfId(self, value):
		self._TrfConfId = value if type(value) != base_types.auto else self.make_default("TrfConfId")

	@TrfConfId.deleter
	def TrfConfId(self):
		del self._TrfConfId
		self._TrfConfId = None

	@property
	def TrfId(self):
		return self._TrfId

	@TrfId.setter
	def TrfId(self, value):
		self._TrfId = value if type(value) != base_types.auto else self.make_default("TrfId")

	@TrfId.deleter
	def TrfId(self):
		del self._TrfId
		self._TrfId = None

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

