# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMMediaStatus1Code
from . import ActiveCurrencyCode
from . import CheckCodeLine1Code
from . import GenericInformation1
from . import ImpliedCurrencyAndAmount
from . import Max70Text
from . import Number
from . import PercentageRate

class ATMDepositedMediaItem1(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_Ccy", "_CdLine", "_CdLineFrmt", "_CnfdncLvl", "_Cnt", "_MdiaId", "_MdiaSts", "_Ref", "_RjctdRsn", "_ScnndVal", "_UnitVal"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', GenericInformation1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', GenericInformation1, True)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CdLine(self):
		return self._CdLine

	@CdLine.setter
	def CdLine(self, value):
		self._CdLine = value if value is not None else base_types.UninitialisedField(self, 'CdLine', Max70Text, False)

	@CdLine.deleter
	def CdLine(self):
		del self._CdLine
		self._CdLine = base_types.UninitialisedField(self, 'CdLine', Max70Text, False)

	@property
	def CdLineFrmt(self):
		return self._CdLineFrmt

	@CdLineFrmt.setter
	def CdLineFrmt(self, value):
		self._CdLineFrmt = value if value is not None else base_types.UninitialisedField(self, 'CdLineFrmt', CheckCodeLine1Code, False)

	@CdLineFrmt.deleter
	def CdLineFrmt(self):
		del self._CdLineFrmt
		self._CdLineFrmt = base_types.UninitialisedField(self, 'CdLineFrmt', CheckCodeLine1Code, False)

	@property
	def CnfdncLvl(self):
		return self._CnfdncLvl

	@CnfdncLvl.setter
	def CnfdncLvl(self, value):
		self._CnfdncLvl = value if value is not None else base_types.UninitialisedField(self, 'CnfdncLvl', PercentageRate, False)

	@CnfdncLvl.deleter
	def CnfdncLvl(self):
		del self._CnfdncLvl
		self._CnfdncLvl = base_types.UninitialisedField(self, 'CnfdncLvl', PercentageRate, False)

	@property
	def Cnt(self):
		return self._Cnt

	@Cnt.setter
	def Cnt(self, value):
		self._Cnt = value if value is not None else base_types.UninitialisedField(self, 'Cnt', Number, False)

	@Cnt.deleter
	def Cnt(self):
		del self._Cnt
		self._Cnt = base_types.UninitialisedField(self, 'Cnt', Number, False)

	@property
	def MdiaId(self):
		return self._MdiaId

	@MdiaId.setter
	def MdiaId(self, value):
		self._MdiaId = value if value is not None else base_types.UninitialisedField(self, 'MdiaId', Max70Text, False)

	@MdiaId.deleter
	def MdiaId(self):
		del self._MdiaId
		self._MdiaId = base_types.UninitialisedField(self, 'MdiaId', Max70Text, False)

	@property
	def MdiaSts(self):
		return self._MdiaSts

	@MdiaSts.setter
	def MdiaSts(self, value):
		self._MdiaSts = value if value is not None else base_types.UninitialisedField(self, 'MdiaSts', ATMMediaStatus1Code, False)

	@MdiaSts.deleter
	def MdiaSts(self):
		del self._MdiaSts
		self._MdiaSts = base_types.UninitialisedField(self, 'MdiaSts', ATMMediaStatus1Code, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max70Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max70Text, False)

	@property
	def RjctdRsn(self):
		return self._RjctdRsn

	@RjctdRsn.setter
	def RjctdRsn(self, value):
		self._RjctdRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctdRsn', Max70Text, False)

	@RjctdRsn.deleter
	def RjctdRsn(self):
		del self._RjctdRsn
		self._RjctdRsn = base_types.UninitialisedField(self, 'RjctdRsn', Max70Text, False)

	@property
	def ScnndVal(self):
		return self._ScnndVal

	@ScnndVal.setter
	def ScnndVal(self, value):
		self._ScnndVal = value if value is not None else base_types.UninitialisedField(self, 'ScnndVal', ImpliedCurrencyAndAmount, False)

	@ScnndVal.deleter
	def ScnndVal(self):
		del self._ScnndVal
		self._ScnndVal = base_types.UninitialisedField(self, 'ScnndVal', ImpliedCurrencyAndAmount, False)

	@property
	def UnitVal(self):
		return self._UnitVal

	@UnitVal.setter
	def UnitVal(self, value):
		self._UnitVal = value if value is not None else base_types.UninitialisedField(self, 'UnitVal', ImpliedCurrencyAndAmount, False)

	@UnitVal.deleter
	def UnitVal(self):
		del self._UnitVal
		self._UnitVal = base_types.UninitialisedField(self, 'UnitVal', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=GenericInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdLine', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdLineFrmt', type=CheckCodeLine1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnfdncLvl', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cnt', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdiaSts', type=ATMMediaStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctdRsn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScnndVal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitVal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))