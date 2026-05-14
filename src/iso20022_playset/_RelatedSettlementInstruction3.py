# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountAndDirection110 import AmountAndDirection110
from ._DeliveryReceiptType2Code import DeliveryReceiptType2Code
from ._Max35Text import Max35Text
from ._PartyIdentification143 import PartyIdentification143
from ._Quantity51Choice import Quantity51Choice
from ._ReceiveDelivery1Code import ReceiveDelivery1Code
from ._SettlementDate17Choice import SettlementDate17Choice
from ._TradeDate8Choice import TradeDate8Choice
from ._UTIIdentifier import UTIIdentifier

class RelatedSettlementInstruction3(base_types._BaseFieldType):

	__slots__ = ["_CtrPtyDpstry", "_MktInfrstrctrTxId", "_Pmt", "_PrcrTxId", "_RltdSttlmInstrId", "_SctiesMvmntTp", "_SttlmAmt", "_SttlmDt", "_SttlmQty", "_TradDt", "_UnqTxIdr"]
	@property
	def CtrPtyDpstry(self):
		return self._CtrPtyDpstry

	@CtrPtyDpstry.setter
	def CtrPtyDpstry(self, value):
		self._CtrPtyDpstry = value if type(value) != base_types.auto else self.make_default("CtrPtyDpstry")

	@CtrPtyDpstry.deleter
	def CtrPtyDpstry(self):
		del self._CtrPtyDpstry
		self._CtrPtyDpstry = None

	@property
	def MktInfrstrctrTxId(self):
		return self._MktInfrstrctrTxId

	@MktInfrstrctrTxId.setter
	def MktInfrstrctrTxId(self, value):
		self._MktInfrstrctrTxId = value if type(value) != base_types.auto else self.make_default("MktInfrstrctrTxId")

	@MktInfrstrctrTxId.deleter
	def MktInfrstrctrTxId(self):
		del self._MktInfrstrctrTxId
		self._MktInfrstrctrTxId = None

	@property
	def Pmt(self):
		return self._Pmt

	@Pmt.setter
	def Pmt(self, value):
		self._Pmt = value if type(value) != base_types.auto else self.make_default("Pmt")

	@Pmt.deleter
	def Pmt(self):
		del self._Pmt
		self._Pmt = None

	@property
	def PrcrTxId(self):
		return self._PrcrTxId

	@PrcrTxId.setter
	def PrcrTxId(self, value):
		self._PrcrTxId = value if type(value) != base_types.auto else self.make_default("PrcrTxId")

	@PrcrTxId.deleter
	def PrcrTxId(self):
		del self._PrcrTxId
		self._PrcrTxId = None

	@property
	def RltdSttlmInstrId(self):
		return self._RltdSttlmInstrId

	@RltdSttlmInstrId.setter
	def RltdSttlmInstrId(self, value):
		self._RltdSttlmInstrId = value if type(value) != base_types.auto else self.make_default("RltdSttlmInstrId")

	@RltdSttlmInstrId.deleter
	def RltdSttlmInstrId(self):
		del self._RltdSttlmInstrId
		self._RltdSttlmInstrId = None

	@property
	def SctiesMvmntTp(self):
		return self._SctiesMvmntTp

	@SctiesMvmntTp.setter
	def SctiesMvmntTp(self, value):
		self._SctiesMvmntTp = value if type(value) != base_types.auto else self.make_default("SctiesMvmntTp")

	@SctiesMvmntTp.deleter
	def SctiesMvmntTp(self):
		del self._SctiesMvmntTp
		self._SctiesMvmntTp = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def SttlmQty(self):
		return self._SttlmQty

	@SttlmQty.setter
	def SttlmQty(self, value):
		self._SttlmQty = value if type(value) != base_types.auto else self.make_default("SttlmQty")

	@SttlmQty.deleter
	def SttlmQty(self):
		del self._SttlmQty
		self._SttlmQty = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != base_types.auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPtyDpstry', type=PartyIdentification143, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktInfrstrctrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pmt', type=DeliveryReceiptType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcrTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdSttlmInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesMvmntTp', type=ReceiveDelivery1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection110, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=SettlementDate17Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmQty', type=Quantity51Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))