from . import base_types
from ._StatusReasonInformation12 import StatusReasonInformation12
from ._TransactionStatus1Choice import TransactionStatus1Choice

class PaymentTransactionStatus1(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_StsRsnInf"]
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
	def StsRsnInf(self):
		return self._StsRsnInf

	@StsRsnInf.setter
	def StsRsnInf(self, value):
		self._StsRsnInf = value if type(value) != base_types.auto else self.make_default("StsRsnInf")

	@StsRsnInf.deleter
	def StsRsnInf(self):
		del self._StsRsnInf
		self._StsRsnInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=TransactionStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsnInf', type=StatusReasonInformation12, min=0, max=None, mutex_group=None, array=True),
	))

