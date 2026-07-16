# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment81
from . import DiagnosisRequest1
from . import LoginRequest7
from . import LogoutRequest1
from . import PaymentContext30
from . import RetailerService4Code
from . import SupplementaryData1

class SessionManagementRequest8(base_types._BaseFieldType):

	__slots__ = ["_Cntxt", "_DgnssReq", "_Envt", "_LgnReq", "_LgtReq", "_SplmtryData", "_SvcCntt"]
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
	def DgnssReq(self):
		return self._DgnssReq

	@DgnssReq.setter
	def DgnssReq(self, value):
		self._DgnssReq = value if value is not None else base_types.UninitialisedField(self, 'DgnssReq', DiagnosisRequest1, False)

	@DgnssReq.deleter
	def DgnssReq(self):
		del self._DgnssReq
		self._DgnssReq = base_types.UninitialisedField(self, 'DgnssReq', DiagnosisRequest1, False)

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
	def LgnReq(self):
		return self._LgnReq

	@LgnReq.setter
	def LgnReq(self, value):
		self._LgnReq = value if value is not None else base_types.UninitialisedField(self, 'LgnReq', LoginRequest7, False)

	@LgnReq.deleter
	def LgnReq(self):
		del self._LgnReq
		self._LgnReq = base_types.UninitialisedField(self, 'LgnReq', LoginRequest7, False)

	@property
	def LgtReq(self):
		return self._LgtReq

	@LgtReq.setter
	def LgtReq(self, value):
		self._LgtReq = value if value is not None else base_types.UninitialisedField(self, 'LgtReq', LogoutRequest1, False)

	@LgtReq.deleter
	def LgtReq(self):
		del self._LgtReq
		self._LgtReq = base_types.UninitialisedField(self, 'LgtReq', LogoutRequest1, False)

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
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if value is not None else base_types.UninitialisedField(self, 'SvcCntt', RetailerService4Code, False)

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = base_types.UninitialisedField(self, 'SvcCntt', RetailerService4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgnssReq', type=DiagnosisRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LgnReq', type=LoginRequest7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LgtReq', type=LogoutRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService4Code, min=1, max=1, mutex_group=None, array=False),
	))