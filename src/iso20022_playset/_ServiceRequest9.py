# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceInquiryRequest9
from . import BatchRequest8
from . import CardAcquisitionRequest3
from . import CardPaymentEnvironment82
from . import EnableServiceRequest7
from . import LoyaltyRequest8
from . import PaymentContext30
from . import PaymentRequest8
from . import RetailerService2Code
from . import ReversalRequest8
from . import StoredValueRequest9
from . import SupplementaryData1

class ServiceRequest9(base_types._BaseFieldType):

	__slots__ = ["_BalNqryReq", "_BtchReq", "_CardAcqstnReq", "_Cntxt", "_Envt", "_LltyReq", "_NblSvcReq", "_PmtReq", "_RvslReq", "_SplmtryData", "_StordValReq", "_SvcCntt"]
	@property
	def BalNqryReq(self):
		return self._BalNqryReq

	@BalNqryReq.setter
	def BalNqryReq(self, value):
		self._BalNqryReq = value if value is not None else base_types.UninitialisedField(self, 'BalNqryReq', BalanceInquiryRequest9, False)

	@BalNqryReq.deleter
	def BalNqryReq(self):
		del self._BalNqryReq
		self._BalNqryReq = base_types.UninitialisedField(self, 'BalNqryReq', BalanceInquiryRequest9, False)

	@property
	def BtchReq(self):
		return self._BtchReq

	@BtchReq.setter
	def BtchReq(self, value):
		self._BtchReq = value if value is not None else base_types.UninitialisedField(self, 'BtchReq', BatchRequest8, False)

	@BtchReq.deleter
	def BtchReq(self):
		del self._BtchReq
		self._BtchReq = base_types.UninitialisedField(self, 'BtchReq', BatchRequest8, False)

	@property
	def CardAcqstnReq(self):
		return self._CardAcqstnReq

	@CardAcqstnReq.setter
	def CardAcqstnReq(self, value):
		self._CardAcqstnReq = value if value is not None else base_types.UninitialisedField(self, 'CardAcqstnReq', CardAcquisitionRequest3, False)

	@CardAcqstnReq.deleter
	def CardAcqstnReq(self):
		del self._CardAcqstnReq
		self._CardAcqstnReq = base_types.UninitialisedField(self, 'CardAcqstnReq', CardAcquisitionRequest3, False)

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if value is not None else base_types.UninitialisedField(self, 'Cntxt', PaymentContext30, False)

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = base_types.UninitialisedField(self, 'Cntxt', PaymentContext30, False)

	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment82, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment82, False)

	@property
	def LltyReq(self):
		return self._LltyReq

	@LltyReq.setter
	def LltyReq(self, value):
		self._LltyReq = value if value is not None else base_types.UninitialisedField(self, 'LltyReq', LoyaltyRequest8, False)

	@LltyReq.deleter
	def LltyReq(self):
		del self._LltyReq
		self._LltyReq = base_types.UninitialisedField(self, 'LltyReq', LoyaltyRequest8, False)

	@property
	def NblSvcReq(self):
		return self._NblSvcReq

	@NblSvcReq.setter
	def NblSvcReq(self, value):
		self._NblSvcReq = value if value is not None else base_types.UninitialisedField(self, 'NblSvcReq', EnableServiceRequest7, False)

	@NblSvcReq.deleter
	def NblSvcReq(self):
		del self._NblSvcReq
		self._NblSvcReq = base_types.UninitialisedField(self, 'NblSvcReq', EnableServiceRequest7, False)

	@property
	def PmtReq(self):
		return self._PmtReq

	@PmtReq.setter
	def PmtReq(self, value):
		self._PmtReq = value if value is not None else base_types.UninitialisedField(self, 'PmtReq', PaymentRequest8, False)

	@PmtReq.deleter
	def PmtReq(self):
		del self._PmtReq
		self._PmtReq = base_types.UninitialisedField(self, 'PmtReq', PaymentRequest8, False)

	@property
	def RvslReq(self):
		return self._RvslReq

	@RvslReq.setter
	def RvslReq(self, value):
		self._RvslReq = value if value is not None else base_types.UninitialisedField(self, 'RvslReq', ReversalRequest8, False)

	@RvslReq.deleter
	def RvslReq(self):
		del self._RvslReq
		self._RvslReq = base_types.UninitialisedField(self, 'RvslReq', ReversalRequest8, False)

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
	def StordValReq(self):
		return self._StordValReq

	@StordValReq.setter
	def StordValReq(self, value):
		self._StordValReq = value if value is not None else base_types.UninitialisedField(self, 'StordValReq', StoredValueRequest9, False)

	@StordValReq.deleter
	def StordValReq(self):
		del self._StordValReq
		self._StordValReq = base_types.UninitialisedField(self, 'StordValReq', StoredValueRequest9, False)

	@property
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if value is not None else base_types.UninitialisedField(self, 'SvcCntt', RetailerService2Code, False)

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = base_types.UninitialisedField(self, 'SvcCntt', RetailerService2Code, False)

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