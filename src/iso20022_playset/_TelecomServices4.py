# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._ISODate import ISODate
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max105Text import Max105Text
from ._Max35Text import Max35Text
from ._PhoneNumber import PhoneNumber
from ._Tax44 import Tax44
from ._TelecomBillingEventAmount1 import TelecomBillingEventAmount1
from ._TelecomServicesLineItem4 import TelecomServicesLineItem4

class TelecomServices4(base_types._BaseFieldType):

	__slots__ = ["_BllgEnd", "_BllgEvt", "_BllgStart", "_CstmrAcctNb", "_CstmrNm", "_CstmrPhne", "_LineItm", "_NtlData", "_PrvtData", "_TtlAmt", "_TtlTax"]
	@property
	def BllgEnd(self):
		return self._BllgEnd

	@BllgEnd.setter
	def BllgEnd(self, value):
		self._BllgEnd = value if type(value) != base_types.auto else self.make_default("BllgEnd")

	@BllgEnd.deleter
	def BllgEnd(self):
		del self._BllgEnd
		self._BllgEnd = None

	@property
	def BllgEvt(self):
		return self._BllgEvt

	@BllgEvt.setter
	def BllgEvt(self, value):
		self._BllgEvt = value if type(value) != base_types.auto else self.make_default("BllgEvt")

	@BllgEvt.deleter
	def BllgEvt(self):
		del self._BllgEvt
		self._BllgEvt = None

	@property
	def BllgStart(self):
		return self._BllgStart

	@BllgStart.setter
	def BllgStart(self, value):
		self._BllgStart = value if type(value) != base_types.auto else self.make_default("BllgStart")

	@BllgStart.deleter
	def BllgStart(self):
		del self._BllgStart
		self._BllgStart = None

	@property
	def CstmrAcctNb(self):
		return self._CstmrAcctNb

	@CstmrAcctNb.setter
	def CstmrAcctNb(self, value):
		self._CstmrAcctNb = value if type(value) != base_types.auto else self.make_default("CstmrAcctNb")

	@CstmrAcctNb.deleter
	def CstmrAcctNb(self):
		del self._CstmrAcctNb
		self._CstmrAcctNb = None

	@property
	def CstmrNm(self):
		return self._CstmrNm

	@CstmrNm.setter
	def CstmrNm(self, value):
		self._CstmrNm = value if type(value) != base_types.auto else self.make_default("CstmrNm")

	@CstmrNm.deleter
	def CstmrNm(self):
		del self._CstmrNm
		self._CstmrNm = None

	@property
	def CstmrPhne(self):
		return self._CstmrPhne

	@CstmrPhne.setter
	def CstmrPhne(self, value):
		self._CstmrPhne = value if type(value) != base_types.auto else self.make_default("CstmrPhne")

	@CstmrPhne.deleter
	def CstmrPhne(self):
		del self._CstmrPhne
		self._CstmrPhne = None

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if type(value) != base_types.auto else self.make_default("LineItm")

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = None

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if type(value) != base_types.auto else self.make_default("TtlAmt")

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = None

	@property
	def TtlTax(self):
		return self._TtlTax

	@TtlTax.setter
	def TtlTax(self, value):
		self._TtlTax = value if type(value) != base_types.auto else self.make_default("TtlTax")

	@TtlTax.deleter
	def TtlTax(self):
		del self._TtlTax
		self._TtlTax = None

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