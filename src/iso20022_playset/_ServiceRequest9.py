from . import base_types
from ._BalanceInquiryRequest9 import BalanceInquiryRequest9
from ._BatchRequest8 import BatchRequest8
from ._CardAcquisitionRequest3 import CardAcquisitionRequest3
from ._CardPaymentEnvironment82 import CardPaymentEnvironment82
from ._EnableServiceRequest7 import EnableServiceRequest7
from ._LoyaltyRequest8 import LoyaltyRequest8
from ._PaymentContext30 import PaymentContext30
from ._PaymentRequest8 import PaymentRequest8
from ._RetailerService2Code import RetailerService2Code
from ._ReversalRequest8 import ReversalRequest8
from ._StoredValueRequest9 import StoredValueRequest9
from ._SupplementaryData1 import SupplementaryData1

class ServiceRequest9(base_types._BaseFieldType):

	__slots__ = ["_BalNqryReq", "_BtchReq", "_CardAcqstnReq", "_Cntxt", "_Envt", "_LltyReq", "_NblSvcReq", "_PmtReq", "_RvslReq", "_SplmtryData", "_StordValReq", "_SvcCntt"]
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
		base_types.FieldEntry(name='BalNqryReq', type=BalanceInquiryRequest9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BtchReq', type=BatchRequest8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CardAcqstnReq', type=CardAcquisitionRequest3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LltyReq', type=LoyaltyRequest8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NblSvcReq', type=EnableServiceRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtReq', type=PaymentRequest8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RvslReq', type=ReversalRequest8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StordValReq', type=StoredValueRequest9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService2Code, min=1, max=1, mutex_group=None, array=False),
	))

