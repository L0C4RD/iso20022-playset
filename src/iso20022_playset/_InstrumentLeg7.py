# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import ActiveCurrencyAndAmount
from . import ActiveCurrencyCode
from . import AgreedRate3
from . import DecimalNumber
from . import ISODate
from . import ISODateTime
from . import Max35Text
from . import SecurityIdentification18
from . import SettlementDate8Code
from . import Side1Code

class InstrumentLeg7(base_types._BaseFieldType):

	__slots__ = ["_LegCcy", "_LegClctdCtrPtyCcyLastQty", "_LegFwdPts", "_LegLastPric", "_LegOrdrQty", "_LegRskAmt", "_LegSctyId", "_LegSd", "_LegSttlmCcy", "_LegSttlmDt", "_LegSttlmTp", "_LegSymb", "_LegValDt", "_LegValtnRate"]
	@property
	def LegCcy(self):
		return self._LegCcy

	@LegCcy.setter
	def LegCcy(self, value):
		self._LegCcy = value if value is not None else base_types.UninitialisedField(self, 'LegCcy', ActiveCurrencyCode, False)

	@LegCcy.deleter
	def LegCcy(self):
		del self._LegCcy
		self._LegCcy = base_types.UninitialisedField(self, 'LegCcy', ActiveCurrencyCode, False)

	@property
	def LegClctdCtrPtyCcyLastQty(self):
		return self._LegClctdCtrPtyCcyLastQty

	@LegClctdCtrPtyCcyLastQty.setter
	def LegClctdCtrPtyCcyLastQty(self, value):
		self._LegClctdCtrPtyCcyLastQty = value if value is not None else base_types.UninitialisedField(self, 'LegClctdCtrPtyCcyLastQty', ActiveCurrencyAndAmount, False)

	@LegClctdCtrPtyCcyLastQty.deleter
	def LegClctdCtrPtyCcyLastQty(self):
		del self._LegClctdCtrPtyCcyLastQty
		self._LegClctdCtrPtyCcyLastQty = base_types.UninitialisedField(self, 'LegClctdCtrPtyCcyLastQty', ActiveCurrencyAndAmount, False)

	@property
	def LegFwdPts(self):
		return self._LegFwdPts

	@LegFwdPts.setter
	def LegFwdPts(self, value):
		self._LegFwdPts = value if value is not None else base_types.UninitialisedField(self, 'LegFwdPts', DecimalNumber, False)

	@LegFwdPts.deleter
	def LegFwdPts(self):
		del self._LegFwdPts
		self._LegFwdPts = base_types.UninitialisedField(self, 'LegFwdPts', DecimalNumber, False)

	@property
	def LegLastPric(self):
		return self._LegLastPric

	@LegLastPric.setter
	def LegLastPric(self, value):
		self._LegLastPric = value if value is not None else base_types.UninitialisedField(self, 'LegLastPric', ActiveCurrencyAnd13DecimalAmount, False)

	@LegLastPric.deleter
	def LegLastPric(self):
		del self._LegLastPric
		self._LegLastPric = base_types.UninitialisedField(self, 'LegLastPric', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def LegOrdrQty(self):
		return self._LegOrdrQty

	@LegOrdrQty.setter
	def LegOrdrQty(self, value):
		self._LegOrdrQty = value if value is not None else base_types.UninitialisedField(self, 'LegOrdrQty', ActiveCurrencyAndAmount, False)

	@LegOrdrQty.deleter
	def LegOrdrQty(self):
		del self._LegOrdrQty
		self._LegOrdrQty = base_types.UninitialisedField(self, 'LegOrdrQty', ActiveCurrencyAndAmount, False)

	@property
	def LegRskAmt(self):
		return self._LegRskAmt

	@LegRskAmt.setter
	def LegRskAmt(self, value):
		self._LegRskAmt = value if value is not None else base_types.UninitialisedField(self, 'LegRskAmt', ActiveCurrencyAndAmount, False)

	@LegRskAmt.deleter
	def LegRskAmt(self):
		del self._LegRskAmt
		self._LegRskAmt = base_types.UninitialisedField(self, 'LegRskAmt', ActiveCurrencyAndAmount, False)

	@property
	def LegSctyId(self):
		return self._LegSctyId

	@LegSctyId.setter
	def LegSctyId(self, value):
		self._LegSctyId = value if value is not None else base_types.UninitialisedField(self, 'LegSctyId', SecurityIdentification18, False)

	@LegSctyId.deleter
	def LegSctyId(self):
		del self._LegSctyId
		self._LegSctyId = base_types.UninitialisedField(self, 'LegSctyId', SecurityIdentification18, False)

	@property
	def LegSd(self):
		return self._LegSd

	@LegSd.setter
	def LegSd(self, value):
		self._LegSd = value if value is not None else base_types.UninitialisedField(self, 'LegSd', Side1Code, False)

	@LegSd.deleter
	def LegSd(self):
		del self._LegSd
		self._LegSd = base_types.UninitialisedField(self, 'LegSd', Side1Code, False)

	@property
	def LegSttlmCcy(self):
		return self._LegSttlmCcy

	@LegSttlmCcy.setter
	def LegSttlmCcy(self, value):
		self._LegSttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'LegSttlmCcy', ActiveCurrencyCode, False)

	@LegSttlmCcy.deleter
	def LegSttlmCcy(self):
		del self._LegSttlmCcy
		self._LegSttlmCcy = base_types.UninitialisedField(self, 'LegSttlmCcy', ActiveCurrencyCode, False)

	@property
	def LegSttlmDt(self):
		return self._LegSttlmDt

	@LegSttlmDt.setter
	def LegSttlmDt(self, value):
		self._LegSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'LegSttlmDt', ISODateTime, False)

	@LegSttlmDt.deleter
	def LegSttlmDt(self):
		del self._LegSttlmDt
		self._LegSttlmDt = base_types.UninitialisedField(self, 'LegSttlmDt', ISODateTime, False)

	@property
	def LegSttlmTp(self):
		return self._LegSttlmTp

	@LegSttlmTp.setter
	def LegSttlmTp(self, value):
		self._LegSttlmTp = value if value is not None else base_types.UninitialisedField(self, 'LegSttlmTp', SettlementDate8Code, False)

	@LegSttlmTp.deleter
	def LegSttlmTp(self):
		del self._LegSttlmTp
		self._LegSttlmTp = base_types.UninitialisedField(self, 'LegSttlmTp', SettlementDate8Code, False)

	@property
	def LegSymb(self):
		return self._LegSymb

	@LegSymb.setter
	def LegSymb(self, value):
		self._LegSymb = value if value is not None else base_types.UninitialisedField(self, 'LegSymb', Max35Text, False)

	@LegSymb.deleter
	def LegSymb(self):
		del self._LegSymb
		self._LegSymb = base_types.UninitialisedField(self, 'LegSymb', Max35Text, False)

	@property
	def LegValDt(self):
		return self._LegValDt

	@LegValDt.setter
	def LegValDt(self, value):
		self._LegValDt = value if value is not None else base_types.UninitialisedField(self, 'LegValDt', ISODate, False)

	@LegValDt.deleter
	def LegValDt(self):
		del self._LegValDt
		self._LegValDt = base_types.UninitialisedField(self, 'LegValDt', ISODate, False)

	@property
	def LegValtnRate(self):
		return self._LegValtnRate

	@LegValtnRate.setter
	def LegValtnRate(self, value):
		self._LegValtnRate = value if value is not None else base_types.UninitialisedField(self, 'LegValtnRate', AgreedRate3, False)

	@LegValtnRate.deleter
	def LegValtnRate(self):
		del self._LegValtnRate
		self._LegValtnRate = base_types.UninitialisedField(self, 'LegValtnRate', AgreedRate3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LegCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegClctdCtrPtyCcyLastQty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegFwdPts', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegLastPric', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegOrdrQty', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegRskAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSctyId', type=SecurityIdentification18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSd', type=Side1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSttlmCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSttlmDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSttlmTp', type=SettlementDate8Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegSymb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegValDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegValtnRate', type=AgreedRate3, min=1, max=1, mutex_group=None, array=False),
	))