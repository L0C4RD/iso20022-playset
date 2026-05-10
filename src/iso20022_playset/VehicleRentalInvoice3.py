from . import base_types
from .Amount21 import Amount21
from .Tax41 import Tax41
from .UnitOfMeasure10Code import UnitOfMeasure10Code
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .Max35Text import Max35Text
from .Max4NumericText import Max4NumericText
from .TrueFalseIndicator import TrueFalseIndicator
from .ISOTime import ISOTime
from .Address2 import Address2
from .ISODate import ISODate
from .RentalRate1 import RentalRate1
from .Max10NumericText import Max10NumericText
from .Max35NumericText import Max35NumericText

class VehicleRentalInvoice3(base_types._BaseFieldType):

	__slots__ = ["_ClssPrvdd", "_DstncRate", "_MdlPrvdd", "_RegnNbPrvdd", "_MakePrvdd", "_Chrg", "_AddtlAmt", "_MakeInvcd", "_Drtn", "_RegnNbInvcd", "_OdmtrRtr", "_RtrLctn", "_Tax", "_ChckOutDt", "_Insrnc", "_OdmtrStart", "_NoShow", "_Adjstd", "_ChckOutTm", "_DstncUnit", "_FreeDstnc", "_ChckInDt", "_MdlInvcd", "_SummryCmmdtyId", "_TtlDstnc", "_ChckInTm", "_ClssInvcd"]
	@property
	def ClssPrvdd(self):
		return self._ClssPrvdd

	@ClssPrvdd.setter
	def ClssPrvdd(self, value):
		self._ClssPrvdd = value if type(value) != base_types.auto else self.make_default("ClssPrvdd")

	@ClssPrvdd.deleter
	def ClssPrvdd(self):
		del self._ClssPrvdd
		self._ClssPrvdd = None

	@property
	def DstncRate(self):
		return self._DstncRate

	@DstncRate.setter
	def DstncRate(self, value):
		self._DstncRate = value if type(value) != base_types.auto else self.make_default("DstncRate")

	@DstncRate.deleter
	def DstncRate(self):
		del self._DstncRate
		self._DstncRate = None

	@property
	def MdlPrvdd(self):
		return self._MdlPrvdd

	@MdlPrvdd.setter
	def MdlPrvdd(self, value):
		self._MdlPrvdd = value if type(value) != base_types.auto else self.make_default("MdlPrvdd")

	@MdlPrvdd.deleter
	def MdlPrvdd(self):
		del self._MdlPrvdd
		self._MdlPrvdd = None

	@property
	def RegnNbPrvdd(self):
		return self._RegnNbPrvdd

	@RegnNbPrvdd.setter
	def RegnNbPrvdd(self, value):
		self._RegnNbPrvdd = value if type(value) != base_types.auto else self.make_default("RegnNbPrvdd")

	@RegnNbPrvdd.deleter
	def RegnNbPrvdd(self):
		del self._RegnNbPrvdd
		self._RegnNbPrvdd = None

	@property
	def MakePrvdd(self):
		return self._MakePrvdd

	@MakePrvdd.setter
	def MakePrvdd(self, value):
		self._MakePrvdd = value if type(value) != base_types.auto else self.make_default("MakePrvdd")

	@MakePrvdd.deleter
	def MakePrvdd(self):
		del self._MakePrvdd
		self._MakePrvdd = None

	@property
	def Chrg(self):
		return self._Chrg

	@Chrg.setter
	def Chrg(self, value):
		self._Chrg = value if type(value) != base_types.auto else self.make_default("Chrg")

	@Chrg.deleter
	def Chrg(self):
		del self._Chrg
		self._Chrg = None

	@property
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if type(value) != base_types.auto else self.make_default("AddtlAmt")

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = None

	@property
	def MakeInvcd(self):
		return self._MakeInvcd

	@MakeInvcd.setter
	def MakeInvcd(self, value):
		self._MakeInvcd = value if type(value) != base_types.auto else self.make_default("MakeInvcd")

	@MakeInvcd.deleter
	def MakeInvcd(self):
		del self._MakeInvcd
		self._MakeInvcd = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != base_types.auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	@property
	def RegnNbInvcd(self):
		return self._RegnNbInvcd

	@RegnNbInvcd.setter
	def RegnNbInvcd(self, value):
		self._RegnNbInvcd = value if type(value) != base_types.auto else self.make_default("RegnNbInvcd")

	@RegnNbInvcd.deleter
	def RegnNbInvcd(self):
		del self._RegnNbInvcd
		self._RegnNbInvcd = None

	@property
	def OdmtrRtr(self):
		return self._OdmtrRtr

	@OdmtrRtr.setter
	def OdmtrRtr(self, value):
		self._OdmtrRtr = value if type(value) != base_types.auto else self.make_default("OdmtrRtr")

	@OdmtrRtr.deleter
	def OdmtrRtr(self):
		del self._OdmtrRtr
		self._OdmtrRtr = None

	@property
	def RtrLctn(self):
		return self._RtrLctn

	@RtrLctn.setter
	def RtrLctn(self, value):
		self._RtrLctn = value if type(value) != base_types.auto else self.make_default("RtrLctn")

	@RtrLctn.deleter
	def RtrLctn(self):
		del self._RtrLctn
		self._RtrLctn = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def ChckOutDt(self):
		return self._ChckOutDt

	@ChckOutDt.setter
	def ChckOutDt(self, value):
		self._ChckOutDt = value if type(value) != base_types.auto else self.make_default("ChckOutDt")

	@ChckOutDt.deleter
	def ChckOutDt(self):
		del self._ChckOutDt
		self._ChckOutDt = None

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if type(value) != base_types.auto else self.make_default("Insrnc")

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = None

	@property
	def OdmtrStart(self):
		return self._OdmtrStart

	@OdmtrStart.setter
	def OdmtrStart(self, value):
		self._OdmtrStart = value if type(value) != base_types.auto else self.make_default("OdmtrStart")

	@OdmtrStart.deleter
	def OdmtrStart(self):
		del self._OdmtrStart
		self._OdmtrStart = None

	@property
	def NoShow(self):
		return self._NoShow

	@NoShow.setter
	def NoShow(self, value):
		self._NoShow = value if type(value) != base_types.auto else self.make_default("NoShow")

	@NoShow.deleter
	def NoShow(self):
		del self._NoShow
		self._NoShow = None

	@property
	def Adjstd(self):
		return self._Adjstd

	@Adjstd.setter
	def Adjstd(self, value):
		self._Adjstd = value if type(value) != base_types.auto else self.make_default("Adjstd")

	@Adjstd.deleter
	def Adjstd(self):
		del self._Adjstd
		self._Adjstd = None

	@property
	def ChckOutTm(self):
		return self._ChckOutTm

	@ChckOutTm.setter
	def ChckOutTm(self, value):
		self._ChckOutTm = value if type(value) != base_types.auto else self.make_default("ChckOutTm")

	@ChckOutTm.deleter
	def ChckOutTm(self):
		del self._ChckOutTm
		self._ChckOutTm = None

	@property
	def DstncUnit(self):
		return self._DstncUnit

	@DstncUnit.setter
	def DstncUnit(self, value):
		self._DstncUnit = value if type(value) != base_types.auto else self.make_default("DstncUnit")

	@DstncUnit.deleter
	def DstncUnit(self):
		del self._DstncUnit
		self._DstncUnit = None

	@property
	def FreeDstnc(self):
		return self._FreeDstnc

	@FreeDstnc.setter
	def FreeDstnc(self, value):
		self._FreeDstnc = value if type(value) != base_types.auto else self.make_default("FreeDstnc")

	@FreeDstnc.deleter
	def FreeDstnc(self):
		del self._FreeDstnc
		self._FreeDstnc = None

	@property
	def ChckInDt(self):
		return self._ChckInDt

	@ChckInDt.setter
	def ChckInDt(self, value):
		self._ChckInDt = value if type(value) != base_types.auto else self.make_default("ChckInDt")

	@ChckInDt.deleter
	def ChckInDt(self):
		del self._ChckInDt
		self._ChckInDt = None

	@property
	def MdlInvcd(self):
		return self._MdlInvcd

	@MdlInvcd.setter
	def MdlInvcd(self, value):
		self._MdlInvcd = value if type(value) != base_types.auto else self.make_default("MdlInvcd")

	@MdlInvcd.deleter
	def MdlInvcd(self):
		del self._MdlInvcd
		self._MdlInvcd = None

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if type(value) != base_types.auto else self.make_default("SummryCmmdtyId")

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = None

	@property
	def TtlDstnc(self):
		return self._TtlDstnc

	@TtlDstnc.setter
	def TtlDstnc(self, value):
		self._TtlDstnc = value if type(value) != base_types.auto else self.make_default("TtlDstnc")

	@TtlDstnc.deleter
	def TtlDstnc(self):
		del self._TtlDstnc
		self._TtlDstnc = None

	@property
	def ChckInTm(self):
		return self._ChckInTm

	@ChckInTm.setter
	def ChckInTm(self, value):
		self._ChckInTm = value if type(value) != base_types.auto else self.make_default("ChckInTm")

	@ChckInTm.deleter
	def ChckInTm(self):
		del self._ChckInTm
		self._ChckInTm = None

	@property
	def ClssInvcd(self):
		return self._ClssInvcd

	@ClssInvcd.setter
	def ClssInvcd(self, value):
		self._ClssInvcd = value if type(value) != base_types.auto else self.make_default("ClssInvcd")

	@ClssInvcd.deleter
	def ClssInvcd(self):
		del self._ClssInvcd
		self._ClssInvcd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssPrvdd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstncRate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdlPrvdd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnNbPrvdd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MakePrvdd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrg', type=RentalRate1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlAmt', type=Amount21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MakeInvcd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnNbInvcd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdmtrRtr', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrLctn', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChckOutDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdmtrStart', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adjstd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckOutTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstncUnit', type=UnitOfMeasure10Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FreeDstnc', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckInDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdlInvcd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlDstnc', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckInTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssInvcd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

