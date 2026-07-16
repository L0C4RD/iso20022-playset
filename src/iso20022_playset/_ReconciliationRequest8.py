# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment81
from . import PaymentContext30
from . import ReconciliationRequestData1
from . import SupplementaryData1

class ReconciliationRequest8(base_types._BaseFieldType):

	__slots__ = ["_Cntxt", "_Envt", "_RcncltnReqData", "_SplmtryData"]
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
	def RcncltnReqData(self):
		return self._RcncltnReqData

	@RcncltnReqData.setter
	def RcncltnReqData(self, value):
		self._RcncltnReqData = value if value is not None else base_types.UninitialisedField(self, 'RcncltnReqData', ReconciliationRequestData1, False)

	@RcncltnReqData.deleter
	def RcncltnReqData(self):
		del self._RcncltnReqData
		self._RcncltnReqData = base_types.UninitialisedField(self, 'RcncltnReqData', ReconciliationRequestData1, False)

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
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnReqData', type=ReconciliationRequestData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))