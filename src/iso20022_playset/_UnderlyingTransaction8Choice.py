from . import base_types
from ._UnderlyingStatementEntry3 import UnderlyingStatementEntry3
from ._UnderlyingPaymentTransaction8 import UnderlyingPaymentTransaction8
from ._UnderlyingPaymentInstruction9 import UnderlyingPaymentInstruction9

class UnderlyingTransaction8Choice(base_types._BaseFieldType):

	__slots__ = ["_Initn", "_IntrBk", "_StmtNtry"]
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
	def StmtNtry(self):
		return self._StmtNtry

	@StmtNtry.setter
	def StmtNtry(self, value):
		self._StmtNtry = value if type(value) != base_types.auto else self.make_default("StmtNtry")

	@StmtNtry.deleter
	def StmtNtry(self):
		del self._StmtNtry
		self._StmtNtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Initn', type=UnderlyingPaymentInstruction9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrBk', type=UnderlyingPaymentTransaction8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtNtry', type=UnderlyingStatementEntry3, min=0, max=1, mutex_group=1, array=False),
	))

