from . import base_types
from .Number import Number
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .GenericInformation1 import GenericInformation1
from .PercentageRate import PercentageRate
from .CheckCodeLine1Code import CheckCodeLine1Code
from .ActiveCurrencyCode import ActiveCurrencyCode
from .Max70Text import Max70Text
from .ATMMediaStatus1Code import ATMMediaStatus1Code

class ATMDepositedMediaItem1(base_types._BaseFieldType):

	__slots__ = ["_CdLine", "_MdiaId", "_Cnt", "_ScnndVal", "_CnfdncLvl", "_UnitVal", "_CdLineFrmt", "_RjctdRsn", "_AddtlData", "_Ccy", "_MdiaSts", "_Ref"]
	@property
	def CdLine(self):
		return self._CdLine

	@CdLine.setter
	def CdLine(self, value):
		self._CdLine = value if type(value) != base_types.auto else self.make_default("CdLine")

	@CdLine.deleter
	def CdLine(self):
		del self._CdLine
		self._CdLine = None

	@property
	def MdiaId(self):
		return self._MdiaId

	@MdiaId.setter
	def MdiaId(self, value):
		self._MdiaId = value if type(value) != base_types.auto else self.make_default("MdiaId")

	@MdiaId.deleter
	def MdiaId(self):
		del self._MdiaId
		self._MdiaId = None

	@property
	def Cnt(self):
		return self._Cnt

	@Cnt.setter
	def Cnt(self, value):
		self._Cnt = value if type(value) != base_types.auto else self.make_default("Cnt")

	@Cnt.deleter
	def Cnt(self):
		del self._Cnt
		self._Cnt = None

	@property
	def ScnndVal(self):
		return self._ScnndVal

	@ScnndVal.setter
	def ScnndVal(self, value):
		self._ScnndVal = value if type(value) != base_types.auto else self.make_default("ScnndVal")

	@ScnndVal.deleter
	def ScnndVal(self):
		del self._ScnndVal
		self._ScnndVal = None

	@property
	def CnfdncLvl(self):
		return self._CnfdncLvl

	@CnfdncLvl.setter
	def CnfdncLvl(self, value):
		self._CnfdncLvl = value if type(value) != base_types.auto else self.make_default("CnfdncLvl")

	@CnfdncLvl.deleter
	def CnfdncLvl(self):
		del self._CnfdncLvl
		self._CnfdncLvl = None

	@property
	def UnitVal(self):
		return self._UnitVal

	@UnitVal.setter
	def UnitVal(self, value):
		self._UnitVal = value if type(value) != base_types.auto else self.make_default("UnitVal")

	@UnitVal.deleter
	def UnitVal(self):
		del self._UnitVal
		self._UnitVal = None

	@property
	def CdLineFrmt(self):
		return self._CdLineFrmt

	@CdLineFrmt.setter
	def CdLineFrmt(self, value):
		self._CdLineFrmt = value if type(value) != base_types.auto else self.make_default("CdLineFrmt")

	@CdLineFrmt.deleter
	def CdLineFrmt(self):
		del self._CdLineFrmt
		self._CdLineFrmt = None

	@property
	def RjctdRsn(self):
		return self._RjctdRsn

	@RjctdRsn.setter
	def RjctdRsn(self, value):
		self._RjctdRsn = value if type(value) != base_types.auto else self.make_default("RjctdRsn")

	@RjctdRsn.deleter
	def RjctdRsn(self):
		del self._RjctdRsn
		self._RjctdRsn = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def MdiaSts(self):
		return self._MdiaSts

	@MdiaSts.setter
	def MdiaSts(self, value):
		self._MdiaSts = value if type(value) != base_types.auto else self.make_default("MdiaSts")

	@MdiaSts.deleter
	def MdiaSts(self):
		del self._MdiaSts
		self._MdiaSts = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdLine', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScnndVal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnfdncLvl', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitVal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdLineFrmt', type=CheckCodeLine1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdRsn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=GenericInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaSts', type=ATMMediaStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

