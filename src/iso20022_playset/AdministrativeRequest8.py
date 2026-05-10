import base_types
import PaymentContext30
import CardPaymentEnvironment81
import Max20000Text
import SupplementaryData1

class AdministrativeRequest8(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_Cntxt", "_SplmtryData", "_AdmstvSvcId"]
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
	def AdmstvSvcId(self):
		return self._AdmstvSvcId

	@AdmstvSvcId.setter
	def AdmstvSvcId(self, value):
		self._AdmstvSvcId = value if type(value) != auto else self.make_default("AdmstvSvcId")

	@AdmstvSvcId.deleter
	def AdmstvSvcId(self):
		del self._AdmstvSvcId
		self._AdmstvSvcId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AdmstvSvcId', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
	))

