# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address2
from . import ContactBusiness1
from . import ContactPersonal1
from . import DecimalNumber
from . import ISODate
from . import ISOTime
from . import ImpliedCurrencyAndAmount
from . import Max350Text
from . import Max35Text
from . import Max70Text
from . import PartyIdentification285
from . import Product8
from . import TrueFalseIndicator
from . import UnitOfMeasure1Code

class ShippingPackage3(base_types._BaseFieldType):

	__slots__ = ["_DlvryAdr", "_DlvryCtct", "_DlvryDt", "_DlvryInstrs", "_DlvryNoteNb", "_DlvryTm", "_Insrnc", "_InsrncAmt", "_NbOfUnits", "_OthrWghtUnit", "_PckpDt", "_PckpTm", "_Pdct", "_SpplrAdr", "_SpplrCtct", "_SpplrId", "_SpplrInstrs", "_SpplrNm", "_TrckgNb", "_WghtUnit"]
	@property
	def DlvryAdr(self):
		return self._DlvryAdr

	@DlvryAdr.setter
	def DlvryAdr(self, value):
		self._DlvryAdr = value if value is not None else base_types.UninitialisedField(self, 'DlvryAdr', Address2, False)

	@DlvryAdr.deleter
	def DlvryAdr(self):
		del self._DlvryAdr
		self._DlvryAdr = base_types.UninitialisedField(self, 'DlvryAdr', Address2, False)

	@property
	def DlvryCtct(self):
		return self._DlvryCtct

	@DlvryCtct.setter
	def DlvryCtct(self, value):
		self._DlvryCtct = value if value is not None else base_types.UninitialisedField(self, 'DlvryCtct', ContactPersonal1, False)

	@DlvryCtct.deleter
	def DlvryCtct(self):
		del self._DlvryCtct
		self._DlvryCtct = base_types.UninitialisedField(self, 'DlvryCtct', ContactPersonal1, False)

	@property
	def DlvryDt(self):
		return self._DlvryDt

	@DlvryDt.setter
	def DlvryDt(self, value):
		self._DlvryDt = value if value is not None else base_types.UninitialisedField(self, 'DlvryDt', ISODate, False)

	@DlvryDt.deleter
	def DlvryDt(self):
		del self._DlvryDt
		self._DlvryDt = base_types.UninitialisedField(self, 'DlvryDt', ISODate, False)

	@property
	def DlvryInstrs(self):
		return self._DlvryInstrs

	@DlvryInstrs.setter
	def DlvryInstrs(self, value):
		self._DlvryInstrs = value if value is not None else base_types.UninitialisedField(self, 'DlvryInstrs', Max350Text, False)

	@DlvryInstrs.deleter
	def DlvryInstrs(self):
		del self._DlvryInstrs
		self._DlvryInstrs = base_types.UninitialisedField(self, 'DlvryInstrs', Max350Text, False)

	@property
	def DlvryNoteNb(self):
		return self._DlvryNoteNb

	@DlvryNoteNb.setter
	def DlvryNoteNb(self, value):
		self._DlvryNoteNb = value if value is not None else base_types.UninitialisedField(self, 'DlvryNoteNb', Max35Text, False)

	@DlvryNoteNb.deleter
	def DlvryNoteNb(self):
		del self._DlvryNoteNb
		self._DlvryNoteNb = base_types.UninitialisedField(self, 'DlvryNoteNb', Max35Text, False)

	@property
	def DlvryTm(self):
		return self._DlvryTm

	@DlvryTm.setter
	def DlvryTm(self, value):
		self._DlvryTm = value if value is not None else base_types.UninitialisedField(self, 'DlvryTm', ISOTime, False)

	@DlvryTm.deleter
	def DlvryTm(self):
		del self._DlvryTm
		self._DlvryTm = base_types.UninitialisedField(self, 'DlvryTm', ISOTime, False)

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
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if value is not None else base_types.UninitialisedField(self, 'InsrncAmt', ImpliedCurrencyAndAmount, False)

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = base_types.UninitialisedField(self, 'InsrncAmt', ImpliedCurrencyAndAmount, False)

	@property
	def NbOfUnits(self):
		return self._NbOfUnits

	@NbOfUnits.setter
	def NbOfUnits(self, value):
		self._NbOfUnits = value if value is not None else base_types.UninitialisedField(self, 'NbOfUnits', DecimalNumber, False)

	@NbOfUnits.deleter
	def NbOfUnits(self):
		del self._NbOfUnits
		self._NbOfUnits = base_types.UninitialisedField(self, 'NbOfUnits', DecimalNumber, False)

	@property
	def OthrWghtUnit(self):
		return self._OthrWghtUnit

	@OthrWghtUnit.setter
	def OthrWghtUnit(self, value):
		self._OthrWghtUnit = value if value is not None else base_types.UninitialisedField(self, 'OthrWghtUnit', Max35Text, False)

	@OthrWghtUnit.deleter
	def OthrWghtUnit(self):
		del self._OthrWghtUnit
		self._OthrWghtUnit = base_types.UninitialisedField(self, 'OthrWghtUnit', Max35Text, False)

	@property
	def PckpDt(self):
		return self._PckpDt

	@PckpDt.setter
	def PckpDt(self, value):
		self._PckpDt = value if value is not None else base_types.UninitialisedField(self, 'PckpDt', ISODate, False)

	@PckpDt.deleter
	def PckpDt(self):
		del self._PckpDt
		self._PckpDt = base_types.UninitialisedField(self, 'PckpDt', ISODate, False)

	@property
	def PckpTm(self):
		return self._PckpTm

	@PckpTm.setter
	def PckpTm(self, value):
		self._PckpTm = value if value is not None else base_types.UninitialisedField(self, 'PckpTm', ISOTime, False)

	@PckpTm.deleter
	def PckpTm(self):
		del self._PckpTm
		self._PckpTm = base_types.UninitialisedField(self, 'PckpTm', ISOTime, False)

	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if value is not None else base_types.UninitialisedField(self, 'Pdct', Product8, True)

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = base_types.UninitialisedField(self, 'Pdct', Product8, True)

	@property
	def SpplrAdr(self):
		return self._SpplrAdr

	@SpplrAdr.setter
	def SpplrAdr(self, value):
		self._SpplrAdr = value if value is not None else base_types.UninitialisedField(self, 'SpplrAdr', Address2, False)

	@SpplrAdr.deleter
	def SpplrAdr(self):
		del self._SpplrAdr
		self._SpplrAdr = base_types.UninitialisedField(self, 'SpplrAdr', Address2, False)

	@property
	def SpplrCtct(self):
		return self._SpplrCtct

	@SpplrCtct.setter
	def SpplrCtct(self, value):
		self._SpplrCtct = value if value is not None else base_types.UninitialisedField(self, 'SpplrCtct', ContactBusiness1, False)

	@SpplrCtct.deleter
	def SpplrCtct(self):
		del self._SpplrCtct
		self._SpplrCtct = base_types.UninitialisedField(self, 'SpplrCtct', ContactBusiness1, False)

	@property
	def SpplrId(self):
		return self._SpplrId

	@SpplrId.setter
	def SpplrId(self, value):
		self._SpplrId = value if value is not None else base_types.UninitialisedField(self, 'SpplrId', PartyIdentification285, False)

	@SpplrId.deleter
	def SpplrId(self):
		del self._SpplrId
		self._SpplrId = base_types.UninitialisedField(self, 'SpplrId', PartyIdentification285, False)

	@property
	def SpplrInstrs(self):
		return self._SpplrInstrs

	@SpplrInstrs.setter
	def SpplrInstrs(self, value):
		self._SpplrInstrs = value if value is not None else base_types.UninitialisedField(self, 'SpplrInstrs', Max350Text, False)

	@SpplrInstrs.deleter
	def SpplrInstrs(self):
		del self._SpplrInstrs
		self._SpplrInstrs = base_types.UninitialisedField(self, 'SpplrInstrs', Max350Text, False)

	@property
	def SpplrNm(self):
		return self._SpplrNm

	@SpplrNm.setter
	def SpplrNm(self, value):
		self._SpplrNm = value if value is not None else base_types.UninitialisedField(self, 'SpplrNm', Max70Text, False)

	@SpplrNm.deleter
	def SpplrNm(self):
		del self._SpplrNm
		self._SpplrNm = base_types.UninitialisedField(self, 'SpplrNm', Max70Text, False)

	@property
	def TrckgNb(self):
		return self._TrckgNb

	@TrckgNb.setter
	def TrckgNb(self, value):
		self._TrckgNb = value if value is not None else base_types.UninitialisedField(self, 'TrckgNb', Max70Text, False)

	@TrckgNb.deleter
	def TrckgNb(self):
		del self._TrckgNb
		self._TrckgNb = base_types.UninitialisedField(self, 'TrckgNb', Max70Text, False)

	@property
	def WghtUnit(self):
		return self._WghtUnit

	@WghtUnit.setter
	def WghtUnit(self, value):
		self._WghtUnit = value if value is not None else base_types.UninitialisedField(self, 'WghtUnit', UnitOfMeasure1Code, False)

	@WghtUnit.deleter
	def WghtUnit(self):
		del self._WghtUnit
		self._WghtUnit = base_types.UninitialisedField(self, 'WghtUnit', UnitOfMeasure1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvryAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryCtct', type=ContactPersonal1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryInstrs', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryNoteNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfUnits', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrWghtUnit', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PckpDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PckpTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdct', type=Product8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpplrAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpplrCtct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpplrId', type=PartyIdentification285, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpplrInstrs', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpplrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckgNb', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WghtUnit', type=UnitOfMeasure1Code, min=0, max=1, mutex_group=None, array=False),
	))