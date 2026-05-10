from . import base_types
from .Tax41 import Tax41
from .TelecomServicesLineItem3 import TelecomServicesLineItem3
from .Max35Text import Max35Text
from .Max70Text import Max70Text
from .ISODate import ISODate
from .Amount22 import Amount22
from .AdditionalData1 import AdditionalData1
from .PhoneNumber import PhoneNumber

class TelecomServices3(base_types._BaseFieldType):

	__slots__ = ["_TtlTax", "_CstmrAcctNb", "_BllgEvt", "_AddtlData", "_LineItm", "_CstmrNm", "_BllgStart", "_CstmrPhne", "_BllgEnd"]
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
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

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
	def BllgEnd(self):
		return self._BllgEnd

	@BllgEnd.setter
	def BllgEnd(self, value):
		self._BllgEnd = value if type(value) != base_types.auto else self.make_default("BllgEnd")

	@BllgEnd.deleter
	def BllgEnd(self):
		del self._BllgEnd
		self._BllgEnd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlTax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrAcctNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgEvt', type=Amount22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LineItm', type=TelecomServicesLineItem3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgStart', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgEnd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

