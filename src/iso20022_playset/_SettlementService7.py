from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime
from ._ISOTime import ISOTime
from ._Max35Text import Max35Text

class SettlementService7(base_types._BaseFieldType):

	__slots__ = ["_CutOffTm", "_DfrrdDt", "_Dt", "_Id", "_NtlData", "_Prd", "_PropsdId", "_PropsdTp", "_PrvtData", "_RptgNttyId", "_RptgNttyTp", "_Tm", "_Tp"]
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
	def DfrrdDt(self):
		return self._DfrrdDt

	@DfrrdDt.setter
	def DfrrdDt(self, value):
		self._DfrrdDt = value if type(value) != base_types.auto else self.make_default("DfrrdDt")

	@DfrrdDt.deleter
	def DfrrdDt(self):
		del self._DfrrdDt
		self._DfrrdDt = None

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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

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
	def PropsdId(self):
		return self._PropsdId

	@PropsdId.setter
	def PropsdId(self, value):
		self._PropsdId = value if type(value) != base_types.auto else self.make_default("PropsdId")

	@PropsdId.deleter
	def PropsdId(self):
		del self._PropsdId
		self._PropsdId = None

	@property
	def PropsdTp(self):
		return self._PropsdTp

	@PropsdTp.setter
	def PropsdTp(self, value):
		self._PropsdTp = value if type(value) != base_types.auto else self.make_default("PropsdTp")

	@PropsdTp.deleter
	def PropsdTp(self):
		del self._PropsdTp
		self._PropsdTp = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

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
		base_types.FieldEntry(name='CutOffTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfrrdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgNttyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNttyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

