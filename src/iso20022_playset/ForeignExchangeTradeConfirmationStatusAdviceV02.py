import base_types
import SupplementaryData1
import Header23
import Trade8
import TradePartyIdentification10
import Confirmation1
import AdditionalReferences2
import MessageIdentification1
import TradePartyIdentification9

class ForeignExchangeTradeConfirmationStatusAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_TradDtl", "_ConfInf", "_Hdr", "_AdvcId", "_CtrPtySdId", "_TradgSdId", "_SplmtryData", "_Ref"]
	@property
	def TradDtl(self):
		return self._TradDtl

	@TradDtl.setter
	def TradDtl(self, value):
		self._TradDtl = value if type(value) != auto else self.make_default("TradDtl")

	@TradDtl.deleter
	def TradDtl(self):
		del self._TradDtl
		self._TradDtl = None

	@property
	def ConfInf(self):
		return self._ConfInf

	@ConfInf.setter
	def ConfInf(self, value):
		self._ConfInf = value if type(value) != auto else self.make_default("ConfInf")

	@ConfInf.deleter
	def ConfInf(self):
		del self._ConfInf
		self._ConfInf = None

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if type(value) != auto else self.make_default("Hdr")

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = None

	@property
	def AdvcId(self):
		return self._AdvcId

	@AdvcId.setter
	def AdvcId(self, value):
		self._AdvcId = value if type(value) != auto else self.make_default("AdvcId")

	@AdvcId.deleter
	def AdvcId(self):
		del self._AdvcId
		self._AdvcId = None

	@property
	def CtrPtySdId(self):
		return self._CtrPtySdId

	@CtrPtySdId.setter
	def CtrPtySdId(self, value):
		self._CtrPtySdId = value if type(value) != auto else self.make_default("CtrPtySdId")

	@CtrPtySdId.deleter
	def CtrPtySdId(self):
		del self._CtrPtySdId
		self._CtrPtySdId = None

	@property
	def TradgSdId(self):
		return self._TradgSdId

	@TradgSdId.setter
	def TradgSdId(self, value):
		self._TradgSdId = value if type(value) != auto else self.make_default("TradgSdId")

	@TradgSdId.deleter
	def TradgSdId(self):
		del self._TradgSdId
		self._TradgSdId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradDtl', type=Trade8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfInf', type=Confirmation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header23, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdvcId', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtySdId', type=TradePartyIdentification10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgSdId', type=TradePartyIdentification9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ref', type=AdditionalReferences2, min=0, max=1, mutex_group=None, array=False),
	))

