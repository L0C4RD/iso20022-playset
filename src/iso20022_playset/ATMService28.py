from . import base_types
from .ATMTransaction8 import ATMTransaction8
from .ATMService18 import ATMService18
from .ATMServiceType13Code import ATMServiceType13Code
from .ATMTransactionAmounts6 import ATMTransactionAmounts6

class ATMService28(base_types._BaseFieldType):

	__slots__ = ["_SvcTp", "_Lmts", "_PrefrdWdrwl", "_SvcVarnt"]
	@property
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if type(value) != auto else self.make_default("SvcTp")

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = None

	@property
	def Lmts(self):
		return self._Lmts

	@Lmts.setter
	def Lmts(self, value):
		self._Lmts = value if type(value) != auto else self.make_default("Lmts")

	@Lmts.deleter
	def Lmts(self):
		del self._Lmts
		self._Lmts = None

	@property
	def PrefrdWdrwl(self):
		return self._PrefrdWdrwl

	@PrefrdWdrwl.setter
	def PrefrdWdrwl(self, value):
		self._PrefrdWdrwl = value if type(value) != auto else self.make_default("PrefrdWdrwl")

	@PrefrdWdrwl.deleter
	def PrefrdWdrwl(self):
		del self._PrefrdWdrwl
		self._PrefrdWdrwl = None

	@property
	def SvcVarnt(self):
		return self._SvcVarnt

	@SvcVarnt.setter
	def SvcVarnt(self, value):
		self._SvcVarnt = value if type(value) != auto else self.make_default("SvcVarnt")

	@SvcVarnt.deleter
	def SvcVarnt(self):
		del self._SvcVarnt
		self._SvcVarnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcTp', type=ATMServiceType13Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lmts', type=ATMTransactionAmounts6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrefrdWdrwl', type=ATMTransaction8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcVarnt', type=ATMService18, min=0, max=None, mutex_group=None, array=True),
	))

