from . import base_types
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._ExternalPaymentTransactionStatus1Code import ExternalPaymentTransactionStatus1Code
from ._PaymentRejectReturnReason1 import PaymentRejectReturnReason1
from ._PaymentStatusReason1 import PaymentStatusReason1

class TrackerStatus1(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_RjctRtrRsn", "_Sts", "_StsRsn"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def RjctRtrRsn(self):
		return self._RjctRtrRsn

	@RjctRtrRsn.setter
	def RjctRtrRsn(self, value):
		self._RjctRtrRsn = value if type(value) != base_types.auto else self.make_default("RjctRtrRsn")

	@RjctRtrRsn.deleter
	def RjctRtrRsn(self):
		del self._RjctRtrRsn
		self._RjctRtrRsn = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != base_types.auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctRtrRsn', type=PaymentRejectReturnReason1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=ExternalPaymentTransactionStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsn', type=PaymentStatusReason1, min=0, max=None, mutex_group=None, array=True),
	))

