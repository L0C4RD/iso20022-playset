# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancingRateOrAmountChoice
from . import Max105Text
from . import RequestStatus1Code
from . import StatusReason4Choice

class FinancingResult1(base_types._BaseFieldType):

	__slots__ = ["_AddtlStsRsnInf", "_FincdAmt", "_FincgReqSts", "_StsRsn"]
	@property
	def AddtlStsRsnInf(self):
		return self._AddtlStsRsnInf

	@AddtlStsRsnInf.setter
	def AddtlStsRsnInf(self, value):
		self._AddtlStsRsnInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlStsRsnInf', Max105Text, True)

	@AddtlStsRsnInf.deleter
	def AddtlStsRsnInf(self):
		del self._AddtlStsRsnInf
		self._AddtlStsRsnInf = base_types.UninitialisedField(self, 'AddtlStsRsnInf', Max105Text, True)

	@property
	def FincdAmt(self):
		return self._FincdAmt

	@FincdAmt.setter
	def FincdAmt(self, value):
		self._FincdAmt = value if value is not None else base_types.UninitialisedField(self, 'FincdAmt', FinancingRateOrAmountChoice, False)

	@FincdAmt.deleter
	def FincdAmt(self):
		del self._FincdAmt
		self._FincdAmt = base_types.UninitialisedField(self, 'FincdAmt', FinancingRateOrAmountChoice, False)

	@property
	def FincgReqSts(self):
		return self._FincgReqSts

	@FincgReqSts.setter
	def FincgReqSts(self, value):
		self._FincgReqSts = value if value is not None else base_types.UninitialisedField(self, 'FincgReqSts', RequestStatus1Code, False)

	@FincgReqSts.deleter
	def FincgReqSts(self):
		del self._FincgReqSts
		self._FincgReqSts = base_types.UninitialisedField(self, 'FincgReqSts', RequestStatus1Code, False)

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if value is not None else base_types.UninitialisedField(self, 'StsRsn', StatusReason4Choice, False)

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = base_types.UninitialisedField(self, 'StsRsn', StatusReason4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlStsRsnInf', type=Max105Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FincdAmt', type=FinancingRateOrAmountChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgReqSts', type=RequestStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=StatusReason4Choice, min=0, max=1, mutex_group=None, array=False),
	))