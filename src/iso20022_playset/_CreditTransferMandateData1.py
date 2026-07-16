# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Frequency36Choice
from . import ISODate
from . import ISODateTime
from . import MandateSetupReason1Choice
from . import MandateTypeInformation2
from . import Max10KBinary
from . import Max35Text

class CreditTransferMandateData1(base_types._BaseFieldType):

	__slots__ = ["_DtOfSgntr", "_DtOfVrfctn", "_ElctrncSgntr", "_FnlPmtDt", "_Frqcy", "_FrstPmtDt", "_MndtId", "_Rsn", "_Tp"]
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
	def DtOfVrfctn(self):
		return self._DtOfVrfctn

	@DtOfVrfctn.setter
	def DtOfVrfctn(self, value):
		self._DtOfVrfctn = value if value is not None else base_types.UninitialisedField(self, 'DtOfVrfctn', ISODateTime, False)

	@DtOfVrfctn.deleter
	def DtOfVrfctn(self):
		del self._DtOfVrfctn
		self._DtOfVrfctn = base_types.UninitialisedField(self, 'DtOfVrfctn', ISODateTime, False)

	@property
	def ElctrncSgntr(self):
		return self._ElctrncSgntr

	@ElctrncSgntr.setter
	def ElctrncSgntr(self, value):
		self._ElctrncSgntr = value if value is not None else base_types.UninitialisedField(self, 'ElctrncSgntr', Max10KBinary, False)

	@ElctrncSgntr.deleter
	def ElctrncSgntr(self):
		del self._ElctrncSgntr
		self._ElctrncSgntr = base_types.UninitialisedField(self, 'ElctrncSgntr', Max10KBinary, False)

	@property
	def FnlPmtDt(self):
		return self._FnlPmtDt

	@FnlPmtDt.setter
	def FnlPmtDt(self, value):
		self._FnlPmtDt = value if value is not None else base_types.UninitialisedField(self, 'FnlPmtDt', ISODate, False)

	@FnlPmtDt.deleter
	def FnlPmtDt(self):
		del self._FnlPmtDt
		self._FnlPmtDt = base_types.UninitialisedField(self, 'FnlPmtDt', ISODate, False)

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
	def FrstPmtDt(self):
		return self._FrstPmtDt

	@FrstPmtDt.setter
	def FrstPmtDt(self, value):
		self._FrstPmtDt = value if value is not None else base_types.UninitialisedField(self, 'FrstPmtDt', ISODate, False)

	@FrstPmtDt.deleter
	def FrstPmtDt(self):
		del self._FrstPmtDt
		self._FrstPmtDt = base_types.UninitialisedField(self, 'FrstPmtDt', ISODate, False)

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', MandateTypeInformation2, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', MandateTypeInformation2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtOfSgntr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfVrfctn', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElctrncSgntr', type=Max10KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlPmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency36Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstPmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=MandateSetupReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MandateTypeInformation2, min=0, max=1, mutex_group=None, array=False),
	))