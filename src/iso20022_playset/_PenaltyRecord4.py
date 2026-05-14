from . import base_types
from ._AmountAndDirection5 import AmountAndDirection5
from ._Number import Number
from ._PenaltyCalculationMethod1Code import PenaltyCalculationMethod1Code
from ._PenaltyCalculationRecord1 import PenaltyCalculationRecord1
from ._PenaltyIdentification1 import PenaltyIdentification1
from ._PenaltyStatus2 import PenaltyStatus2
from ._PenaltyTransaction3 import PenaltyTransaction3
from ._PenaltyType1Code import PenaltyType1Code
from ._YesNoIndicator import YesNoIndicator

class PenaltyRecord4(base_types._BaseFieldType):

	__slots__ = ["_ClctnData", "_ClctnMtd", "_CmptdAmt", "_Id", "_Inslvncy", "_NbOfDays", "_RltdTx", "_Sts", "_Tp"]
	@property
	def ClctnData(self):
		return self._ClctnData

	@ClctnData.setter
	def ClctnData(self, value):
		self._ClctnData = value if type(value) != base_types.auto else self.make_default("ClctnData")

	@ClctnData.deleter
	def ClctnData(self):
		del self._ClctnData
		self._ClctnData = None

	@property
	def ClctnMtd(self):
		return self._ClctnMtd

	@ClctnMtd.setter
	def ClctnMtd(self, value):
		self._ClctnMtd = value if type(value) != base_types.auto else self.make_default("ClctnMtd")

	@ClctnMtd.deleter
	def ClctnMtd(self):
		del self._ClctnMtd
		self._ClctnMtd = None

	@property
	def CmptdAmt(self):
		return self._CmptdAmt

	@CmptdAmt.setter
	def CmptdAmt(self, value):
		self._CmptdAmt = value if type(value) != base_types.auto else self.make_default("CmptdAmt")

	@CmptdAmt.deleter
	def CmptdAmt(self):
		del self._CmptdAmt
		self._CmptdAmt = None

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
	def Inslvncy(self):
		return self._Inslvncy

	@Inslvncy.setter
	def Inslvncy(self, value):
		self._Inslvncy = value if type(value) != base_types.auto else self.make_default("Inslvncy")

	@Inslvncy.deleter
	def Inslvncy(self):
		del self._Inslvncy
		self._Inslvncy = None

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if type(value) != base_types.auto else self.make_default("NbOfDays")

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = None

	@property
	def RltdTx(self):
		return self._RltdTx

	@RltdTx.setter
	def RltdTx(self, value):
		self._RltdTx = value if type(value) != base_types.auto else self.make_default("RltdTx")

	@RltdTx.deleter
	def RltdTx(self):
		del self._RltdTx
		self._RltdTx = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

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
		base_types.FieldEntry(name='ClctnData', type=PenaltyCalculationRecord1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClctnMtd', type=PenaltyCalculationMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CmptdAmt', type=AmountAndDirection5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PenaltyIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Inslvncy', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdTx', type=PenaltyTransaction3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=PenaltyStatus2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PenaltyType1Code, min=1, max=1, mutex_group=None, array=False),
	))

