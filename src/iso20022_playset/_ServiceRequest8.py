from . import base_types
from ._EnableServiceRequest6 import EnableServiceRequest6
from ._BalanceInquiryRequest8 import BalanceInquiryRequest8
from ._PaymentRequest7 import PaymentRequest7
from ._BatchRequest7 import BatchRequest7
from ._LoyaltyRequest7 import LoyaltyRequest7
from ._CardPaymentEnvironment81 import CardPaymentEnvironment81
from ._StoredValueRequest8 import StoredValueRequest8
from ._ReversalRequest7 import ReversalRequest7
from ._RetailerService2Code import RetailerService2Code
from ._SupplementaryData1 import SupplementaryData1
from ._PaymentContext30 import PaymentContext30
from ._CardAcquisitionRequest3 import CardAcquisitionRequest3

class ServiceRequest8(base_types._BaseFieldType):

	__slots__ = ["_CardAcqstnReq", "_PmtReq", "_NblSvcReq", "_SplmtryData", "_RvslReq", "_Cntxt", "_StordValReq", "_BtchReq", "_SvcCntt", "_LltyReq", "_Envt", "_BalNqryReq"]
	@property
	def CardAcqstnReq(self):
		return self._CardAcqstnReq

	@CardAcqstnReq.setter
	def CardAcqstnReq(self, value):
		self._CardAcqstnReq = value if type(value) != base_types.auto else self.make_default("CardAcqstnReq")

	@CardAcqstnReq.deleter
	def CardAcqstnReq(self):
		del self._CardAcqstnReq
		self._CardAcqstnReq = None

	@property
	def PmtReq(self):
		return self._PmtReq

	@PmtReq.setter
	def PmtReq(self, value):
		self._PmtReq = value if type(value) != base_types.auto else self.make_default("PmtReq")

	@PmtReq.deleter
	def PmtReq(self):
		del self._PmtReq
		self._PmtReq = None

	@property
	def NblSvcReq(self):
		return self._NblSvcReq

	@NblSvcReq.setter
	def NblSvcReq(self, value):
		self._NblSvcReq = value if type(value) != base_types.auto else self.make_default("NblSvcReq")

	@NblSvcReq.deleter
	def NblSvcReq(self):
		del self._NblSvcReq
		self._NblSvcReq = None

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
	def RvslReq(self):
		return self._RvslReq

	@RvslReq.setter
	def RvslReq(self, value):
		self._RvslReq = value if type(value) != base_types.auto else self.make_default("RvslReq")

	@RvslReq.deleter
	def RvslReq(self):
		del self._RvslReq
		self._RvslReq = None

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
	def StordValReq(self):
		return self._StordValReq

	@StordValReq.setter
	def StordValReq(self, value):
		self._StordValReq = value if type(value) != base_types.auto else self.make_default("StordValReq")

	@StordValReq.deleter
	def StordValReq(self):
		del self._StordValReq
		self._StordValReq = None

	@property
	def BtchReq(self):
		return self._BtchReq

	@BtchReq.setter
	def BtchReq(self, value):
		self._BtchReq = value if type(value) != base_types.auto else self.make_default("BtchReq")

	@BtchReq.deleter
	def BtchReq(self):
		del self._BtchReq
		self._BtchReq = None

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

	@property
	def LltyReq(self):
		return self._LltyReq

	@LltyReq.setter
	def LltyReq(self, value):
		self._LltyReq = value if type(value) != base_types.auto else self.make_default("LltyReq")

	@LltyReq.deleter
	def LltyReq(self):
		del self._LltyReq
		self._LltyReq = None

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
	def BalNqryReq(self):
		return self._BalNqryReq

	@BalNqryReq.setter
	def BalNqryReq(self, value):
		self._BalNqryReq = value if type(value) != base_types.auto else self.make_default("BalNqryReq")

	@BalNqryReq.deleter
	def BalNqryReq(self):
		del self._BalNqryReq
		self._BalNqryReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CardAcqstnReq', type=CardAcquisitionRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtReq', type=PaymentRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NblSvcReq', type=EnableServiceRequest6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RvslReq', type=ReversalRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StordValReq', type=StoredValueRequest8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchReq', type=BatchRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyReq', type=LoyaltyRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalNqryReq', type=BalanceInquiryRequest8, min=0, max=1, mutex_group=None, array=False),
	))

