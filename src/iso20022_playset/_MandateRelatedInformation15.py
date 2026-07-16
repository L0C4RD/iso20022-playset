# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmendmentInformationDetails14
from . import Exact2NumericText
from . import Frequency36Choice
from . import ISODate
from . import MandateSetupReason1Choice
from . import Max1025Text
from . import Max35Text
from . import TrueFalseIndicator

class MandateRelatedInformation15(base_types._BaseFieldType):

	__slots__ = ["_AmdmntInd", "_AmdmntInfDtls", "_DtOfSgntr", "_ElctrncSgntr", "_FnlColltnDt", "_Frqcy", "_FrstColltnDt", "_MndtId", "_Rsn", "_TrckgDays"]
	@property
	def AmdmntInd(self):
		return self._AmdmntInd

	@AmdmntInd.setter
	def AmdmntInd(self, value):
		self._AmdmntInd = value if value is not None else base_types.UninitialisedField(self, 'AmdmntInd', TrueFalseIndicator, False)

	@AmdmntInd.deleter
	def AmdmntInd(self):
		del self._AmdmntInd
		self._AmdmntInd = base_types.UninitialisedField(self, 'AmdmntInd', TrueFalseIndicator, False)

	@property
	def AmdmntInfDtls(self):
		return self._AmdmntInfDtls

	@AmdmntInfDtls.setter
	def AmdmntInfDtls(self, value):
		self._AmdmntInfDtls = value if value is not None else base_types.UninitialisedField(self, 'AmdmntInfDtls', AmendmentInformationDetails14, False)

	@AmdmntInfDtls.deleter
	def AmdmntInfDtls(self):
		del self._AmdmntInfDtls
		self._AmdmntInfDtls = base_types.UninitialisedField(self, 'AmdmntInfDtls', AmendmentInformationDetails14, False)

	@property
	def DtOfSgntr(self):
		return self._DtOfSgntr

	@DtOfSgntr.setter
	def DtOfSgntr(self, value):
		self._DtOfSgntr = value if value is not None else base_types.UninitialisedField(self, 'DtOfSgntr', ISODate, False)

	@DtOfSgntr.deleter
	def DtOfSgntr(self):
		del self._DtOfSgntr
		self._DtOfSgntr = base_types.UninitialisedField(self, 'DtOfSgntr', ISODate, False)

	@property
	def ElctrncSgntr(self):
		return self._ElctrncSgntr

	@ElctrncSgntr.setter
	def ElctrncSgntr(self, value):
		self._ElctrncSgntr = value if value is not None else base_types.UninitialisedField(self, 'ElctrncSgntr', Max1025Text, False)

	@ElctrncSgntr.deleter
	def ElctrncSgntr(self):
		del self._ElctrncSgntr
		self._ElctrncSgntr = base_types.UninitialisedField(self, 'ElctrncSgntr', Max1025Text, False)

	@property
	def FnlColltnDt(self):
		return self._FnlColltnDt

	@FnlColltnDt.setter
	def FnlColltnDt(self, value):
		self._FnlColltnDt = value if value is not None else base_types.UninitialisedField(self, 'FnlColltnDt', ISODate, False)

	@FnlColltnDt.deleter
	def FnlColltnDt(self):
		del self._FnlColltnDt
		self._FnlColltnDt = base_types.UninitialisedField(self, 'FnlColltnDt', ISODate, False)

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency36Choice, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency36Choice, False)

	@property
	def FrstColltnDt(self):
		return self._FrstColltnDt

	@FrstColltnDt.setter
	def FrstColltnDt(self, value):
		self._FrstColltnDt = value if value is not None else base_types.UninitialisedField(self, 'FrstColltnDt', ISODate, False)

	@FrstColltnDt.deleter
	def FrstColltnDt(self):
		del self._FrstColltnDt
		self._FrstColltnDt = base_types.UninitialisedField(self, 'FrstColltnDt', ISODate, False)

	@property
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if value is not None else base_types.UninitialisedField(self, 'MndtId', Max35Text, False)

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = base_types.UninitialisedField(self, 'MndtId', Max35Text, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', MandateSetupReason1Choice, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', MandateSetupReason1Choice, False)

	@property
	def TrckgDays(self):
		return self._TrckgDays

	@TrckgDays.setter
	def TrckgDays(self, value):
		self._TrckgDays = value if value is not None else base_types.UninitialisedField(self, 'TrckgDays', Exact2NumericText, False)

	@TrckgDays.deleter
	def TrckgDays(self):
		del self._TrckgDays
		self._TrckgDays = base_types.UninitialisedField(self, 'TrckgDays', Exact2NumericText, False)

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