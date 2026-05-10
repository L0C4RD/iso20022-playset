from . import base_types
from ._ISODate import ISODate
from ._TrueFalseIndicator import TrueFalseIndicator
from ._ISOTime import ISOTime
from ._Max35Text import Max35Text
from ._ISODateTime import ISODateTime
from ._AdditionalData1 import AdditionalData1

class SettlementService6(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_AddtlInf", "_Dfrrd", "_RptgNttyTp", "_RptgNttyId", "_Prd", "_CutOffTm", "_Tm", "_Id", "_Tp", "_ReqdDt"]
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
	def CutOffTm(self):
		return self._CutOffTm

	@CutOffTm.setter
	def CutOffTm(self, value):
		self._CutOffTm = value if type(value) != base_types.auto else self.make_default("CutOffTm")

	@CutOffTm.deleter
	def CutOffTm(self):
		del self._CutOffTm
		self._CutOffTm = None

	@property
	def Dfrrd(self):
		return self._Dfrrd

	@Dfrrd.setter
	def Dfrrd(self, value):
		self._Dfrrd = value if type(value) != base_types.auto else self.make_default("Dfrrd")

	@Dfrrd.deleter
	def Dfrrd(self):
		del self._Dfrrd
		self._Dfrrd = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != base_types.auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def ReqdDt(self):
		return self._ReqdDt

	@ReqdDt.setter
	def ReqdDt(self, value):
		self._ReqdDt = value if type(value) != base_types.auto else self.make_default("ReqdDt")

	@ReqdDt.deleter
	def ReqdDt(self):
		del self._ReqdDt
		self._ReqdDt = None

	@property
	def RptgNttyId(self):
		return self._RptgNttyId

	@RptgNttyId.setter
	def RptgNttyId(self, value):
		self._RptgNttyId = value if type(value) != base_types.auto else self.make_default("RptgNttyId")

	@RptgNttyId.deleter
	def RptgNttyId(self):
		del self._RptgNttyId
		self._RptgNttyId = None

	@property
	def RptgNttyTp(self):
		return self._RptgNttyTp

	@RptgNttyTp.setter
	def RptgNttyTp(self, value):
		self._RptgNttyTp = value if type(value) != base_types.auto else self.make_default("RptgNttyTp")

	@RptgNttyTp.deleter
	def RptgNttyTp(self):
		del self._RptgNttyTp
		self._RptgNttyTp = None

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if type(value) != base_types.auto else self.make_default("Tm")

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = None

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
		base_types.FieldEntry(name='AddtlInf', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CutOffTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dfrrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNttyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNttyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

