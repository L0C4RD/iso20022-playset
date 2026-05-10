import base_types
import CardPaymentEnvironment81
import PaymentContext30
import LoginRequest7
import SupplementaryData1
import RetailerService4Code
import LogoutRequest1
import DiagnosisRequest1

class SessionManagementRequest8(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_Cntxt", "_DgnssReq", "_SplmtryData", "_SvcCntt", "_LgtReq", "_LgnReq"]
	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if type(value) != auto else self.make_default("Cntxt")

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = None

	@property
	def DgnssReq(self):
		return self._DgnssReq

	@DgnssReq.setter
	def DgnssReq(self, value):
		self._DgnssReq = value if type(value) != auto else self.make_default("DgnssReq")

	@DgnssReq.deleter
	def DgnssReq(self):
		del self._DgnssReq
		self._DgnssReq = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def SvcCntt(self):
		return self._SvcCntt

	@SvcCntt.setter
	def SvcCntt(self, value):
		self._SvcCntt = value if type(value) != auto else self.make_default("SvcCntt")

	@SvcCntt.deleter
	def SvcCntt(self):
		del self._SvcCntt
		self._SvcCntt = None

	@property
	def LgtReq(self):
		return self._LgtReq

	@LgtReq.setter
	def LgtReq(self, value):
		self._LgtReq = value if type(value) != auto else self.make_default("LgtReq")

	@LgtReq.deleter
	def LgtReq(self):
		del self._LgtReq
		self._LgtReq = None

	@property
	def LgnReq(self):
		return self._LgnReq

	@LgnReq.setter
	def LgnReq(self, value):
		self._LgnReq = value if type(value) != auto else self.make_default("LgnReq")

	@LgnReq.deleter
	def LgnReq(self):
		del self._LgnReq
		self._LgnReq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgnssReq', type=DiagnosisRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcCntt', type=RetailerService4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LgtReq', type=LogoutRequest1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LgnReq', type=LoginRequest7, min=0, max=1, mutex_group=None, array=False),
	))

