# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment81
from . import DiagnosisResponse7
from . import LoginResponse7
from . import PaymentContext30
from . import ResponseType11
from . import RetailerService5Code
from . import SupplementaryData1

class SessionManagementResponse8(base_types._BaseFieldType):

	__slots__ = ["_Cntxt", "_DgnssRspn", "_Envt", "_LgnRspn", "_Rspn", "_SplmtryData", "_SvcCntt"]
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
	def DgnssRspn(self):
		return self._DgnssRspn

	@DgnssRspn.setter
	def DgnssRspn(self, value):
		self._DgnssRspn = value if value is not None else base_types.UninitialisedField(self, 'DgnssRspn', DiagnosisResponse7, False)

	@DgnssRspn.deleter
	def DgnssRspn(self):
		del self._DgnssRspn
		self._DgnssRspn = base_types.UninitialisedField(self, 'DgnssRspn', DiagnosisResponse7, False)

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
	def LgnRspn(self):
		return self._LgnRspn

	@LgnRspn.setter
	def LgnRspn(self, value):
		self._LgnRspn = value if value is not None else base_types.UninitialisedField(self, 'LgnRspn', LoginResponse7, False)

	@LgnRspn.deleter
	def LgnRspn(self):
		del self._LgnRspn
		self._LgnRspn = base_types.UninitialisedField(self, 'LgnRspn', LoginResponse7, False)

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
		self._SvcCntt = value if value is not None else base_types.UninitialisedField(self, 'SvcCntt', RetailerService5Code, False)

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = base_types.UninitialisedField(self, 'SvcCntt', RetailerService5Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgnssRspn', type=DiagnosisResponse7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LgnRspn', type=LoginResponse7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=ResponseType11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService5Code, min=1, max=1, mutex_group=None, array=False),
	))