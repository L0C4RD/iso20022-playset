# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BalanceInquiryResponse6
from . import BatchResponse7
from . import CardAcquisitionResponse3
from . import CardPaymentEnvironment81
from . import LoyaltyResponse3
from . import PaymentContext30
from . import PaymentResponse7
from . import ResponseType11
from . import RetailerService3Code
from . import ReversalResponse9
from . import StoredValueResponse8
from . import SupplementaryData1

class ServiceResponse9(base_types._BaseFieldType):

	__slots__ = ["_BalNqryRspn", "_BtchRspn", "_CardAcqstnRspn", "_Cntxt", "_Envt", "_LltyRspn", "_PmtRspn", "_Rspn", "_RvslRspn", "_SplmtryData", "_StordValRspn", "_SvcCntt"]
	@property
	def BalNqryRspn(self):
		return self._BalNqryRspn

	@BalNqryRspn.setter
	def BalNqryRspn(self, value):
		self._BalNqryRspn = value if value is not None else base_types.UninitialisedField(self, 'BalNqryRspn', BalanceInquiryResponse6, False)

	@BalNqryRspn.deleter
	def BalNqryRspn(self):
		del self._BalNqryRspn
		self._BalNqryRspn = base_types.UninitialisedField(self, 'BalNqryRspn', BalanceInquiryResponse6, False)

	@property
	def BtchRspn(self):
		return self._BtchRspn

	@BtchRspn.setter
	def BtchRspn(self, value):
		self._BtchRspn = value if value is not None else base_types.UninitialisedField(self, 'BtchRspn', BatchResponse7, False)

	@BtchRspn.deleter
	def BtchRspn(self):
		del self._BtchRspn
		self._BtchRspn = base_types.UninitialisedField(self, 'BtchRspn', BatchResponse7, False)

	@property
	def CardAcqstnRspn(self):
		return self._CardAcqstnRspn

	@CardAcqstnRspn.setter
	def CardAcqstnRspn(self, value):
		self._CardAcqstnRspn = value if value is not None else base_types.UninitialisedField(self, 'CardAcqstnRspn', CardAcquisitionResponse3, False)

	@CardAcqstnRspn.deleter
	def CardAcqstnRspn(self):
		del self._CardAcqstnRspn
		self._CardAcqstnRspn = base_types.UninitialisedField(self, 'CardAcqstnRspn', CardAcquisitionResponse3, False)

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
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment81, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment81, False)

	@property
	def LltyRspn(self):
		return self._LltyRspn

	@LltyRspn.setter
	def LltyRspn(self, value):
		self._LltyRspn = value if value is not None else base_types.UninitialisedField(self, 'LltyRspn', LoyaltyResponse3, False)

	@LltyRspn.deleter
	def LltyRspn(self):
		del self._LltyRspn
		self._LltyRspn = base_types.UninitialisedField(self, 'LltyRspn', LoyaltyResponse3, False)

	@property
	def PmtRspn(self):
		return self._PmtRspn

	@PmtRspn.setter
	def PmtRspn(self, value):
		self._PmtRspn = value if value is not None else base_types.UninitialisedField(self, 'PmtRspn', PaymentResponse7, False)

	@PmtRspn.deleter
	def PmtRspn(self):
		del self._PmtRspn
		self._PmtRspn = base_types.UninitialisedField(self, 'PmtRspn', PaymentResponse7, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', ResponseType11, False)

	@property
	def RvslRspn(self):
		return self._RvslRspn

	@RvslRspn.setter
	def RvslRspn(self, value):
		self._RvslRspn = value if value is not None else base_types.UninitialisedField(self, 'RvslRspn', ReversalResponse9, False)

	@RvslRspn.deleter
	def RvslRspn(self):
		del self._RvslRspn
		self._RvslRspn = base_types.UninitialisedField(self, 'RvslRspn', ReversalResponse9, False)

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
	def StordValRspn(self):
		return self._StordValRspn

	@StordValRspn.setter
	def StordValRspn(self, value):
		self._StordValRspn = value if value is not None else base_types.UninitialisedField(self, 'StordValRspn', StoredValueResponse8, False)

	@StordValRspn.deleter
	def StordValRspn(self):
		del self._StordValRspn
		self._StordValRspn = base_types.UninitialisedField(self, 'StordValRspn', StoredValueResponse8, False)

	@property
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if value is not None else base_types.UninitialisedField(self, 'SvcCntt', RetailerService3Code, False)

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = base_types.UninitialisedField(self, 'SvcCntt', RetailerService3Code, False)

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