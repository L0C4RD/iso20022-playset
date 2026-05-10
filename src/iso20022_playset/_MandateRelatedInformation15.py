from . import base_types
from ._AmendmentInformationDetails14 import AmendmentInformationDetails14
from ._Exact2NumericText import Exact2NumericText
from ._Frequency36Choice import Frequency36Choice
from ._ISODate import ISODate
from ._MandateSetupReason1Choice import MandateSetupReason1Choice
from ._Max1025Text import Max1025Text
from ._Max35Text import Max35Text
from ._TrueFalseIndicator import TrueFalseIndicator

class MandateRelatedInformation15(base_types._BaseFieldType):

	__slots__ = ["_AmdmntInd", "_AmdmntInfDtls", "_DtOfSgntr", "_ElctrncSgntr", "_FnlColltnDt", "_Frqcy", "_FrstColltnDt", "_MndtId", "_Rsn", "_TrckgDays"]
	@property
	def AmdmntInd(self):
		return self._AmdmntInd

	@AmdmntInd.setter
	def AmdmntInd(self, value):
		self._AmdmntInd = value if type(value) != base_types.auto else self.make_default("AmdmntInd")

	@AmdmntInd.deleter
	def AmdmntInd(self):
		del self._AmdmntInd
		self._AmdmntInd = None

	@property
	def AmdmntInfDtls(self):
		return self._AmdmntInfDtls

	@AmdmntInfDtls.setter
	def AmdmntInfDtls(self, value):
		self._AmdmntInfDtls = value if type(value) != base_types.auto else self.make_default("AmdmntInfDtls")

	@AmdmntInfDtls.deleter
	def AmdmntInfDtls(self):
		del self._AmdmntInfDtls
		self._AmdmntInfDtls = None

	@property
	def DtOfSgntr(self):
		return self._DtOfSgntr

	@DtOfSgntr.setter
	def DtOfSgntr(self, value):
		self._DtOfSgntr = value if type(value) != base_types.auto else self.make_default("DtOfSgntr")

	@DtOfSgntr.deleter
	def DtOfSgntr(self):
		del self._DtOfSgntr
		self._DtOfSgntr = None

	@property
	def ElctrncSgntr(self):
		return self._ElctrncSgntr

	@ElctrncSgntr.setter
	def ElctrncSgntr(self, value):
		self._ElctrncSgntr = value if type(value) != base_types.auto else self.make_default("ElctrncSgntr")

	@ElctrncSgntr.deleter
	def ElctrncSgntr(self):
		del self._ElctrncSgntr
		self._ElctrncSgntr = None

	@property
	def FnlColltnDt(self):
		return self._FnlColltnDt

	@FnlColltnDt.setter
	def FnlColltnDt(self, value):
		self._FnlColltnDt = value if type(value) != base_types.auto else self.make_default("FnlColltnDt")

	@FnlColltnDt.deleter
	def FnlColltnDt(self):
		del self._FnlColltnDt
		self._FnlColltnDt = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	@property
	def FrstColltnDt(self):
		return self._FrstColltnDt

	@FrstColltnDt.setter
	def FrstColltnDt(self, value):
		self._FrstColltnDt = value if type(value) != base_types.auto else self.make_default("FrstColltnDt")

	@FrstColltnDt.deleter
	def FrstColltnDt(self):
		del self._FrstColltnDt
		self._FrstColltnDt = None

	@property
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if type(value) != base_types.auto else self.make_default("MndtId")

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def TrckgDays(self):
		return self._TrckgDays

	@TrckgDays.setter
	def TrckgDays(self, value):
		self._TrckgDays = value if type(value) != base_types.auto else self.make_default("TrckgDays")

	@TrckgDays.deleter
	def TrckgDays(self):
		del self._TrckgDays
		self._TrckgDays = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntInfDtls', type=AmendmentInformationDetails14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfSgntr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncSgntr', type=Max1025Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=MandateSetupReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckgDays', type=Exact2NumericText, min=0, max=1, mutex_group=None, array=False),
	))

