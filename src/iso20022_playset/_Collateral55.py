# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashCollateral3
from . import Max140Text
from . import Max35Text
from . import OtherCollateral9
from . import SecuritiesCollateral10

class Collateral55(base_types._BaseFieldType):

	__slots__ = ["_CollPrpslRspnId", "_CshColl", "_MrgnCallReqId", "_MrgnCallRspnId", "_OthrColl", "_SctiesColl", "_StdSttlmInstrs"]
	@property
	def CollPrpslRspnId(self):
		return self._CollPrpslRspnId

	@CollPrpslRspnId.setter
	def CollPrpslRspnId(self, value):
		self._CollPrpslRspnId = value if value is not None else base_types.UninitialisedField(self, 'CollPrpslRspnId', Max35Text, False)

	@CollPrpslRspnId.deleter
	def CollPrpslRspnId(self):
		del self._CollPrpslRspnId
		self._CollPrpslRspnId = base_types.UninitialisedField(self, 'CollPrpslRspnId', Max35Text, False)

	@property
	def CshColl(self):
		return self._CshColl

	@CshColl.setter
	def CshColl(self, value):
		self._CshColl = value if value is not None else base_types.UninitialisedField(self, 'CshColl', CashCollateral3, True)

	@CshColl.deleter
	def CshColl(self):
		del self._CshColl
		self._CshColl = base_types.UninitialisedField(self, 'CshColl', CashCollateral3, True)

	@property
	def MrgnCallReqId(self):
		return self._MrgnCallReqId

	@MrgnCallReqId.setter
	def MrgnCallReqId(self, value):
		self._MrgnCallReqId = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallReqId', Max35Text, False)

	@MrgnCallReqId.deleter
	def MrgnCallReqId(self):
		del self._MrgnCallReqId
		self._MrgnCallReqId = base_types.UninitialisedField(self, 'MrgnCallReqId', Max35Text, False)

	@property
	def MrgnCallRspnId(self):
		return self._MrgnCallRspnId

	@MrgnCallRspnId.setter
	def MrgnCallRspnId(self, value):
		self._MrgnCallRspnId = value if value is not None else base_types.UninitialisedField(self, 'MrgnCallRspnId', Max35Text, False)

	@MrgnCallRspnId.deleter
	def MrgnCallRspnId(self):
		del self._MrgnCallRspnId
		self._MrgnCallRspnId = base_types.UninitialisedField(self, 'MrgnCallRspnId', Max35Text, False)

	@property
	def OthrColl(self):
		return self._OthrColl

	@OthrColl.setter
	def OthrColl(self, value):
		self._OthrColl = value if value is not None else base_types.UninitialisedField(self, 'OthrColl', OtherCollateral9, True)

	@OthrColl.deleter
	def OthrColl(self):
		del self._OthrColl
		self._OthrColl = base_types.UninitialisedField(self, 'OthrColl', OtherCollateral9, True)

	@property
	def SctiesColl(self):
		return self._SctiesColl

	@SctiesColl.setter
	def SctiesColl(self, value):
		self._SctiesColl = value if value is not None else base_types.UninitialisedField(self, 'SctiesColl', SecuritiesCollateral10, True)

	@SctiesColl.deleter
	def SctiesColl(self):
		del self._SctiesColl
		self._SctiesColl = base_types.UninitialisedField(self, 'SctiesColl', SecuritiesCollateral10, True)

	@property
	def StdSttlmInstrs(self):
		return self._StdSttlmInstrs

	@StdSttlmInstrs.setter
	def StdSttlmInstrs(self, value):
		self._StdSttlmInstrs = value if value is not None else base_types.UninitialisedField(self, 'StdSttlmInstrs', Max140Text, False)

	@StdSttlmInstrs.deleter
	def StdSttlmInstrs(self):
		del self._StdSttlmInstrs
		self._StdSttlmInstrs = base_types.UninitialisedField(self, 'StdSttlmInstrs', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrpslRspnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshColl', type=CashCollateral3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrgnCallReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallRspnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrColl', type=OtherCollateral9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesColl', type=SecuritiesCollateral10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StdSttlmInstrs', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))