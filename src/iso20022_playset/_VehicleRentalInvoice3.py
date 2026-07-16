# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address2
from . import Amount21
from . import ISODate
from . import ISOTime
from . import ImpliedCurrencyAndAmount
from . import Max10NumericText
from . import Max35NumericText
from . import Max35Text
from . import Max4NumericText
from . import RentalRate1
from . import Tax41
from . import TrueFalseIndicator
from . import UnitOfMeasure10Code

class VehicleRentalInvoice3(base_types._BaseFieldType):

	__slots__ = ["_AddtlAmt", "_Adjstd", "_ChckInDt", "_ChckInTm", "_ChckOutDt", "_ChckOutTm", "_Chrg", "_ClssInvcd", "_ClssPrvdd", "_Drtn", "_DstncRate", "_DstncUnit", "_FreeDstnc", "_Insrnc", "_MakeInvcd", "_MakePrvdd", "_MdlInvcd", "_MdlPrvdd", "_NoShow", "_OdmtrRtr", "_OdmtrStart", "_RegnNbInvcd", "_RegnNbPrvdd", "_RtrLctn", "_SummryCmmdtyId", "_Tax", "_TtlDstnc"]
	@property
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if value is not None else base_types.UninitialisedField(self, 'AddtlAmt', Amount21, True)

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = base_types.UninitialisedField(self, 'AddtlAmt', Amount21, True)

	@property
	def Adjstd(self):
		return self._Adjstd

	@Adjstd.setter
	def Adjstd(self, value):
		self._Adjstd = value if value is not None else base_types.UninitialisedField(self, 'Adjstd', TrueFalseIndicator, False)

	@Adjstd.deleter
	def Adjstd(self):
		del self._Adjstd
		self._Adjstd = base_types.UninitialisedField(self, 'Adjstd', TrueFalseIndicator, False)

	@property
	def ChckInDt(self):
		return self._ChckInDt

	@ChckInDt.setter
	def ChckInDt(self, value):
		self._ChckInDt = value if value is not None else base_types.UninitialisedField(self, 'ChckInDt', ISODate, False)

	@ChckInDt.deleter
	def ChckInDt(self):
		del self._ChckInDt
		self._ChckInDt = base_types.UninitialisedField(self, 'ChckInDt', ISODate, False)

	@property
	def ChckInTm(self):
		return self._ChckInTm

	@ChckInTm.setter
	def ChckInTm(self, value):
		self._ChckInTm = value if value is not None else base_types.UninitialisedField(self, 'ChckInTm', ISOTime, False)

	@ChckInTm.deleter
	def ChckInTm(self):
		del self._ChckInTm
		self._ChckInTm = base_types.UninitialisedField(self, 'ChckInTm', ISOTime, False)

	@property
	def ChckOutDt(self):
		return self._ChckOutDt

	@ChckOutDt.setter
	def ChckOutDt(self, value):
		self._ChckOutDt = value if value is not None else base_types.UninitialisedField(self, 'ChckOutDt', ISODate, False)

	@ChckOutDt.deleter
	def ChckOutDt(self):
		del self._ChckOutDt
		self._ChckOutDt = base_types.UninitialisedField(self, 'ChckOutDt', ISODate, False)

	@property
	def ChckOutTm(self):
		return self._ChckOutTm

	@ChckOutTm.setter
	def ChckOutTm(self, value):
		self._ChckOutTm = value if value is not None else base_types.UninitialisedField(self, 'ChckOutTm', ISOTime, False)

	@ChckOutTm.deleter
	def ChckOutTm(self):
		del self._ChckOutTm
		self._ChckOutTm = base_types.UninitialisedField(self, 'ChckOutTm', ISOTime, False)

	@property
	def Chrg(self):
		return self._Chrg

	@Chrg.setter
	def Chrg(self, value):
		self._Chrg = value if value is not None else base_types.UninitialisedField(self, 'Chrg', RentalRate1, True)

	@Chrg.deleter
	def Chrg(self):
		del self._Chrg
		self._Chrg = base_types.UninitialisedField(self, 'Chrg', RentalRate1, True)

	@property
	def ClssInvcd(self):
		return self._ClssInvcd

	@ClssInvcd.setter
	def ClssInvcd(self, value):
		self._ClssInvcd = value if value is not None else base_types.UninitialisedField(self, 'ClssInvcd', Max35Text, False)

	@ClssInvcd.deleter
	def ClssInvcd(self):
		del self._ClssInvcd
		self._ClssInvcd = base_types.UninitialisedField(self, 'ClssInvcd', Max35Text, False)

	@property
	def ClssPrvdd(self):
		return self._ClssPrvdd

	@ClssPrvdd.setter
	def ClssPrvdd(self, value):
		self._ClssPrvdd = value if value is not None else base_types.UninitialisedField(self, 'ClssPrvdd', Max35Text, False)

	@ClssPrvdd.deleter
	def ClssPrvdd(self):
		del self._ClssPrvdd
		self._ClssPrvdd = base_types.UninitialisedField(self, 'ClssPrvdd', Max35Text, False)

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if value is not None else base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = base_types.UninitialisedField(self, 'Drtn', Max4NumericText, False)

	@property
	def DstncRate(self):
		return self._DstncRate

	@DstncRate.setter
	def DstncRate(self, value):
		self._DstncRate = value if value is not None else base_types.UninitialisedField(self, 'DstncRate', ImpliedCurrencyAndAmount, False)

	@DstncRate.deleter
	def DstncRate(self):
		del self._DstncRate
		self._DstncRate = base_types.UninitialisedField(self, 'DstncRate', ImpliedCurrencyAndAmount, False)

	@property
	def DstncUnit(self):
		return self._DstncUnit

	@DstncUnit.setter
	def DstncUnit(self, value):
		self._DstncUnit = value if value is not None else base_types.UninitialisedField(self, 'DstncUnit', UnitOfMeasure10Code, False)

	@DstncUnit.deleter
	def DstncUnit(self):
		del self._DstncUnit
		self._DstncUnit = base_types.UninitialisedField(self, 'DstncUnit', UnitOfMeasure10Code, False)

	@property
	def FreeDstnc(self):
		return self._FreeDstnc

	@FreeDstnc.setter
	def FreeDstnc(self, value):
		self._FreeDstnc = value if value is not None else base_types.UninitialisedField(self, 'FreeDstnc', Max10NumericText, False)

	@FreeDstnc.deleter
	def FreeDstnc(self):
		del self._FreeDstnc
		self._FreeDstnc = base_types.UninitialisedField(self, 'FreeDstnc', Max10NumericText, False)

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if value is not None else base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@property
	def MakeInvcd(self):
		return self._MakeInvcd

	@MakeInvcd.setter
	def MakeInvcd(self, value):
		self._MakeInvcd = value if value is not None else base_types.UninitialisedField(self, 'MakeInvcd', Max35NumericText, False)

	@MakeInvcd.deleter
	def MakeInvcd(self):
		del self._MakeInvcd
		self._MakeInvcd = base_types.UninitialisedField(self, 'MakeInvcd', Max35NumericText, False)

	@property
	def MakePrvdd(self):
		return self._MakePrvdd

	@MakePrvdd.setter
	def MakePrvdd(self, value):
		self._MakePrvdd = value if value is not None else base_types.UninitialisedField(self, 'MakePrvdd', Max35NumericText, False)

	@MakePrvdd.deleter
	def MakePrvdd(self):
		del self._MakePrvdd
		self._MakePrvdd = base_types.UninitialisedField(self, 'MakePrvdd', Max35NumericText, False)

	@property
	def MdlInvcd(self):
		return self._MdlInvcd

	@MdlInvcd.setter
	def MdlInvcd(self, value):
		self._MdlInvcd = value if value is not None else base_types.UninitialisedField(self, 'MdlInvcd', Max35NumericText, False)

	@MdlInvcd.deleter
	def MdlInvcd(self):
		del self._MdlInvcd
		self._MdlInvcd = base_types.UninitialisedField(self, 'MdlInvcd', Max35NumericText, False)

	@property
	def MdlPrvdd(self):
		return self._MdlPrvdd

	@MdlPrvdd.setter
	def MdlPrvdd(self, value):
		self._MdlPrvdd = value if value is not None else base_types.UninitialisedField(self, 'MdlPrvdd', Max35NumericText, False)

	@MdlPrvdd.deleter
	def MdlPrvdd(self):
		del self._MdlPrvdd
		self._MdlPrvdd = base_types.UninitialisedField(self, 'MdlPrvdd', Max35NumericText, False)

	@property
	def NoShow(self):
		return self._NoShow

	@NoShow.setter
	def NoShow(self, value):
		self._NoShow = value if value is not None else base_types.UninitialisedField(self, 'NoShow', TrueFalseIndicator, False)

	@NoShow.deleter
	def NoShow(self):
		del self._NoShow
		self._NoShow = base_types.UninitialisedField(self, 'NoShow', TrueFalseIndicator, False)

	@property
	def OdmtrRtr(self):
		return self._OdmtrRtr

	@OdmtrRtr.setter
	def OdmtrRtr(self, value):
		self._OdmtrRtr = value if value is not None else base_types.UninitialisedField(self, 'OdmtrRtr', Max10NumericText, False)

	@OdmtrRtr.deleter
	def OdmtrRtr(self):
		del self._OdmtrRtr
		self._OdmtrRtr = base_types.UninitialisedField(self, 'OdmtrRtr', Max10NumericText, False)

	@property
	def OdmtrStart(self):
		return self._OdmtrStart

	@OdmtrStart.setter
	def OdmtrStart(self, value):
		self._OdmtrStart = value if value is not None else base_types.UninitialisedField(self, 'OdmtrStart', Max10NumericText, False)

	@OdmtrStart.deleter
	def OdmtrStart(self):
		del self._OdmtrStart
		self._OdmtrStart = base_types.UninitialisedField(self, 'OdmtrStart', Max10NumericText, False)

	@property
	def RegnNbInvcd(self):
		return self._RegnNbInvcd

	@RegnNbInvcd.setter
	def RegnNbInvcd(self, value):
		self._RegnNbInvcd = value if value is not None else base_types.UninitialisedField(self, 'RegnNbInvcd', Max35Text, False)

	@RegnNbInvcd.deleter
	def RegnNbInvcd(self):
		del self._RegnNbInvcd
		self._RegnNbInvcd = base_types.UninitialisedField(self, 'RegnNbInvcd', Max35Text, False)

	@property
	def RegnNbPrvdd(self):
		return self._RegnNbPrvdd

	@RegnNbPrvdd.setter
	def RegnNbPrvdd(self, value):
		self._RegnNbPrvdd = value if value is not None else base_types.UninitialisedField(self, 'RegnNbPrvdd', Max35Text, False)

	@RegnNbPrvdd.deleter
	def RegnNbPrvdd(self):
		del self._RegnNbPrvdd
		self._RegnNbPrvdd = base_types.UninitialisedField(self, 'RegnNbPrvdd', Max35Text, False)

	@property
	def RtrLctn(self):
		return self._RtrLctn

	@RtrLctn.setter
	def RtrLctn(self, value):
		self._RtrLctn = value if value is not None else base_types.UninitialisedField(self, 'RtrLctn', Address2, False)

	@RtrLctn.deleter
	def RtrLctn(self):
		del self._RtrLctn
		self._RtrLctn = base_types.UninitialisedField(self, 'RtrLctn', Address2, False)

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if value is not None else base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax41, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax41, True)

	@property
	def TtlDstnc(self):
		return self._TtlDstnc

	@TtlDstnc.setter
	def TtlDstnc(self, value):
		self._TtlDstnc = value if value is not None else base_types.UninitialisedField(self, 'TtlDstnc', Max10NumericText, False)

	@TtlDstnc.deleter
	def TtlDstnc(self):
		del self._TtlDstnc
		self._TtlDstnc = base_types.UninitialisedField(self, 'TtlDstnc', Max10NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAmt', type=Amount21, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Adjstd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckInDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckInTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckOutDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChckOutTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrg', type=RentalRate1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClssInvcd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssPrvdd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstncRate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstncUnit', type=UnitOfMeasure10Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FreeDstnc', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MakeInvcd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MakePrvdd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdlInvcd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MdlPrvdd', type=Max35NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoShow', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdmtrRtr', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdmtrStart', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnNbInvcd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnNbPrvdd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrLctn', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlDstnc', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
	))