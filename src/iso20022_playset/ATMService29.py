from . import base_types
import ATMTransactionAmounts6
import ATMServiceType13Code
import ATMService18

class ATMService29(base_types._BaseFieldType):

	__slots__ = ["_SvcVarnt", "_Lmts", "_SvcTp"]
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
	def SvcTp(self):
		return self._SvcTp

	@SvcTp.setter
	def SvcTp(self, value):
		self._SvcTp = value if type(value) != auto else self.make_default("SvcTp")

	@SvcTp.deleter
	def SvcTp(self):
		del self._SvcTp
		self._SvcTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvcVarnt', type=ATMService18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Lmts', type=ATMTransactionAmounts6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcTp', type=ATMServiceType13Code, min=1, max=1, mutex_group=None, array=False),
	))

