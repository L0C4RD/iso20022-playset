from . import base_types
from .DateAndDateTime2Choice import DateAndDateTime2Choice
from .PaymentStatusCode6Choice import PaymentStatusCode6Choice
from .PaymentStatusReason1Choice import PaymentStatusReason1Choice

class PaymentStatus6(base_types._BaseFieldType):

	__slots__ = ["_Rsn", "_Cd", "_DtTm"]
	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != base_types.auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != base_types.auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rsn', type=PaymentStatusReason1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cd', type=PaymentStatusCode6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))

