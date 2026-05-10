import base_types
import Side1Code
import ISODateTime
import DecimalNumber
import ActiveCurrencyCode
import AgreedRate3
import SecurityIdentification18
import ActiveCurrencyAndAmount
import SettlementDate8Code
import Max35Text
import ISODate
import ActiveCurrencyAnd13DecimalAmount

class InstrumentLeg7(base_types._BaseFieldType):

	__slots__ = ["_LegRskAmt", "_LegSd", "_LegClctdCtrPtyCcyLastQty", "_LegSctyId", "_LegValtnRate", "_LegSttlmDt", "_LegSttlmTp", "_LegOrdrQty", "_LegSttlmCcy", "_LegCcy", "_LegFwdPts", "_LegValDt", "_LegLastPric", "_LegSymb"]
	@property
	def LegRskAmt(self):
		return self._LegRskAmt

	@LegRskAmt.setter
	def LegRskAmt(self, value):
		self._LegRskAmt = value if type(value) != auto else self.make_default("LegRskAmt")

	@LegRskAmt.deleter
	def LegRskAmt(self):
		del self._LegRskAmt
		self._LegRskAmt = None

	@property
	def LegSd(self):
		return self._LegSd

	@LegSd.setter
	def LegSd(self, value):
		self._LegSd = value if type(value) != auto else self.make_default("LegSd")

	@LegSd.deleter
	def LegSd(self):
		del self._LegSd
		self._LegSd = None

	@property
	def LegClctdCtrPtyCcyLastQty(self):
		return self._LegClctdCtrPtyCcyLastQty

	@LegClctdCtrPtyCcyLastQty.setter
	def LegClctdCtrPtyCcyLastQty(self, value):
		self._LegClctdCtrPtyCcyLastQty = value if type(value) != auto else self.make_default("LegClctdCtrPtyCcyLastQty")

	@LegClctdCtrPtyCcyLastQty.deleter
	def LegClctdCtrPtyCcyLastQty(self):
		del self._LegClctdCtrPtyCcyLastQty
		self._LegClctdCtrPtyCcyLastQty = None

	@property
	def LegSctyId(self):
		return self._LegSctyId

	@LegSctyId.setter
	def LegSctyId(self, value):
		self._LegSctyId = value if type(value) != auto else self.make_default("LegSctyId")

	@LegSctyId.deleter
	def LegSctyId(self):
		del self._LegSctyId
		self._LegSctyId = None

	@property
	def LegValtnRate(self):
		return self._LegValtnRate

	@LegValtnRate.setter
	def LegValtnRate(self, value):
		self._LegValtnRate = value if type(value) != auto else self.make_default("LegValtnRate")

	@LegValtnRate.deleter
	def LegValtnRate(self):
		del self._LegValtnRate
		self._LegValtnRate = None

	@property
	def LegSttlmDt(self):
		return self._LegSttlmDt

	@LegSttlmDt.setter
	def LegSttlmDt(self, value):
		self._LegSttlmDt = value if type(value) != auto else self.make_default("LegSttlmDt")

	@LegSttlmDt.deleter
	def LegSttlmDt(self):
		del self._LegSttlmDt
		self._LegSttlmDt = None

	@property
	def LegSttlmTp(self):
		return self._LegSttlmTp

	@LegSttlmTp.setter
	def LegSttlmTp(self, value):
		self._LegSttlmTp = value if type(value) != auto else self.make_default("LegSttlmTp")

	@LegSttlmTp.deleter
	def LegSttlmTp(self):
		del self._LegSttlmTp
		self._LegSttlmTp = None

	@property
	def LegOrdrQty(self):
		return self._LegOrdrQty

	@LegOrdrQty.setter
	def LegOrdrQty(self, value):
		self._LegOrdrQty = value if type(value) != auto else self.make_default("LegOrdrQty")

	@LegOrdrQty.deleter
	def LegOrdrQty(self):
		del self._LegOrdrQty
		self._LegOrdrQty = None

	@property
	def LegSttlmCcy(self):
		return self._LegSttlmCcy

	@LegSttlmCcy.setter
	def LegSttlmCcy(self, value):
		self._LegSttlmCcy = value if type(value) != auto else self.make_default("LegSttlmCcy")

	@LegSttlmCcy.deleter
	def LegSttlmCcy(self):
		del self._LegSttlmCcy
		self._LegSttlmCcy = None

	@property
	def LegCcy(self):
		return self._LegCcy

	@LegCcy.setter
	def LegCcy(self, value):
		self._LegCcy = value if type(value) != auto else self.make_default("LegCcy")

	@LegCcy.deleter
	def LegCcy(self):
		del self._LegCcy
		self._LegCcy = None

	@property
	def LegFwdPts(self):
		return self._LegFwdPts

	@LegFwdPts.setter
	def LegFwdPts(self, value):
		self._LegFwdPts = value if type(value) != auto else self.make_default("LegFwdPts")

	@LegFwdPts.deleter
	def LegFwdPts(self):
		del self._LegFwdPts
		self._LegFwdPts = None

	@property
	def LegValDt(self):
		return self._LegValDt

	@LegValDt.setter
	def LegValDt(self, value):
		self._LegValDt = value if type(value) != auto else self.make_default("LegValDt")

	@LegValDt.deleter
	def LegValDt(self):
		del self._LegValDt
		self._LegValDt = None

	@property
	def LegLastPric(self):
		return self._LegLastPric

	@LegLastPric.setter
	def LegLastPric(self, value):
		self._LegLastPric = value if type(value) != auto else self.make_default("LegLastPric")

	@LegLastPric.deleter
	def LegLastPric(self):
		del self._LegLastPric
		self._LegLastPric = None

	@property
	def LegSymb(self):
		return self._LegSymb

	@LegSymb.setter
	def LegSymb(self, value):
		self._LegSymb = value if type(value) != auto else self.make_default("LegSymb")

	@LegSymb.deleter
	def LegSymb(self):
		del self._LegSymb
		self._LegSymb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LegRskAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSd', type=Side1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegClctdCtrPtyCcyLastQty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSctyId', type=SecurityIdentification18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegValtnRate', type=AgreedRate3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSttlmDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSttlmTp', type=SettlementDate8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegOrdrQty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSttlmCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegFwdPts', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegLastPric', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSymb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

