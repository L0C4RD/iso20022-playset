from . import base_types
from ._Frequency36Choice import Frequency36Choice
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime
from ._MandateSetupReason1Choice import MandateSetupReason1Choice
from ._MandateTypeInformation2 import MandateTypeInformation2
from ._Max10KBinary import Max10KBinary
from ._Max35Text import Max35Text

class CreditTransferMandateData1(base_types._BaseFieldType):

	__slots__ = ["_DtOfSgntr", "_DtOfVrfctn", "_ElctrncSgntr", "_FnlPmtDt", "_Frqcy", "_FrstPmtDt", "_MndtId", "_Rsn", "_Tp"]
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
	def DtOfVrfctn(self):
		return self._DtOfVrfctn

	@DtOfVrfctn.setter
	def DtOfVrfctn(self, value):
		self._DtOfVrfctn = value if type(value) != base_types.auto else self.make_default("DtOfVrfctn")

	@DtOfVrfctn.deleter
	def DtOfVrfctn(self):
		del self._DtOfVrfctn
		self._DtOfVrfctn = None

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
	def FnlPmtDt(self):
		return self._FnlPmtDt

	@FnlPmtDt.setter
	def FnlPmtDt(self, value):
		self._FnlPmtDt = value if type(value) != base_types.auto else self.make_default("FnlPmtDt")

	@FnlPmtDt.deleter
	def FnlPmtDt(self):
		del self._FnlPmtDt
		self._FnlPmtDt = None

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
	def FrstPmtDt(self):
		return self._FrstPmtDt

	@FrstPmtDt.setter
	def FrstPmtDt(self, value):
		self._FrstPmtDt = value if type(value) != base_types.auto else self.make_default("FrstPmtDt")

	@FrstPmtDt.deleter
	def FrstPmtDt(self):
		del self._FrstPmtDt
		self._FrstPmtDt = None

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
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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

