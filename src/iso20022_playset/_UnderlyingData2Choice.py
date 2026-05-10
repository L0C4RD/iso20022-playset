from . import base_types
from ._UnderlyingPaymentInstruction8 import UnderlyingPaymentInstruction8
from ._GenericIdentification1 import GenericIdentification1
from ._CashAccount40 import CashAccount40
from ._UnderlyingPaymentTransaction7 import UnderlyingPaymentTransaction7
from ._UnderlyingStatementEntry5 import UnderlyingStatementEntry5

class UnderlyingData2Choice(base_types._BaseFieldType):

	__slots__ = ["_Initn", "_StmtNtry", "_Othr", "_IntrBk", "_Acct"]
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
	def StmtNtry(self):
		return self._StmtNtry

	@StmtNtry.setter
	def StmtNtry(self, value):
		self._StmtNtry = value if type(value) != base_types.auto else self.make_default("StmtNtry")

	@StmtNtry.deleter
	def StmtNtry(self):
		del self._StmtNtry
		self._StmtNtry = None

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
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != base_types.auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Initn', type=UnderlyingPaymentInstruction8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='StmtNtry', type=UnderlyingStatementEntry5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntrBk', type=UnderlyingPaymentTransaction7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Acct', type=CashAccount40, min=0, max=1, mutex_group=1, array=False),
	))

