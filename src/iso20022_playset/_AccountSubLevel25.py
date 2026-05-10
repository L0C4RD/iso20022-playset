from . import base_types
from .Max35Text import Max35Text
from .ShareholdingBalance1 import ShareholdingBalance1
from .PartyIdentification276 import PartyIdentification276

class AccountSubLevel25(base_types._BaseFieldType):

	__slots__ = ["_SfkpgAcct", "_ShrhldgBal", "_AcctHldr"]
	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def ShrhldgBal(self):
		return self._ShrhldgBal

	@ShrhldgBal.setter
	def ShrhldgBal(self, value):
		self._ShrhldgBal = value if type(value) != base_types.auto else self.make_default("ShrhldgBal")

	@ShrhldgBal.deleter
	def ShrhldgBal(self):
		del self._ShrhldgBal
		self._ShrhldgBal = None

	@property
	def AcctHldr(self):
		return self._AcctHldr

	@AcctHldr.setter
	def AcctHldr(self, value):
		self._AcctHldr = value if type(value) != base_types.auto else self.make_default("AcctHldr")

	@AcctHldr.deleter
	def AcctHldr(self):
		del self._AcctHldr
		self._AcctHldr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SfkpgAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldgBal', type=ShareholdingBalance1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcctHldr', type=PartyIdentification276, min=1, max=1, mutex_group=None, array=False),
	))

