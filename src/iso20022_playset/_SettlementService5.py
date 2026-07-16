# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import ISODate
from . import ISODateTime
from . import ISOTime
from . import Max35Text
from . import TrueFalseIndicator

class SettlementService5(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CutOffTm", "_Dfrrd", "_Dt", "_Id", "_Prd", "_PropsdId", "_PropsdTp", "_ReqdDt", "_RptgNttyId", "_RptgNttyTp", "_Tm", "_Tp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalData1, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalData1, True)

	@property
	def CutOffTm(self):
		return self._CutOffTm

	@CutOffTm.setter
	def CutOffTm(self, value):
		self._CutOffTm = value if value is not None else base_types.UninitialisedField(self, 'CutOffTm', ISODateTime, False)

	@CutOffTm.deleter
	def CutOffTm(self):
		del self._CutOffTm
		self._CutOffTm = base_types.UninitialisedField(self, 'CutOffTm', ISODateTime, False)

	@property
	def Dfrrd(self):
		return self._Dfrrd

	@Dfrrd.setter
	def Dfrrd(self, value):
		self._Dfrrd = value if value is not None else base_types.UninitialisedField(self, 'Dfrrd', TrueFalseIndicator, False)

	@Dfrrd.deleter
	def Dfrrd(self):
		del self._Dfrrd
		self._Dfrrd = base_types.UninitialisedField(self, 'Dfrrd', TrueFalseIndicator, False)

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', Max35Text, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', Max35Text, False)

	@property
	def PropsdId(self):
		return self._PropsdId

	@PropsdId.setter
	def PropsdId(self, value):
		self._PropsdId = value if value is not None else base_types.UninitialisedField(self, 'PropsdId', Max35Text, False)

	@PropsdId.deleter
	def PropsdId(self):
		del self._PropsdId
		self._PropsdId = base_types.UninitialisedField(self, 'PropsdId', Max35Text, False)

	@property
	def PropsdTp(self):
		return self._PropsdTp

	@PropsdTp.setter
	def PropsdTp(self, value):
		self._PropsdTp = value if value is not None else base_types.UninitialisedField(self, 'PropsdTp', Max35Text, False)

	@PropsdTp.deleter
	def PropsdTp(self):
		del self._PropsdTp
		self._PropsdTp = base_types.UninitialisedField(self, 'PropsdTp', Max35Text, False)

	@property
	def ReqdDt(self):
		return self._ReqdDt

	@ReqdDt.setter
	def ReqdDt(self, value):
		self._ReqdDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdDt', ISODate, False)

	@ReqdDt.deleter
	def ReqdDt(self):
		del self._ReqdDt
		self._ReqdDt = base_types.UninitialisedField(self, 'ReqdDt', ISODate, False)

	@property
	def RptgNttyId(self):
		return self._RptgNttyId

	@RptgNttyId.setter
	def RptgNttyId(self, value):
		self._RptgNttyId = value if value is not None else base_types.UninitialisedField(self, 'RptgNttyId', Max35Text, False)

	@RptgNttyId.deleter
	def RptgNttyId(self):
		del self._RptgNttyId
		self._RptgNttyId = base_types.UninitialisedField(self, 'RptgNttyId', Max35Text, False)

	@property
	def RptgNttyTp(self):
		return self._RptgNttyTp

	@RptgNttyTp.setter
	def RptgNttyTp(self, value):
		self._RptgNttyTp = value if value is not None else base_types.UninitialisedField(self, 'RptgNttyTp', Max35Text, False)

	@RptgNttyTp.deleter
	def RptgNttyTp(self):
		del self._RptgNttyTp
		self._RptgNttyTp = base_types.UninitialisedField(self, 'RptgNttyTp', Max35Text, False)

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if value is not None else base_types.UninitialisedField(self, 'Tm', ISOTime, False)

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = base_types.UninitialisedField(self, 'Tm', ISOTime, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CutOffTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dfrrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNttyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgNttyTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))