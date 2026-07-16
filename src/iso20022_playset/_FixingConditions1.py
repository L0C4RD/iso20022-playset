# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import BaseOneRate
from . import ISODate
from . import Max35Text

class FixingConditions1(base_types._BaseFieldType):

	__slots__ = ["_CmonRef", "_OrgtrRef", "_RltdRef", "_TradDt", "_TradgSdBuyAmt", "_TradgSdSellAmt", "_XchgRate"]
	@property
	def CmonRef(self):
		return self._CmonRef

	@CmonRef.setter
	def CmonRef(self, value):
		self._CmonRef = value if value is not None else base_types.UninitialisedField(self, 'CmonRef', Max35Text, False)

	@CmonRef.deleter
	def CmonRef(self):
		del self._CmonRef
		self._CmonRef = base_types.UninitialisedField(self, 'CmonRef', Max35Text, False)

	@property
	def OrgtrRef(self):
		return self._OrgtrRef

	@OrgtrRef.setter
	def OrgtrRef(self, value):
		self._OrgtrRef = value if value is not None else base_types.UninitialisedField(self, 'OrgtrRef', Max35Text, False)

	@OrgtrRef.deleter
	def OrgtrRef(self):
		del self._OrgtrRef
		self._OrgtrRef = base_types.UninitialisedField(self, 'OrgtrRef', Max35Text, False)

	@property
	def RltdRef(self):
		return self._RltdRef

	@RltdRef.setter
	def RltdRef(self, value):
		self._RltdRef = value if value is not None else base_types.UninitialisedField(self, 'RltdRef', Max35Text, False)

	@RltdRef.deleter
	def RltdRef(self):
		del self._RltdRef
		self._RltdRef = base_types.UninitialisedField(self, 'RltdRef', Max35Text, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@property
	def TradgSdBuyAmt(self):
		return self._TradgSdBuyAmt

	@TradgSdBuyAmt.setter
	def TradgSdBuyAmt(self, value):
		self._TradgSdBuyAmt = value if value is not None else base_types.UninitialisedField(self, 'TradgSdBuyAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TradgSdBuyAmt.deleter
	def TradgSdBuyAmt(self):
		del self._TradgSdBuyAmt
		self._TradgSdBuyAmt = base_types.UninitialisedField(self, 'TradgSdBuyAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def TradgSdSellAmt(self):
		return self._TradgSdSellAmt

	@TradgSdSellAmt.setter
	def TradgSdSellAmt(self, value):
		self._TradgSdSellAmt = value if value is not None else base_types.UninitialisedField(self, 'TradgSdSellAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@TradgSdSellAmt.deleter
	def TradgSdSellAmt(self):
		del self._TradgSdSellAmt
		self._TradgSdSellAmt = base_types.UninitialisedField(self, 'TradgSdSellAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmonRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdBuyAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdSellAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
	))