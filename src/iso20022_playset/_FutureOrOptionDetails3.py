from . import base_types
from ._DateAndDateTime1Choice import DateAndDateTime1Choice
from ._UnderlyingRatio2 import UnderlyingRatio2
from ._Rating1 import Rating1
from ._YesNoIndicator import YesNoIndicator
from ._OptionRight2Choice import OptionRight2Choice
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Price14 import Price14
from ._Number import Number
from ._Max256Text import Max256Text
from ._FutureAndOptionContractType1Code import FutureAndOptionContractType1Code
from ._ISOYearMonth import ISOYearMonth
from ._Appearance1Code import Appearance1Code
from ._ISODateTime import ISODateTime
from ._UnitOfMeasure1Code import UnitOfMeasure1Code

class FutureOrOptionDetails3(base_types._BaseFieldType):

	__slots__ = ["_AnncmntDt", "_StrpblInd", "_FutrDt", "_MinSz", "_Ratg", "_IssePric", "_SprdTx", "_UnitOfMeasr", "_OptnRghts", "_LastDlvryDt", "_NearTermPosLmt", "_CtrctSttlmMnth", "_FrstDealgDt", "_PosLmt", "_Ratio", "_Purp", "_LastTx", "_Apprnc", "_FutrAndOptnCtrctTp", "_MinTradgPricgIncrmt"]
	@property
	def AnncmntDt(self):
		return self._AnncmntDt

	@AnncmntDt.setter
	def AnncmntDt(self, value):
		self._AnncmntDt = value if type(value) != base_types.auto else self.make_default("AnncmntDt")

	@AnncmntDt.deleter
	def AnncmntDt(self):
		del self._AnncmntDt
		self._AnncmntDt = None

	@property
	def Apprnc(self):
		return self._Apprnc

	@Apprnc.setter
	def Apprnc(self, value):
		self._Apprnc = value if type(value) != base_types.auto else self.make_default("Apprnc")

	@Apprnc.deleter
	def Apprnc(self):
		del self._Apprnc
		self._Apprnc = None

	@property
	def CtrctSttlmMnth(self):
		return self._CtrctSttlmMnth

	@CtrctSttlmMnth.setter
	def CtrctSttlmMnth(self, value):
		self._CtrctSttlmMnth = value if type(value) != base_types.auto else self.make_default("CtrctSttlmMnth")

	@CtrctSttlmMnth.deleter
	def CtrctSttlmMnth(self):
		del self._CtrctSttlmMnth
		self._CtrctSttlmMnth = None

	@property
	def FrstDealgDt(self):
		return self._FrstDealgDt

	@FrstDealgDt.setter
	def FrstDealgDt(self, value):
		self._FrstDealgDt = value if type(value) != base_types.auto else self.make_default("FrstDealgDt")

	@FrstDealgDt.deleter
	def FrstDealgDt(self):
		del self._FrstDealgDt
		self._FrstDealgDt = None

	@property
	def FutrAndOptnCtrctTp(self):
		return self._FutrAndOptnCtrctTp

	@FutrAndOptnCtrctTp.setter
	def FutrAndOptnCtrctTp(self, value):
		self._FutrAndOptnCtrctTp = value if type(value) != base_types.auto else self.make_default("FutrAndOptnCtrctTp")

	@FutrAndOptnCtrctTp.deleter
	def FutrAndOptnCtrctTp(self):
		del self._FutrAndOptnCtrctTp
		self._FutrAndOptnCtrctTp = None

	@property
	def FutrDt(self):
		return self._FutrDt

	@FutrDt.setter
	def FutrDt(self, value):
		self._FutrDt = value if type(value) != base_types.auto else self.make_default("FutrDt")

	@FutrDt.deleter
	def FutrDt(self):
		del self._FutrDt
		self._FutrDt = None

	@property
	def IssePric(self):
		return self._IssePric

	@IssePric.setter
	def IssePric(self, value):
		self._IssePric = value if type(value) != base_types.auto else self.make_default("IssePric")

	@IssePric.deleter
	def IssePric(self):
		del self._IssePric
		self._IssePric = None

	@property
	def LastDlvryDt(self):
		return self._LastDlvryDt

	@LastDlvryDt.setter
	def LastDlvryDt(self, value):
		self._LastDlvryDt = value if type(value) != base_types.auto else self.make_default("LastDlvryDt")

	@LastDlvryDt.deleter
	def LastDlvryDt(self):
		del self._LastDlvryDt
		self._LastDlvryDt = None

	@property
	def LastTx(self):
		return self._LastTx

	@LastTx.setter
	def LastTx(self, value):
		self._LastTx = value if type(value) != base_types.auto else self.make_default("LastTx")

	@LastTx.deleter
	def LastTx(self):
		del self._LastTx
		self._LastTx = None

	@property
	def MinSz(self):
		return self._MinSz

	@MinSz.setter
	def MinSz(self, value):
		self._MinSz = value if type(value) != base_types.auto else self.make_default("MinSz")

	@MinSz.deleter
	def MinSz(self):
		del self._MinSz
		self._MinSz = None

	@property
	def MinTradgPricgIncrmt(self):
		return self._MinTradgPricgIncrmt

	@MinTradgPricgIncrmt.setter
	def MinTradgPricgIncrmt(self, value):
		self._MinTradgPricgIncrmt = value if type(value) != base_types.auto else self.make_default("MinTradgPricgIncrmt")

	@MinTradgPricgIncrmt.deleter
	def MinTradgPricgIncrmt(self):
		del self._MinTradgPricgIncrmt
		self._MinTradgPricgIncrmt = None

	@property
	def NearTermPosLmt(self):
		return self._NearTermPosLmt

	@NearTermPosLmt.setter
	def NearTermPosLmt(self, value):
		self._NearTermPosLmt = value if type(value) != base_types.auto else self.make_default("NearTermPosLmt")

	@NearTermPosLmt.deleter
	def NearTermPosLmt(self):
		del self._NearTermPosLmt
		self._NearTermPosLmt = None

	@property
	def OptnRghts(self):
		return self._OptnRghts

	@OptnRghts.setter
	def OptnRghts(self, value):
		self._OptnRghts = value if type(value) != base_types.auto else self.make_default("OptnRghts")

	@OptnRghts.deleter
	def OptnRghts(self):
		del self._OptnRghts
		self._OptnRghts = None

	@property
	def PosLmt(self):
		return self._PosLmt

	@PosLmt.setter
	def PosLmt(self, value):
		self._PosLmt = value if type(value) != base_types.auto else self.make_default("PosLmt")

	@PosLmt.deleter
	def PosLmt(self):
		del self._PosLmt
		self._PosLmt = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != base_types.auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def Ratg(self):
		return self._Ratg

	@Ratg.setter
	def Ratg(self, value):
		self._Ratg = value if type(value) != base_types.auto else self.make_default("Ratg")

	@Ratg.deleter
	def Ratg(self):
		del self._Ratg
		self._Ratg = None

	@property
	def Ratio(self):
		return self._Ratio

	@Ratio.setter
	def Ratio(self, value):
		self._Ratio = value if type(value) != base_types.auto else self.make_default("Ratio")

	@Ratio.deleter
	def Ratio(self):
		del self._Ratio
		self._Ratio = None

	@property
	def SprdTx(self):
		return self._SprdTx

	@SprdTx.setter
	def SprdTx(self, value):
		self._SprdTx = value if type(value) != base_types.auto else self.make_default("SprdTx")

	@SprdTx.deleter
	def SprdTx(self):
		del self._SprdTx
		self._SprdTx = None

	@property
	def StrpblInd(self):
		return self._StrpblInd

	@StrpblInd.setter
	def StrpblInd(self, value):
		self._StrpblInd = value if type(value) != base_types.auto else self.make_default("StrpblInd")

	@StrpblInd.deleter
	def StrpblInd(self):
		del self._StrpblInd
		self._StrpblInd = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != base_types.auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnncmntDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Apprnc', type=Appearance1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctSttlmMnth', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstDealgDt', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FutrAndOptnCtrctTp', type=FutureAndOptionContractType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FutrDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssePric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastDlvryDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastTx', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinSz', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinTradgPricgIncrmt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NearTermPosLmt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnRghts', type=OptionRight2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PosLmt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ratg', type=Rating1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ratio', type=UnderlyingRatio2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SprdTx', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrpblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure1Code, min=0, max=1, mutex_group=None, array=False),
	))

