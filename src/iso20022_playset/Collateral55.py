import base_types
import Max35Text
import CashCollateral3
import Max140Text
import SecuritiesCollateral10
import OtherCollateral9

class Collateral55(base_types._BaseFieldType):

	__slots__ = ["_SctiesColl", "_CollPrpslRspnId", "_MrgnCallReqId", "_CshColl", "_MrgnCallRspnId", "_OthrColl", "_StdSttlmInstrs"]
	@property
	def SctiesColl(self):
		return self._SctiesColl

	@SctiesColl.setter
	def SctiesColl(self, value):
		self._SctiesColl = value if type(value) != auto else self.make_default("SctiesColl")

	@SctiesColl.deleter
	def SctiesColl(self):
		del self._SctiesColl
		self._SctiesColl = None

	@property
	def CollPrpslRspnId(self):
		return self._CollPrpslRspnId

	@CollPrpslRspnId.setter
	def CollPrpslRspnId(self, value):
		self._CollPrpslRspnId = value if type(value) != auto else self.make_default("CollPrpslRspnId")

	@CollPrpslRspnId.deleter
	def CollPrpslRspnId(self):
		del self._CollPrpslRspnId
		self._CollPrpslRspnId = None

	@property
	def MrgnCallReqId(self):
		return self._MrgnCallReqId

	@MrgnCallReqId.setter
	def MrgnCallReqId(self, value):
		self._MrgnCallReqId = value if type(value) != auto else self.make_default("MrgnCallReqId")

	@MrgnCallReqId.deleter
	def MrgnCallReqId(self):
		del self._MrgnCallReqId
		self._MrgnCallReqId = None

	@property
	def CshColl(self):
		return self._CshColl

	@CshColl.setter
	def CshColl(self, value):
		self._CshColl = value if type(value) != auto else self.make_default("CshColl")

	@CshColl.deleter
	def CshColl(self):
		del self._CshColl
		self._CshColl = None

	@property
	def MrgnCallRspnId(self):
		return self._MrgnCallRspnId

	@MrgnCallRspnId.setter
	def MrgnCallRspnId(self, value):
		self._MrgnCallRspnId = value if type(value) != auto else self.make_default("MrgnCallRspnId")

	@MrgnCallRspnId.deleter
	def MrgnCallRspnId(self):
		del self._MrgnCallRspnId
		self._MrgnCallRspnId = None

	@property
	def OthrColl(self):
		return self._OthrColl

	@OthrColl.setter
	def OthrColl(self, value):
		self._OthrColl = value if type(value) != auto else self.make_default("OthrColl")

	@OthrColl.deleter
	def OthrColl(self):
		del self._OthrColl
		self._OthrColl = None

	@property
	def StdSttlmInstrs(self):
		return self._StdSttlmInstrs

	@StdSttlmInstrs.setter
	def StdSttlmInstrs(self, value):
		self._StdSttlmInstrs = value if type(value) != auto else self.make_default("StdSttlmInstrs")

	@StdSttlmInstrs.deleter
	def StdSttlmInstrs(self):
		del self._StdSttlmInstrs
		self._StdSttlmInstrs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctiesColl', type=SecuritiesCollateral10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CollPrpslRspnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshColl', type=CashCollateral3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrgnCallRspnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrColl', type=OtherCollateral9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StdSttlmInstrs', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

