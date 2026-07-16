# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ReturnExcessCash1
from . import ThresholdType1Code

class SummaryAmounts2(base_types._BaseFieldType):

	__slots__ = ["_AdjstdXpsr", "_CollReqrd", "_MinTrfAmt", "_PreHrcutCollVal", "_PrvsCollVal", "_PrvsXpsrVal", "_RndgAmt", "_RtrXcssCshAndCollCcy", "_ThrshldAmt", "_ThrshldTp", "_TtlAcrdIntrstAmt", "_TtlFees", "_TtlPdgIncmgColl", "_TtlPdgOutgngColl"]
	@property
	def AdjstdXpsr(self):
		return self._AdjstdXpsr

	@AdjstdXpsr.setter
	def AdjstdXpsr(self, value):
		self._AdjstdXpsr = value if value is not None else base_types.UninitialisedField(self, 'AdjstdXpsr', ActiveCurrencyAndAmount, False)

	@AdjstdXpsr.deleter
	def AdjstdXpsr(self):
		del self._AdjstdXpsr
		self._AdjstdXpsr = base_types.UninitialisedField(self, 'AdjstdXpsr', ActiveCurrencyAndAmount, False)

	@property
	def CollReqrd(self):
		return self._CollReqrd

	@CollReqrd.setter
	def CollReqrd(self, value):
		self._CollReqrd = value if value is not None else base_types.UninitialisedField(self, 'CollReqrd', ActiveCurrencyAndAmount, False)

	@CollReqrd.deleter
	def CollReqrd(self):
		del self._CollReqrd
		self._CollReqrd = base_types.UninitialisedField(self, 'CollReqrd', ActiveCurrencyAndAmount, False)

	@property
	def MinTrfAmt(self):
		return self._MinTrfAmt

	@MinTrfAmt.setter
	def MinTrfAmt(self, value):
		self._MinTrfAmt = value if value is not None else base_types.UninitialisedField(self, 'MinTrfAmt', ActiveCurrencyAndAmount, False)

	@MinTrfAmt.deleter
	def MinTrfAmt(self):
		del self._MinTrfAmt
		self._MinTrfAmt = base_types.UninitialisedField(self, 'MinTrfAmt', ActiveCurrencyAndAmount, False)

	@property
	def PreHrcutCollVal(self):
		return self._PreHrcutCollVal

	@PreHrcutCollVal.setter
	def PreHrcutCollVal(self, value):
		self._PreHrcutCollVal = value if value is not None else base_types.UninitialisedField(self, 'PreHrcutCollVal', ActiveCurrencyAndAmount, False)

	@PreHrcutCollVal.deleter
	def PreHrcutCollVal(self):
		del self._PreHrcutCollVal
		self._PreHrcutCollVal = base_types.UninitialisedField(self, 'PreHrcutCollVal', ActiveCurrencyAndAmount, False)

	@property
	def PrvsCollVal(self):
		return self._PrvsCollVal

	@PrvsCollVal.setter
	def PrvsCollVal(self, value):
		self._PrvsCollVal = value if value is not None else base_types.UninitialisedField(self, 'PrvsCollVal', ActiveCurrencyAndAmount, False)

	@PrvsCollVal.deleter
	def PrvsCollVal(self):
		del self._PrvsCollVal
		self._PrvsCollVal = base_types.UninitialisedField(self, 'PrvsCollVal', ActiveCurrencyAndAmount, False)

	@property
	def PrvsXpsrVal(self):
		return self._PrvsXpsrVal

	@PrvsXpsrVal.setter
	def PrvsXpsrVal(self, value):
		self._PrvsXpsrVal = value if value is not None else base_types.UninitialisedField(self, 'PrvsXpsrVal', ActiveCurrencyAndAmount, False)

	@PrvsXpsrVal.deleter
	def PrvsXpsrVal(self):
		del self._PrvsXpsrVal
		self._PrvsXpsrVal = base_types.UninitialisedField(self, 'PrvsXpsrVal', ActiveCurrencyAndAmount, False)

	@property
	def RndgAmt(self):
		return self._RndgAmt

	@RndgAmt.setter
	def RndgAmt(self, value):
		self._RndgAmt = value if value is not None else base_types.UninitialisedField(self, 'RndgAmt', ActiveCurrencyAndAmount, False)

	@RndgAmt.deleter
	def RndgAmt(self):
		del self._RndgAmt
		self._RndgAmt = base_types.UninitialisedField(self, 'RndgAmt', ActiveCurrencyAndAmount, False)

	@property
	def RtrXcssCshAndCollCcy(self):
		return self._RtrXcssCshAndCollCcy

	@RtrXcssCshAndCollCcy.setter
	def RtrXcssCshAndCollCcy(self, value):
		self._RtrXcssCshAndCollCcy = value if value is not None else base_types.UninitialisedField(self, 'RtrXcssCshAndCollCcy', ReturnExcessCash1, True)

	@RtrXcssCshAndCollCcy.deleter
	def RtrXcssCshAndCollCcy(self):
		del self._RtrXcssCshAndCollCcy
		self._RtrXcssCshAndCollCcy = base_types.UninitialisedField(self, 'RtrXcssCshAndCollCcy', ReturnExcessCash1, True)

	@property
	def ThrshldAmt(self):
		return self._ThrshldAmt

	@ThrshldAmt.setter
	def ThrshldAmt(self, value):
		self._ThrshldAmt = value if value is not None else base_types.UninitialisedField(self, 'ThrshldAmt', ActiveCurrencyAndAmount, False)

	@ThrshldAmt.deleter
	def ThrshldAmt(self):
		del self._ThrshldAmt
		self._ThrshldAmt = base_types.UninitialisedField(self, 'ThrshldAmt', ActiveCurrencyAndAmount, False)

	@property
	def ThrshldTp(self):
		return self._ThrshldTp

	@ThrshldTp.setter
	def ThrshldTp(self, value):
		self._ThrshldTp = value if value is not None else base_types.UninitialisedField(self, 'ThrshldTp', ThresholdType1Code, False)

	@ThrshldTp.deleter
	def ThrshldTp(self):
		del self._ThrshldTp
		self._ThrshldTp = base_types.UninitialisedField(self, 'ThrshldTp', ThresholdType1Code, False)

	@property
	def TtlAcrdIntrstAmt(self):
		return self._TtlAcrdIntrstAmt

	@TtlAcrdIntrstAmt.setter
	def TtlAcrdIntrstAmt(self, value):
		self._TtlAcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAcrdIntrstAmt', ActiveCurrencyAndAmount, False)

	@TtlAcrdIntrstAmt.deleter
	def TtlAcrdIntrstAmt(self):
		del self._TtlAcrdIntrstAmt
		self._TtlAcrdIntrstAmt = base_types.UninitialisedField(self, 'TtlAcrdIntrstAmt', ActiveCurrencyAndAmount, False)

	@property
	def TtlFees(self):
		return self._TtlFees

	@TtlFees.setter
	def TtlFees(self, value):
		self._TtlFees = value if value is not None else base_types.UninitialisedField(self, 'TtlFees', ActiveCurrencyAndAmount, False)

	@TtlFees.deleter
	def TtlFees(self):
		del self._TtlFees
		self._TtlFees = base_types.UninitialisedField(self, 'TtlFees', ActiveCurrencyAndAmount, False)

	@property
	def TtlPdgIncmgColl(self):
		return self._TtlPdgIncmgColl

	@TtlPdgIncmgColl.setter
	def TtlPdgIncmgColl(self, value):
		self._TtlPdgIncmgColl = value if value is not None else base_types.UninitialisedField(self, 'TtlPdgIncmgColl', ActiveCurrencyAndAmount, False)

	@TtlPdgIncmgColl.deleter
	def TtlPdgIncmgColl(self):
		del self._TtlPdgIncmgColl
		self._TtlPdgIncmgColl = base_types.UninitialisedField(self, 'TtlPdgIncmgColl', ActiveCurrencyAndAmount, False)

	@property
	def TtlPdgOutgngColl(self):
		return self._TtlPdgOutgngColl

	@TtlPdgOutgngColl.setter
	def TtlPdgOutgngColl(self, value):
		self._TtlPdgOutgngColl = value if value is not None else base_types.UninitialisedField(self, 'TtlPdgOutgngColl', ActiveCurrencyAndAmount, False)

	@TtlPdgOutgngColl.deleter
	def TtlPdgOutgngColl(self):
		del self._TtlPdgOutgngColl
		self._TtlPdgOutgngColl = base_types.UninitialisedField(self, 'TtlPdgOutgngColl', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdjstdXpsr', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollReqrd', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinTrfAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreHrcutCollVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsCollVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsXpsrVal', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrXcssCshAndCollCcy', type=ReturnExcessCash1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ThrshldAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrshldTp', type=ThresholdType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlAcrdIntrstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlFees', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgIncmgColl', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPdgOutgngColl', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))