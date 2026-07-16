# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import Amount22
from . import ISODate
from . import Max35Text
from . import Max70Text
from . import PhoneNumber
from . import Tax41
from . import TelecomServicesLineItem3

class TelecomServices3(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_BllgEnd", "_BllgEvt", "_BllgStart", "_CstmrAcctNb", "_CstmrNm", "_CstmrPhne", "_LineItm", "_TtlTax"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

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
		self._BllgEvt = value if value is not None else base_types.UninitialisedField(self, 'BllgEvt', Amount22, True)

	@BllgEvt.deleter
	def BllgEvt(self):
		del self._BllgEvt
		self._BllgEvt = base_types.UninitialisedField(self, 'BllgEvt', Amount22, True)

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
		self._CstmrNm = value if value is not None else base_types.UninitialisedField(self, 'CstmrNm', Max70Text, False)

	@CstmrNm.deleter
	def CstmrNm(self):
		del self._CstmrNm
		self._CstmrNm = base_types.UninitialisedField(self, 'CstmrNm', Max70Text, False)

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
		self._LineItm = value if value is not None else base_types.UninitialisedField(self, 'LineItm', TelecomServicesLineItem3, True)

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = base_types.UninitialisedField(self, 'LineItm', TelecomServicesLineItem3, True)

	@property
	def TtlTax(self):
		return self._TtlTax

	@TtlTax.setter
	def TtlTax(self, value):
		self._TtlTax = value if value is not None else base_types.UninitialisedField(self, 'TtlTax', Tax41, True)

	@TtlTax.deleter
	def TtlTax(self):
		del self._TtlTax
		self._TtlTax = base_types.UninitialisedField(self, 'TtlTax', Tax41, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BllgEnd', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BllgEvt', type=Amount22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BllgStart', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrAcctNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItm', type=TelecomServicesLineItem3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlTax', type=Tax41, min=0, max=None, mutex_group=None, array=True),
	))