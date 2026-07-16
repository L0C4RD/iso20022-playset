# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment82
from . import MessageStatusRequestData2
from . import PaymentContext30
from . import SupplementaryData1

class MessageStatusRequest9(base_types._BaseFieldType):

	__slots__ = ["_Cntxt", "_Envt", "_MsgStsReqData", "_SplmtryData"]
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
	def MsgStsReqData(self):
		return self._MsgStsReqData

	@MsgStsReqData.setter
	def MsgStsReqData(self, value):
		self._MsgStsReqData = value if value is not None else base_types.UninitialisedField(self, 'MsgStsReqData', MessageStatusRequestData2, False)

	@MsgStsReqData.deleter
	def MsgStsReqData(self):
		del self._MsgStsReqData
		self._MsgStsReqData = base_types.UninitialisedField(self, 'MsgStsReqData', MessageStatusRequestData2, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgStsReqData', type=MessageStatusRequestData2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))