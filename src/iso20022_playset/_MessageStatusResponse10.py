# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardPaymentEnvironment82 import CardPaymentEnvironment82
from ._MessageStatusResponseData10 import MessageStatusResponseData10
from ._PaymentContext30 import PaymentContext30
from ._ResponseType11 import ResponseType11
from ._SupplementaryData1 import SupplementaryData1

class MessageStatusResponse10(base_types._BaseFieldType):

	__slots__ = ["_Cntxt", "_Envt", "_MsgStsRspnData", "_Rspn", "_SplmtryData"]
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
	def MsgStsRspnData(self):
		return self._MsgStsRspnData

	@MsgStsRspnData.setter
	def MsgStsRspnData(self, value):
		self._MsgStsRspnData = value if type(value) != base_types.auto else self.make_default("MsgStsRspnData")

	@MsgStsRspnData.deleter
	def MsgStsRspnData(self):
		del self._MsgStsRspnData
		self._MsgStsRspnData = None

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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgStsRspnData', type=MessageStatusResponseData10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))