from . import base_types
import PaymentContext30
import CardPaymentServiceType15Code
import CardPaymentServiceType12Code
import Max35Text
import ActiveCurrencyCode
import CardPaymentEnvironment81
import Min3Max4Text
import CardPaymentServiceType9Code

class CommonData14(base_types._BaseFieldType):

	__slots__ = ["_SvcAttr", "_Ccy", "_TxTp", "_AddtlSvc", "_Envt", "_MrchntCtgyCd", "_RcncltnId", "_Cntxt"]
	@property
	def SvcAttr(self):
		return self._SvcAttr

	@SvcAttr.setter
	def SvcAttr(self, value):
		self._SvcAttr = value if type(value) != auto else self.make_default("SvcAttr")

	@SvcAttr.deleter
	def SvcAttr(self):
		del self._SvcAttr
		self._SvcAttr = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	@property
	def AddtlSvc(self):
		return self._AddtlSvc

	@AddtlSvc.setter
	def AddtlSvc(self, value):
		self._AddtlSvc = value if type(value) != auto else self.make_default("AddtlSvc")

	@AddtlSvc.deleter
	def AddtlSvc(self):
		del self._AddtlSvc
		self._AddtlSvc = None

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
	def MrchntCtgyCd(self):
		return self._MrchntCtgyCd

	@MrchntCtgyCd.setter
	def MrchntCtgyCd(self, value):
		self._MrchntCtgyCd = value if type(value) != auto else self.make_default("MrchntCtgyCd")

	@MrchntCtgyCd.deleter
	def MrchntCtgyCd(self):
		del self._MrchntCtgyCd
		self._MrchntCtgyCd = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcAttr', type=CardPaymentServiceType15Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=CardPaymentServiceType12Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlSvc', type=CardPaymentServiceType9Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrchntCtgyCd', type=Min3Max4Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=0, max=1, mutex_group=None, array=False),
	))

