from . import base_types
import ISODate
import Max256Text
import ISOTime
import Max35Text
import Tax41
import TelephonyCallType1Code
import ISOMax3ACountryCode
import ImpliedCurrencyAndAmount
import ISOCountrySubDivisionCode
import Amount23
import AdditionalData1
import PhoneNumber
import Max70Text

class TelecomServicesLineItem3(base_types._BaseFieldType):

	__slots__ = ["_CallFrCtrySubDvsnMjr", "_TmPrd", "_CallFrCity", "_CallToTp", "_CallFrPhne", "_CallToCtry", "_AddtlData", "_CallToCtrySubDvsnMnr", "_StartDtTm", "_Chrg", "_CallFrCtry", "_CallFrTp", "_Tax", "_CallToOthrTp", "_TtlAmt", "_CallToPhne", "_Drtn", "_CallToCtrySubDvsnMjr", "_Desc", "_CallFrCtrySubDvsnMnr", "_CallFrOthrTp", "_CallToCity"]
	@property
	def CallFrCtrySubDvsnMjr(self):
		return self._CallFrCtrySubDvsnMjr

	@CallFrCtrySubDvsnMjr.setter
	def CallFrCtrySubDvsnMjr(self, value):
		self._CallFrCtrySubDvsnMjr = value if type(value) != auto else self.make_default("CallFrCtrySubDvsnMjr")

	@CallFrCtrySubDvsnMjr.deleter
	def CallFrCtrySubDvsnMjr(self):
		del self._CallFrCtrySubDvsnMjr
		self._CallFrCtrySubDvsnMjr = None

	@property
	def TmPrd(self):
		return self._TmPrd

	@TmPrd.setter
	def TmPrd(self, value):
		self._TmPrd = value if type(value) != auto else self.make_default("TmPrd")

	@TmPrd.deleter
	def TmPrd(self):
		del self._TmPrd
		self._TmPrd = None

	@property
	def CallFrCity(self):
		return self._CallFrCity

	@CallFrCity.setter
	def CallFrCity(self, value):
		self._CallFrCity = value if type(value) != auto else self.make_default("CallFrCity")

	@CallFrCity.deleter
	def CallFrCity(self):
		del self._CallFrCity
		self._CallFrCity = None

	@property
	def CallToTp(self):
		return self._CallToTp

	@CallToTp.setter
	def CallToTp(self, value):
		self._CallToTp = value if type(value) != auto else self.make_default("CallToTp")

	@CallToTp.deleter
	def CallToTp(self):
		del self._CallToTp
		self._CallToTp = None

	@property
	def CallFrPhne(self):
		return self._CallFrPhne

	@CallFrPhne.setter
	def CallFrPhne(self, value):
		self._CallFrPhne = value if type(value) != auto else self.make_default("CallFrPhne")

	@CallFrPhne.deleter
	def CallFrPhne(self):
		del self._CallFrPhne
		self._CallFrPhne = None

	@property
	def CallToCtry(self):
		return self._CallToCtry

	@CallToCtry.setter
	def CallToCtry(self, value):
		self._CallToCtry = value if type(value) != auto else self.make_default("CallToCtry")

	@CallToCtry.deleter
	def CallToCtry(self):
		del self._CallToCtry
		self._CallToCtry = None

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def CallToCtrySubDvsnMnr(self):
		return self._CallToCtrySubDvsnMnr

	@CallToCtrySubDvsnMnr.setter
	def CallToCtrySubDvsnMnr(self, value):
		self._CallToCtrySubDvsnMnr = value if type(value) != auto else self.make_default("CallToCtrySubDvsnMnr")

	@CallToCtrySubDvsnMnr.deleter
	def CallToCtrySubDvsnMnr(self):
		del self._CallToCtrySubDvsnMnr
		self._CallToCtrySubDvsnMnr = None

	@property
	def StartDtTm(self):
		return self._StartDtTm

	@StartDtTm.setter
	def StartDtTm(self, value):
		self._StartDtTm = value if type(value) != auto else self.make_default("StartDtTm")

	@StartDtTm.deleter
	def StartDtTm(self):
		del self._StartDtTm
		self._StartDtTm = None

	@property
	def Chrg(self):
		return self._Chrg

	@Chrg.setter
	def Chrg(self, value):
		self._Chrg = value if type(value) != auto else self.make_default("Chrg")

	@Chrg.deleter
	def Chrg(self):
		del self._Chrg
		self._Chrg = None

	@property
	def CallFrCtry(self):
		return self._CallFrCtry

	@CallFrCtry.setter
	def CallFrCtry(self, value):
		self._CallFrCtry = value if type(value) != auto else self.make_default("CallFrCtry")

	@CallFrCtry.deleter
	def CallFrCtry(self):
		del self._CallFrCtry
		self._CallFrCtry = None

	@property
	def CallFrTp(self):
		return self._CallFrTp

	@CallFrTp.setter
	def CallFrTp(self, value):
		self._CallFrTp = value if type(value) != auto else self.make_default("CallFrTp")

	@CallFrTp.deleter
	def CallFrTp(self):
		del self._CallFrTp
		self._CallFrTp = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def CallToOthrTp(self):
		return self._CallToOthrTp

	@CallToOthrTp.setter
	def CallToOthrTp(self, value):
		self._CallToOthrTp = value if type(value) != auto else self.make_default("CallToOthrTp")

	@CallToOthrTp.deleter
	def CallToOthrTp(self):
		del self._CallToOthrTp
		self._CallToOthrTp = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def CallToPhne(self):
		return self._CallToPhne

	@CallToPhne.setter
	def CallToPhne(self, value):
		self._CallToPhne = value if type(value) != auto else self.make_default("CallToPhne")

	@CallToPhne.deleter
	def CallToPhne(self):
		del self._CallToPhne
		self._CallToPhne = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	@property
	def CallToCtrySubDvsnMjr(self):
		return self._CallToCtrySubDvsnMjr

	@CallToCtrySubDvsnMjr.setter
	def CallToCtrySubDvsnMjr(self, value):
		self._CallToCtrySubDvsnMjr = value if type(value) != auto else self.make_default("CallToCtrySubDvsnMjr")

	@CallToCtrySubDvsnMjr.deleter
	def CallToCtrySubDvsnMjr(self):
		del self._CallToCtrySubDvsnMjr
		self._CallToCtrySubDvsnMjr = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def CallFrCtrySubDvsnMnr(self):
		return self._CallFrCtrySubDvsnMnr

	@CallFrCtrySubDvsnMnr.setter
	def CallFrCtrySubDvsnMnr(self, value):
		self._CallFrCtrySubDvsnMnr = value if type(value) != auto else self.make_default("CallFrCtrySubDvsnMnr")

	@CallFrCtrySubDvsnMnr.deleter
	def CallFrCtrySubDvsnMnr(self):
		del self._CallFrCtrySubDvsnMnr
		self._CallFrCtrySubDvsnMnr = None

	@property
	def CallFrOthrTp(self):
		return self._CallFrOthrTp

	@CallFrOthrTp.setter
	def CallFrOthrTp(self, value):
		self._CallFrOthrTp = value if type(value) != auto else self.make_default("CallFrOthrTp")

	@CallFrOthrTp.deleter
	def CallFrOthrTp(self):
		del self._CallFrOthrTp
		self._CallFrOthrTp = None

	@property
	def CallToCity(self):
		return self._CallToCity

	@CallToCity.setter
	def CallToCity(self, value):
		self._CallToCity = value if type(value) != auto else self.make_default("CallToCity")

	@CallToCity.deleter
	def CallToCity(self):
		del self._CallToCity
		self._CallToCity = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CallFrCtrySubDvsnMjr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmPrd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallFrCity', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToTp', type=TelephonyCallType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallFrPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CallToCtrySubDvsnMnr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDtTm', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrg', type=Amount23, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CallFrCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallFrTp', type=TelephonyCallType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CallToOthrTp', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToCtrySubDvsnMjr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallFrCtrySubDvsnMnr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallFrOthrTp', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToCity', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

