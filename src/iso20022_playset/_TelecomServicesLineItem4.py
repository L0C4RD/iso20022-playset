# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import ISOCountrySubDivisionCode
from . import ISODate
from . import ISOMax3ACountryCode
from . import ISOTime
from . import ImpliedCurrencyAndAmount
from . import Max256Text
from . import Max35Text
from . import PhoneNumber
from . import Tax44
from . import TelecomLineItemAmount1
from . import TelephonyCallType2Code

class TelecomServicesLineItem4(base_types._BaseFieldType):

	__slots__ = ["_CallFrCity", "_CallFrCtry", "_CallFrCtrySubDvsnMjr", "_CallFrCtrySubDvsnMnr", "_CallFrPhne", "_CallFrTp", "_CallToCity", "_CallToCtry", "_CallToCtrySubDvsnMjr", "_CallToCtrySubDvsnMnr", "_CallToPhne", "_CallToTp", "_Chrg", "_Desc", "_Drtn", "_NtlData", "_PrvtData", "_StartDtTm", "_Tax", "_TmPrd", "_TtlAmt"]
	@property
	def CallFrCity(self):
		return self._CallFrCity

	@CallFrCity.setter
	def CallFrCity(self, value):
		self._CallFrCity = value if value is not None else base_types.UninitialisedField(self, 'CallFrCity', Max35Text, False)

	@CallFrCity.deleter
	def CallFrCity(self):
		del self._CallFrCity
		self._CallFrCity = base_types.UninitialisedField(self, 'CallFrCity', Max35Text, False)

	@property
	def CallFrCtry(self):
		return self._CallFrCtry

	@CallFrCtry.setter
	def CallFrCtry(self, value):
		self._CallFrCtry = value if value is not None else base_types.UninitialisedField(self, 'CallFrCtry', ISOMax3ACountryCode, False)

	@CallFrCtry.deleter
	def CallFrCtry(self):
		del self._CallFrCtry
		self._CallFrCtry = base_types.UninitialisedField(self, 'CallFrCtry', ISOMax3ACountryCode, False)

	@property
	def CallFrCtrySubDvsnMjr(self):
		return self._CallFrCtrySubDvsnMjr

	@CallFrCtrySubDvsnMjr.setter
	def CallFrCtrySubDvsnMjr(self, value):
		self._CallFrCtrySubDvsnMjr = value if value is not None else base_types.UninitialisedField(self, 'CallFrCtrySubDvsnMjr', ISOCountrySubDivisionCode, False)

	@CallFrCtrySubDvsnMjr.deleter
	def CallFrCtrySubDvsnMjr(self):
		del self._CallFrCtrySubDvsnMjr
		self._CallFrCtrySubDvsnMjr = base_types.UninitialisedField(self, 'CallFrCtrySubDvsnMjr', ISOCountrySubDivisionCode, False)

	@property
	def CallFrCtrySubDvsnMnr(self):
		return self._CallFrCtrySubDvsnMnr

	@CallFrCtrySubDvsnMnr.setter
	def CallFrCtrySubDvsnMnr(self, value):
		self._CallFrCtrySubDvsnMnr = value if value is not None else base_types.UninitialisedField(self, 'CallFrCtrySubDvsnMnr', ISOCountrySubDivisionCode, False)

	@CallFrCtrySubDvsnMnr.deleter
	def CallFrCtrySubDvsnMnr(self):
		del self._CallFrCtrySubDvsnMnr
		self._CallFrCtrySubDvsnMnr = base_types.UninitialisedField(self, 'CallFrCtrySubDvsnMnr', ISOCountrySubDivisionCode, False)

	@property
	def CallFrPhne(self):
		return self._CallFrPhne

	@CallFrPhne.setter
	def CallFrPhne(self, value):
		self._CallFrPhne = value if value is not None else base_types.UninitialisedField(self, 'CallFrPhne', PhoneNumber, False)

	@CallFrPhne.deleter
	def CallFrPhne(self):
		del self._CallFrPhne
		self._CallFrPhne = base_types.UninitialisedField(self, 'CallFrPhne', PhoneNumber, False)

	@property
	def CallFrTp(self):
		return self._CallFrTp

	@CallFrTp.setter
	def CallFrTp(self, value):
		self._CallFrTp = value if value is not None else base_types.UninitialisedField(self, 'CallFrTp', TelephonyCallType2Code, False)

	@CallFrTp.deleter
	def CallFrTp(self):
		del self._CallFrTp
		self._CallFrTp = base_types.UninitialisedField(self, 'CallFrTp', TelephonyCallType2Code, False)

	@property
	def CallToCity(self):
		return self._CallToCity

	@CallToCity.setter
	def CallToCity(self, value):
		self._CallToCity = value if value is not None else base_types.UninitialisedField(self, 'CallToCity', Max35Text, False)

	@CallToCity.deleter
	def CallToCity(self):
		del self._CallToCity
		self._CallToCity = base_types.UninitialisedField(self, 'CallToCity', Max35Text, False)

	@property
	def CallToCtry(self):
		return self._CallToCtry

	@CallToCtry.setter
	def CallToCtry(self, value):
		self._CallToCtry = value if value is not None else base_types.UninitialisedField(self, 'CallToCtry', ISOMax3ACountryCode, False)

	@CallToCtry.deleter
	def CallToCtry(self):
		del self._CallToCtry
		self._CallToCtry = base_types.UninitialisedField(self, 'CallToCtry', ISOMax3ACountryCode, False)

	@property
	def CallToCtrySubDvsnMjr(self):
		return self._CallToCtrySubDvsnMjr

	@CallToCtrySubDvsnMjr.setter
	def CallToCtrySubDvsnMjr(self, value):
		self._CallToCtrySubDvsnMjr = value if value is not None else base_types.UninitialisedField(self, 'CallToCtrySubDvsnMjr', ISOCountrySubDivisionCode, False)

	@CallToCtrySubDvsnMjr.deleter
	def CallToCtrySubDvsnMjr(self):
		del self._CallToCtrySubDvsnMjr
		self._CallToCtrySubDvsnMjr = base_types.UninitialisedField(self, 'CallToCtrySubDvsnMjr', ISOCountrySubDivisionCode, False)

	@property
	def CallToCtrySubDvsnMnr(self):
		return self._CallToCtrySubDvsnMnr

	@CallToCtrySubDvsnMnr.setter
	def CallToCtrySubDvsnMnr(self, value):
		self._CallToCtrySubDvsnMnr = value if value is not None else base_types.UninitialisedField(self, 'CallToCtrySubDvsnMnr', ISOCountrySubDivisionCode, False)

	@CallToCtrySubDvsnMnr.deleter
	def CallToCtrySubDvsnMnr(self):
		del self._CallToCtrySubDvsnMnr
		self._CallToCtrySubDvsnMnr = base_types.UninitialisedField(self, 'CallToCtrySubDvsnMnr', ISOCountrySubDivisionCode, False)

	@property
	def CallToPhne(self):
		return self._CallToPhne

	@CallToPhne.setter
	def CallToPhne(self, value):
		self._CallToPhne = value if value is not None else base_types.UninitialisedField(self, 'CallToPhne', PhoneNumber, False)

	@CallToPhne.deleter
	def CallToPhne(self):
		del self._CallToPhne
		self._CallToPhne = base_types.UninitialisedField(self, 'CallToPhne', PhoneNumber, False)

	@property
	def CallToTp(self):
		return self._CallToTp

	@CallToTp.setter
	def CallToTp(self, value):
		self._CallToTp = value if value is not None else base_types.UninitialisedField(self, 'CallToTp', TelephonyCallType2Code, False)

	@CallToTp.deleter
	def CallToTp(self):
		del self._CallToTp
		self._CallToTp = base_types.UninitialisedField(self, 'CallToTp', TelephonyCallType2Code, False)

	@property
	def Chrg(self):
		return self._Chrg

	@Chrg.setter
	def Chrg(self, value):
		self._Chrg = value if value is not None else base_types.UninitialisedField(self, 'Chrg', TelecomLineItemAmount1, True)

	@Chrg.deleter
	def Chrg(self):
		del self._Chrg
		self._Chrg = base_types.UninitialisedField(self, 'Chrg', TelecomLineItemAmount1, True)

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max256Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max256Text, False)

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if value is not None else base_types.UninitialisedField(self, 'Drtn', ISOTime, False)

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = base_types.UninitialisedField(self, 'Drtn', ISOTime, False)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def StartDtTm(self):
		return self._StartDtTm

	@StartDtTm.setter
	def StartDtTm(self, value):
		self._StartDtTm = value if value is not None else base_types.UninitialisedField(self, 'StartDtTm', ISODate, False)

	@StartDtTm.deleter
	def StartDtTm(self):
		del self._StartDtTm
		self._StartDtTm = base_types.UninitialisedField(self, 'StartDtTm', ISODate, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax44, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax44, True)

	@property
	def TmPrd(self):
		return self._TmPrd

	@TmPrd.setter
	def TmPrd(self, value):
		self._TmPrd = value if value is not None else base_types.UninitialisedField(self, 'TmPrd', Max35Text, False)

	@TmPrd.deleter
	def TmPrd(self):
		del self._TmPrd
		self._TmPrd = base_types.UninitialisedField(self, 'TmPrd', Max35Text, False)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CallFrCity', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallFrCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallFrCtrySubDvsnMjr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallFrCtrySubDvsnMnr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallFrPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallFrTp', type=TelephonyCallType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToCity', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToCtrySubDvsnMjr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToCtrySubDvsnMnr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CallToTp', type=TelephonyCallType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Chrg', type=TelecomLineItemAmount1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Desc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StartDtTm', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax44, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TmPrd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))