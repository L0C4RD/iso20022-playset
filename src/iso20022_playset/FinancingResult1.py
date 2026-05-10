from . import base_types
from .StatusReason4Choice import StatusReason4Choice
from .Max105Text import Max105Text
from .RequestStatus1Code import RequestStatus1Code
from .FinancingRateOrAmountChoice import FinancingRateOrAmountChoice

class FinancingResult1(base_types._BaseFieldType):

	__slots__ = ["_StsRsn", "_FincgReqSts", "_FincdAmt", "_AddtlStsRsnInf"]
	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	@property
	def FincgReqSts(self):
		return self._FincgReqSts

	@FincgReqSts.setter
	def FincgReqSts(self, value):
		self._FincgReqSts = value if type(value) != auto else self.make_default("FincgReqSts")

	@FincgReqSts.deleter
	def FincgReqSts(self):
		del self._FincgReqSts
		self._FincgReqSts = None

	@property
	def FincdAmt(self):
		return self._FincdAmt

	@FincdAmt.setter
	def FincdAmt(self, value):
		self._FincdAmt = value if type(value) != auto else self.make_default("FincdAmt")

	@FincdAmt.deleter
	def FincdAmt(self):
		del self._FincdAmt
		self._FincdAmt = None

	@property
	def AddtlStsRsnInf(self):
		return self._AddtlStsRsnInf

	@AddtlStsRsnInf.setter
	def AddtlStsRsnInf(self, value):
		self._AddtlStsRsnInf = value if type(value) != auto else self.make_default("AddtlStsRsnInf")

	@AddtlStsRsnInf.deleter
	def AddtlStsRsnInf(self):
		del self._AddtlStsRsnInf
		self._AddtlStsRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsRsn', type=StatusReason4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgReqSts', type=RequestStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincdAmt', type=FinancingRateOrAmountChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlStsRsnInf', type=Max105Text, min=0, max=None, mutex_group=None, array=True),
	))

