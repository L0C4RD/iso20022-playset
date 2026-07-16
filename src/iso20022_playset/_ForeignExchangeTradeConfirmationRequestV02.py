# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ConfirmationRequest1Code
from . import Header23
from . import Max35NumericText
from . import MessageIdentification1
from . import Period12
from . import QueryTradeStatus1Code
from . import SupplementaryData1
from . import Trade9

class ForeignExchangeTradeConfirmationRequestV02(base_types._BaseFieldType):

	__slots__ = ["_ConfTp", "_Hdr", "_QryPrd", "_QryStartNb", "_QryTradSts", "_ReqId", "_SplmtryData", "_TradDtl"]
	@property
	def ConfTp(self):
		return self._ConfTp

	@ConfTp.setter
	def ConfTp(self, value):
		self._ConfTp = value if value is not None else base_types.UninitialisedField(self, 'ConfTp', ConfirmationRequest1Code, False)

	@ConfTp.deleter
	def ConfTp(self):
		del self._ConfTp
		self._ConfTp = base_types.UninitialisedField(self, 'ConfTp', ConfirmationRequest1Code, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header23, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header23, False)

	@property
	def QryPrd(self):
		return self._QryPrd

	@QryPrd.setter
	def QryPrd(self, value):
		self._QryPrd = value if value is not None else base_types.UninitialisedField(self, 'QryPrd', Period12, False)

	@QryPrd.deleter
	def QryPrd(self):
		del self._QryPrd
		self._QryPrd = base_types.UninitialisedField(self, 'QryPrd', Period12, False)

	@property
	def QryStartNb(self):
		return self._QryStartNb

	@QryStartNb.setter
	def QryStartNb(self, value):
		self._QryStartNb = value if value is not None else base_types.UninitialisedField(self, 'QryStartNb', Max35NumericText, False)

	@QryStartNb.deleter
	def QryStartNb(self):
		del self._QryStartNb
		self._QryStartNb = base_types.UninitialisedField(self, 'QryStartNb', Max35NumericText, False)

	@property
	def QryTradSts(self):
		return self._QryTradSts

	@QryTradSts.setter
	def QryTradSts(self, value):
		self._QryTradSts = value if value is not None else base_types.UninitialisedField(self, 'QryTradSts', QueryTradeStatus1Code, False)

	@QryTradSts.deleter
	def QryTradSts(self):
		del self._QryTradSts
		self._QryTradSts = base_types.UninitialisedField(self, 'QryTradSts', QueryTradeStatus1Code, False)

	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if value is not None else base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def TradDtl(self):
		return self._TradDtl

	@TradDtl.setter
	def TradDtl(self, value):
		self._TradDtl = value if value is not None else base_types.UninitialisedField(self, 'TradDtl', Trade9, False)

	@TradDtl.deleter
	def TradDtl(self):
		del self._TradDtl
		self._TradDtl = base_types.UninitialisedField(self, 'TradDtl', Trade9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ConfTp', type=ConfirmationRequest1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header23, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryPrd', type=Period12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryStartNb', type=Max35NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryTradSts', type=QueryTradeStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDtl', type=Trade9, min=1, max=1, mutex_group=None, array=False),
	))