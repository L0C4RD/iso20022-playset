from . import base_types
from .CorrectivePaymentInitiation5 import CorrectivePaymentInitiation5
from .CorrectiveInterbankTransaction3 import CorrectiveInterbankTransaction3

class CorrectiveTransaction5Choice(base_types._BaseFieldType):

	__slots__ = ["_IntrBk", "_Initn"]
	@property
	def IntrBk(self):
		return self._IntrBk

	@IntrBk.setter
	def IntrBk(self, value):
		self._IntrBk = value if type(value) != base_types.auto else self.make_default("IntrBk")

	@IntrBk.deleter
	def IntrBk(self):
		del self._IntrBk
		self._IntrBk = None

	@property
	def Initn(self):
		return self._Initn

	@Initn.setter
	def Initn(self, value):
		self._Initn = value if type(value) != base_types.auto else self.make_default("Initn")

	@Initn.deleter
	def Initn(self):
		del self._Initn
		self._Initn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrBk', type=CorrectiveInterbankTransaction3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Initn', type=CorrectivePaymentInitiation5, min=0, max=1, mutex_group=1, array=False),
	))

