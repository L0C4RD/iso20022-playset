# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Appearance1Code
from . import DateAndDateTime1Choice
from . import FutureAndOptionContractType1Code
from . import ISODateTime
from . import ISOYearMonth
from . import Max256Text
from . import Number
from . import OptionRight2Choice
from . import Price14
from . import Rating1
from . import UnderlyingRatio2
from . import UnitOfMeasure1Code
from . import YesNoIndicator

class FutureOrOptionDetails3(base_types._BaseFieldType):

	__slots__ = ["_AnncmntDt", "_Apprnc", "_CtrctSttlmMnth", "_FrstDealgDt", "_FutrAndOptnCtrctTp", "_FutrDt", "_IssePric", "_LastDlvryDt", "_LastTx", "_MinSz", "_MinTradgPricgIncrmt", "_NearTermPosLmt", "_OptnRghts", "_PosLmt", "_Purp", "_Ratg", "_Ratio", "_SprdTx", "_StrpblInd", "_UnitOfMeasr"]
	@property
	def AnncmntDt(self):
		return self._AnncmntDt

	@AnncmntDt.setter
	def AnncmntDt(self, value):
		self._AnncmntDt = value if value is not None else base_types.UninitialisedField(self, 'AnncmntDt', ISODateTime, False)

	@AnncmntDt.deleter
	def AnncmntDt(self):
		del self._AnncmntDt
		self._AnncmntDt = base_types.UninitialisedField(self, 'AnncmntDt', ISODateTime, False)

	@property
	def Apprnc(self):
		return self._Apprnc

	@Apprnc.setter
	def Apprnc(self, value):
		self._Apprnc = value if value is not None else base_types.UninitialisedField(self, 'Apprnc', Appearance1Code, False)

	@Apprnc.deleter
	def Apprnc(self):
		del self._Apprnc
		self._Apprnc = base_types.UninitialisedField(self, 'Apprnc', Appearance1Code, False)

	@property
	def CtrctSttlmMnth(self):
		return self._CtrctSttlmMnth

	@CtrctSttlmMnth.setter
	def CtrctSttlmMnth(self, value):
		self._CtrctSttlmMnth = value if value is not None else base_types.UninitialisedField(self, 'CtrctSttlmMnth', ISOYearMonth, False)

	@CtrctSttlmMnth.deleter
	def CtrctSttlmMnth(self):
		del self._CtrctSttlmMnth
		self._CtrctSttlmMnth = base_types.UninitialisedField(self, 'CtrctSttlmMnth', ISOYearMonth, False)

	@property
	def FrstDealgDt(self):
		return self._FrstDealgDt

	@FrstDealgDt.setter
	def FrstDealgDt(self, value):
		self._FrstDealgDt = value if value is not None else base_types.UninitialisedField(self, 'FrstDealgDt', DateAndDateTime1Choice, False)

	@FrstDealgDt.deleter
	def FrstDealgDt(self):
		del self._FrstDealgDt
		self._FrstDealgDt = base_types.UninitialisedField(self, 'FrstDealgDt', DateAndDateTime1Choice, False)

	@property
	def FutrAndOptnCtrctTp(self):
		return self._FutrAndOptnCtrctTp

	@FutrAndOptnCtrctTp.setter
	def FutrAndOptnCtrctTp(self, value):
		self._FutrAndOptnCtrctTp = value if value is not None else base_types.UninitialisedField(self, 'FutrAndOptnCtrctTp', FutureAndOptionContractType1Code, False)

	@FutrAndOptnCtrctTp.deleter
	def FutrAndOptnCtrctTp(self):
		del self._FutrAndOptnCtrctTp
		self._FutrAndOptnCtrctTp = base_types.UninitialisedField(self, 'FutrAndOptnCtrctTp', FutureAndOptionContractType1Code, False)

	@property
	def FutrDt(self):
		return self._FutrDt

	@FutrDt.setter
	def FutrDt(self, value):
		self._FutrDt = value if value is not None else base_types.UninitialisedField(self, 'FutrDt', ISODateTime, False)

	@FutrDt.deleter
	def FutrDt(self):
		del self._FutrDt
		self._FutrDt = base_types.UninitialisedField(self, 'FutrDt', ISODateTime, False)

	@property
	def IssePric(self):
		return self._IssePric

	@IssePric.setter
	def IssePric(self, value):
		self._IssePric = value if value is not None else base_types.UninitialisedField(self, 'IssePric', Price14, False)

	@IssePric.deleter
	def IssePric(self):
		del self._IssePric
		self._IssePric = base_types.UninitialisedField(self, 'IssePric', Price14, False)

	@property
	def LastDlvryDt(self):
		return self._LastDlvryDt

	@LastDlvryDt.setter
	def LastDlvryDt(self, value):
		self._LastDlvryDt = value if value is not None else base_types.UninitialisedField(self, 'LastDlvryDt', ISODateTime, False)

	@LastDlvryDt.deleter
	def LastDlvryDt(self):
		del self._LastDlvryDt
		self._LastDlvryDt = base_types.UninitialisedField(self, 'LastDlvryDt', ISODateTime, False)

	@property
	def LastTx(self):
		return self._LastTx

	@LastTx.setter
	def LastTx(self, value):
		self._LastTx = value if value is not None else base_types.UninitialisedField(self, 'LastTx', YesNoIndicator, False)

	@LastTx.deleter
	def LastTx(self):
		del self._LastTx
		self._LastTx = base_types.UninitialisedField(self, 'LastTx', YesNoIndicator, False)

	@property
	def MinSz(self):
		return self._MinSz

	@MinSz.setter
	def MinSz(self, value):
		self._MinSz = value if value is not None else base_types.UninitialisedField(self, 'MinSz', ActiveCurrencyAndAmount, False)

	@MinSz.deleter
	def MinSz(self):
		del self._MinSz
		self._MinSz = base_types.UninitialisedField(self, 'MinSz', ActiveCurrencyAndAmount, False)

	@property
	def MinTradgPricgIncrmt(self):
		return self._MinTradgPricgIncrmt

	@MinTradgPricgIncrmt.setter
	def MinTradgPricgIncrmt(self, value):
		self._MinTradgPricgIncrmt = value if value is not None else base_types.UninitialisedField(self, 'MinTradgPricgIncrmt', Number, False)

	@MinTradgPricgIncrmt.deleter
	def MinTradgPricgIncrmt(self):
		del self._MinTradgPricgIncrmt
		self._MinTradgPricgIncrmt = base_types.UninitialisedField(self, 'MinTradgPricgIncrmt', Number, False)

	@property
	def NearTermPosLmt(self):
		return self._NearTermPosLmt

	@NearTermPosLmt.setter
	def NearTermPosLmt(self, value):
		self._NearTermPosLmt = value if value is not None else base_types.UninitialisedField(self, 'NearTermPosLmt', Number, False)

	@NearTermPosLmt.deleter
	def NearTermPosLmt(self):
		del self._NearTermPosLmt
		self._NearTermPosLmt = base_types.UninitialisedField(self, 'NearTermPosLmt', Number, False)

	@property
	def OptnRghts(self):
		return self._OptnRghts

	@OptnRghts.setter
	def OptnRghts(self, value):
		self._OptnRghts = value if value is not None else base_types.UninitialisedField(self, 'OptnRghts', OptionRight2Choice, False)

	@OptnRghts.deleter
	def OptnRghts(self):
		del self._OptnRghts
		self._OptnRghts = base_types.UninitialisedField(self, 'OptnRghts', OptionRight2Choice, False)

	@property
	def PosLmt(self):
		return self._PosLmt

	@PosLmt.setter
	def PosLmt(self, value):
		self._PosLmt = value if value is not None else base_types.UninitialisedField(self, 'PosLmt', Number, False)

	@PosLmt.deleter
	def PosLmt(self):
		del self._PosLmt
		self._PosLmt = base_types.UninitialisedField(self, 'PosLmt', Number, False)

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', Max256Text, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', Max256Text, False)

	@property
	def Ratg(self):
		return self._Ratg

	@Ratg.setter
	def Ratg(self, value):
		self._Ratg = value if value is not None else base_types.UninitialisedField(self, 'Ratg', Rating1, True)

	@Ratg.deleter
	def Ratg(self):
		del self._Ratg
		self._Ratg = base_types.UninitialisedField(self, 'Ratg', Rating1, True)

	@property
	def Ratio(self):
		return self._Ratio

	@Ratio.setter
	def Ratio(self, value):
		self._Ratio = value if value is not None else base_types.UninitialisedField(self, 'Ratio', UnderlyingRatio2, True)

	@Ratio.deleter
	def Ratio(self):
		del self._Ratio
		self._Ratio = base_types.UninitialisedField(self, 'Ratio', UnderlyingRatio2, True)

	@property
	def SprdTx(self):
		return self._SprdTx

	@SprdTx.setter
	def SprdTx(self, value):
		self._SprdTx = value if value is not None else base_types.UninitialisedField(self, 'SprdTx', YesNoIndicator, False)

	@SprdTx.deleter
	def SprdTx(self):
		del self._SprdTx
		self._SprdTx = base_types.UninitialisedField(self, 'SprdTx', YesNoIndicator, False)

	@property
	def StrpblInd(self):
		return self._StrpblInd

	@StrpblInd.setter
	def StrpblInd(self, value):
		self._StrpblInd = value if value is not None else base_types.UninitialisedField(self, 'StrpblInd', YesNoIndicator, False)

	@StrpblInd.deleter
	def StrpblInd(self):
		del self._StrpblInd
		self._StrpblInd = base_types.UninitialisedField(self, 'StrpblInd', YesNoIndicator, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure1Code, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure1Code, False)

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