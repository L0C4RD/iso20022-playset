from . import base_types
from ._BatchResponse7 import BatchResponse7
from ._CardPaymentEnvironment81 import CardPaymentEnvironment81
from ._SupplementaryData1 import SupplementaryData1
from ._ReversalResponse9 import ReversalResponse9
from ._RetailerService3Code import RetailerService3Code
from ._CardAcquisitionResponse3 import CardAcquisitionResponse3
from ._BalanceInquiryResponse6 import BalanceInquiryResponse6
from ._PaymentContext30 import PaymentContext30
from ._ResponseType11 import ResponseType11
from ._StoredValueResponse8 import StoredValueResponse8
from ._LoyaltyResponse3 import LoyaltyResponse3
from ._PaymentResponse7 import PaymentResponse7

class ServiceResponse9(base_types._BaseFieldType):

	__slots__ = ["_BtchRspn", "_StordValRspn", "_PmtRspn", "_LltyRspn", "_BalNqryRspn", "_SvcCntt", "_RvslRspn", "_Rspn", "_Cntxt", "_CardAcqstnRspn", "_Envt", "_SplmtryData"]
	@property
	def BalNqryRspn(self):
		return self._BalNqryRspn

	@BalNqryRspn.setter
	def BalNqryRspn(self, value):
		self._BalNqryRspn = value if type(value) != base_types.auto else self.make_default("BalNqryRspn")

	@BalNqryRspn.deleter
	def BalNqryRspn(self):
		del self._BalNqryRspn
		self._BalNqryRspn = None

	@property
	def BtchRspn(self):
		return self._BtchRspn

	@BtchRspn.setter
	def BtchRspn(self, value):
		self._BtchRspn = value if type(value) != base_types.auto else self.make_default("BtchRspn")

	@BtchRspn.deleter
	def BtchRspn(self):
		del self._BtchRspn
		self._BtchRspn = None

	@property
	def CardAcqstnRspn(self):
		return self._CardAcqstnRspn

	@CardAcqstnRspn.setter
	def CardAcqstnRspn(self, value):
		self._CardAcqstnRspn = value if type(value) != base_types.auto else self.make_default("CardAcqstnRspn")

	@CardAcqstnRspn.deleter
	def CardAcqstnRspn(self):
		del self._CardAcqstnRspn
		self._CardAcqstnRspn = None

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if type(value) != base_types.auto else self.make_default("Cntxt")

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = None

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def LltyRspn(self):
		return self._LltyRspn

	@LltyRspn.setter
	def LltyRspn(self, value):
		self._LltyRspn = value if type(value) != base_types.auto else self.make_default("LltyRspn")

	@LltyRspn.deleter
	def LltyRspn(self):
		del self._LltyRspn
		self._LltyRspn = None

	@property
	def PmtRspn(self):
		return self._PmtRspn

	@PmtRspn.setter
	def PmtRspn(self, value):
		self._PmtRspn = value if type(value) != base_types.auto else self.make_default("PmtRspn")

	@PmtRspn.deleter
	def PmtRspn(self):
		del self._PmtRspn
		self._PmtRspn = None

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if type(value) != base_types.auto else self.make_default("Rspn")

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = None

	@property
	def RvslRspn(self):
		return self._RvslRspn

	@RvslRspn.setter
	def RvslRspn(self, value):
		self._RvslRspn = value if type(value) != base_types.auto else self.make_default("RvslRspn")

	@RvslRspn.deleter
	def RvslRspn(self):
		del self._RvslRspn
		self._RvslRspn = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def StordValRspn(self):
		return self._StordValRspn

	@StordValRspn.setter
	def StordValRspn(self, value):
		self._StordValRspn = value if type(value) != base_types.auto else self.make_default("StordValRspn")

	@StordValRspn.deleter
	def StordValRspn(self):
		del self._StordValRspn
		self._StordValRspn = None

	@property
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if type(value) != base_types.auto else self.make_default("SvcCntt")

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalNqryRspn', type=BalanceInquiryResponse6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchRspn', type=BatchResponse7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardAcqstnRspn', type=CardAcquisitionResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyRspn', type=LoyaltyResponse3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtRspn', type=PaymentResponse7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslRspn', type=ReversalResponse9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StordValRspn', type=StoredValueResponse8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService3Code, min=1, max=1, mutex_group=None, array=False),
	))

