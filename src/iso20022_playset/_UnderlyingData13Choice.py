from . import base_types
from ._CashAccount40 import CashAccount40
from ._GenericIdentification1 import GenericIdentification1
from ._UnderlyingPaymentInstruction11 import UnderlyingPaymentInstruction11
from ._UnderlyingPaymentTransaction11 import UnderlyingPaymentTransaction11
from ._UnderlyingStatementEntry11 import UnderlyingStatementEntry11

class UnderlyingData13Choice(base_types._BaseFieldType):

	__slots__ = ["_Acct", "_Initn", "_IntrBk", "_Othr", "_StmtNtry"]
	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

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
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

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
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Initn', type=UnderlyingPaymentInstruction11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrBk', type=UnderlyingPaymentTransaction11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtNtry', type=UnderlyingStatementEntry11, min=0, max=1, mutex_group=1, array=False),
	))

