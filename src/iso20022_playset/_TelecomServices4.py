# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max105Text
from . import Max35Text
from . import PhoneNumber
from . import Tax44
from . import TelecomBillingEventAmount1
from . import TelecomServicesLineItem4

class TelecomServices4(base_types._BaseFieldType):

	__slots__ = ["_BllgEnd", "_BllgEvt", "_BllgStart", "_CstmrAcctNb", "_CstmrNm", "_CstmrPhne", "_LineItm", "_NtlData", "_PrvtData", "_TtlAmt", "_TtlTax"]
	@property
	def BllgEnd(self):
		return self._BllgEnd

	@BllgEnd.setter
	def BllgEnd(self, value):
		self._BllgEnd = value if value is not None else base_types.UninitialisedField(self, 'BllgEnd', ISODate, False)

	@BllgEnd.deleter
	def BllgEnd(self):
		del self._BllgEnd
		self._BllgEnd = base_types.UninitialisedField(self, 'BllgEnd', ISODate, False)

	@property
	def BllgEvt(self):
		return self._BllgEvt

	@BllgEvt.setter
	def BllgEvt(self, value):
		self._BllgEvt = value if value is not None else base_types.UninitialisedField(self, 'BllgEvt', TelecomBillingEventAmount1, True)

	@BllgEvt.deleter
	def BllgEvt(self):
		del self._BllgEvt
		self._BllgEvt = base_types.UninitialisedField(self, 'BllgEvt', TelecomBillingEventAmount1, True)

	@property
	def BllgStart(self):
		return self._BllgStart

	@BllgStart.setter
	def BllgStart(self, value):
		self._BllgStart = value if value is not None else base_types.UninitialisedField(self, 'BllgStart', ISODate, False)

	@BllgStart.deleter
	def BllgStart(self):
		del self._BllgStart
		self._BllgStart = base_types.UninitialisedField(self, 'BllgStart', ISODate, False)

	@property
	def CstmrAcctNb(self):
		return self._CstmrAcctNb

	@CstmrAcctNb.setter
	def CstmrAcctNb(self, value):
		self._CstmrAcctNb = value if value is not None else base_types.UninitialisedField(self, 'CstmrAcctNb', Max35Text, False)

	@CstmrAcctNb.deleter
	def CstmrAcctNb(self):
		del self._CstmrAcctNb
		self._CstmrAcctNb = base_types.UninitialisedField(self, 'CstmrAcctNb', Max35Text, False)

	@property
	def CstmrNm(self):
		return self._CstmrNm

	@CstmrNm.setter
	def CstmrNm(self, value):
		self._CstmrNm = value if value is not None else base_types.UninitialisedField(self, 'CstmrNm', Max105Text, False)

	@CstmrNm.deleter
	def CstmrNm(self):
		del self._CstmrNm
		self._CstmrNm = base_types.UninitialisedField(self, 'CstmrNm', Max105Text, False)

	@property
	def CstmrPhne(self):
		return self._CstmrPhne

	@CstmrPhne.setter
	def CstmrPhne(self, value):
		self._CstmrPhne = value if value is not None else base_types.UninitialisedField(self, 'CstmrPhne', PhoneNumber, False)

	@CstmrPhne.deleter
	def CstmrPhne(self):
		del self._CstmrPhne
		self._CstmrPhne = base_types.UninitialisedField(self, 'CstmrPhne', PhoneNumber, False)

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if value is not None else base_types.UninitialisedField(self, 'LineItm', TelecomServicesLineItem4, True)

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = base_types.UninitialisedField(self, 'LineItm', TelecomServicesLineItem4, True)

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
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', ImpliedCurrencyAndAmount, False)

	@property
	def TtlTax(self):
		return self._TtlTax

	@TtlTax.setter
	def TtlTax(self, value):
		self._TtlTax = value if value is not None else base_types.UninitialisedField(self, 'TtlTax', Tax44, True)

	@TtlTax.deleter
	def TtlTax(self):
		del self._TtlTax
		self._TtlTax = base_types.UninitialisedField(self, 'TtlTax', Tax44, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllgEnd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgEvt', type=TelecomBillingEventAmount1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BllgStart', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrAcctNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrNm', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItm', type=TelecomServicesLineItem4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlTax', type=Tax44, min=0, max=None, mutex_group=None, array=True),
	))