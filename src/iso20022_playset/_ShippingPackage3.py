from . import base_types
from ._ISODate import ISODate
from ._TrueFalseIndicator import TrueFalseIndicator
from ._DecimalNumber import DecimalNumber
from ._ISOTime import ISOTime
from ._PartyIdentification285 import PartyIdentification285
from ._ContactPersonal1 import ContactPersonal1
from ._Product8 import Product8
from ._Address2 import Address2
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._ContactBusiness1 import ContactBusiness1
from ._Max350Text import Max350Text
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._UnitOfMeasure1Code import UnitOfMeasure1Code

class ShippingPackage3(base_types._BaseFieldType):

	__slots__ = ["_SpplrNm", "_SpplrAdr", "_Pdct", "_DlvryNoteNb", "_DlvryCtct", "_PckpTm", "_SpplrCtct", "_DlvryAdr", "_DlvryInstrs", "_SpplrId", "_NbOfUnits", "_PckpDt", "_DlvryTm", "_WghtUnit", "_OthrWghtUnit", "_TrckgNb", "_InsrncAmt", "_SpplrInstrs", "_DlvryDt", "_Insrnc"]
	@property
	def DlvryAdr(self):
		return self._DlvryAdr

	@DlvryAdr.setter
	def DlvryAdr(self, value):
		self._DlvryAdr = value if type(value) != base_types.auto else self.make_default("DlvryAdr")

	@DlvryAdr.deleter
	def DlvryAdr(self):
		del self._DlvryAdr
		self._DlvryAdr = None

	@property
	def DlvryCtct(self):
		return self._DlvryCtct

	@DlvryCtct.setter
	def DlvryCtct(self, value):
		self._DlvryCtct = value if type(value) != base_types.auto else self.make_default("DlvryCtct")

	@DlvryCtct.deleter
	def DlvryCtct(self):
		del self._DlvryCtct
		self._DlvryCtct = None

	@property
	def DlvryDt(self):
		return self._DlvryDt

	@DlvryDt.setter
	def DlvryDt(self, value):
		self._DlvryDt = value if type(value) != base_types.auto else self.make_default("DlvryDt")

	@DlvryDt.deleter
	def DlvryDt(self):
		del self._DlvryDt
		self._DlvryDt = None

	@property
	def DlvryInstrs(self):
		return self._DlvryInstrs

	@DlvryInstrs.setter
	def DlvryInstrs(self, value):
		self._DlvryInstrs = value if type(value) != base_types.auto else self.make_default("DlvryInstrs")

	@DlvryInstrs.deleter
	def DlvryInstrs(self):
		del self._DlvryInstrs
		self._DlvryInstrs = None

	@property
	def DlvryNoteNb(self):
		return self._DlvryNoteNb

	@DlvryNoteNb.setter
	def DlvryNoteNb(self, value):
		self._DlvryNoteNb = value if type(value) != base_types.auto else self.make_default("DlvryNoteNb")

	@DlvryNoteNb.deleter
	def DlvryNoteNb(self):
		del self._DlvryNoteNb
		self._DlvryNoteNb = None

	@property
	def DlvryTm(self):
		return self._DlvryTm

	@DlvryTm.setter
	def DlvryTm(self, value):
		self._DlvryTm = value if type(value) != base_types.auto else self.make_default("DlvryTm")

	@DlvryTm.deleter
	def DlvryTm(self):
		del self._DlvryTm
		self._DlvryTm = None

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
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if type(value) != base_types.auto else self.make_default("InsrncAmt")

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = None

	@property
	def NbOfUnits(self):
		return self._NbOfUnits

	@NbOfUnits.setter
	def NbOfUnits(self, value):
		self._NbOfUnits = value if type(value) != base_types.auto else self.make_default("NbOfUnits")

	@NbOfUnits.deleter
	def NbOfUnits(self):
		del self._NbOfUnits
		self._NbOfUnits = None

	@property
	def OthrWghtUnit(self):
		return self._OthrWghtUnit

	@OthrWghtUnit.setter
	def OthrWghtUnit(self, value):
		self._OthrWghtUnit = value if type(value) != base_types.auto else self.make_default("OthrWghtUnit")

	@OthrWghtUnit.deleter
	def OthrWghtUnit(self):
		del self._OthrWghtUnit
		self._OthrWghtUnit = None

	@property
	def PckpDt(self):
		return self._PckpDt

	@PckpDt.setter
	def PckpDt(self, value):
		self._PckpDt = value if type(value) != base_types.auto else self.make_default("PckpDt")

	@PckpDt.deleter
	def PckpDt(self):
		del self._PckpDt
		self._PckpDt = None

	@property
	def PckpTm(self):
		return self._PckpTm

	@PckpTm.setter
	def PckpTm(self, value):
		self._PckpTm = value if type(value) != base_types.auto else self.make_default("PckpTm")

	@PckpTm.deleter
	def PckpTm(self):
		del self._PckpTm
		self._PckpTm = None

	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if type(value) != base_types.auto else self.make_default("Pdct")

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = None

	@property
	def SpplrAdr(self):
		return self._SpplrAdr

	@SpplrAdr.setter
	def SpplrAdr(self, value):
		self._SpplrAdr = value if type(value) != base_types.auto else self.make_default("SpplrAdr")

	@SpplrAdr.deleter
	def SpplrAdr(self):
		del self._SpplrAdr
		self._SpplrAdr = None

	@property
	def SpplrCtct(self):
		return self._SpplrCtct

	@SpplrCtct.setter
	def SpplrCtct(self, value):
		self._SpplrCtct = value if type(value) != base_types.auto else self.make_default("SpplrCtct")

	@SpplrCtct.deleter
	def SpplrCtct(self):
		del self._SpplrCtct
		self._SpplrCtct = None

	@property
	def SpplrId(self):
		return self._SpplrId

	@SpplrId.setter
	def SpplrId(self, value):
		self._SpplrId = value if type(value) != base_types.auto else self.make_default("SpplrId")

	@SpplrId.deleter
	def SpplrId(self):
		del self._SpplrId
		self._SpplrId = None

	@property
	def SpplrInstrs(self):
		return self._SpplrInstrs

	@SpplrInstrs.setter
	def SpplrInstrs(self, value):
		self._SpplrInstrs = value if type(value) != base_types.auto else self.make_default("SpplrInstrs")

	@SpplrInstrs.deleter
	def SpplrInstrs(self):
		del self._SpplrInstrs
		self._SpplrInstrs = None

	@property
	def SpplrNm(self):
		return self._SpplrNm

	@SpplrNm.setter
	def SpplrNm(self, value):
		self._SpplrNm = value if type(value) != base_types.auto else self.make_default("SpplrNm")

	@SpplrNm.deleter
	def SpplrNm(self):
		del self._SpplrNm
		self._SpplrNm = None

	@property
	def TrckgNb(self):
		return self._TrckgNb

	@TrckgNb.setter
	def TrckgNb(self, value):
		self._TrckgNb = value if type(value) != base_types.auto else self.make_default("TrckgNb")

	@TrckgNb.deleter
	def TrckgNb(self):
		del self._TrckgNb
		self._TrckgNb = None

	@property
	def WghtUnit(self):
		return self._WghtUnit

	@WghtUnit.setter
	def WghtUnit(self, value):
		self._WghtUnit = value if type(value) != base_types.auto else self.make_default("WghtUnit")

	@WghtUnit.deleter
	def WghtUnit(self):
		del self._WghtUnit
		self._WghtUnit = None

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

