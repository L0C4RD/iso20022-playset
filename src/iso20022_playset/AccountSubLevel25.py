import base_types
import PartyIdentification276
import ShareholdingBalance1
import Max35Text

class AccountSubLevel25(base_types._BaseFieldType):

	__slots__ = ["_AcctHldr", "_ShrhldgBal", "_SfkpgAcct"]
	@property
	def AcctHldr(self):
		return self._AcctHldr

	@AcctHldr.setter
	def AcctHldr(self, value):
		self._AcctHldr = value if type(value) != auto else self.make_default("AcctHldr")

	@AcctHldr.deleter
	def AcctHldr(self):
		del self._AcctHldr
		self._AcctHldr = None

	@property
	def ShrhldgBal(self):
		return self._ShrhldgBal

	@ShrhldgBal.setter
	def ShrhldgBal(self, value):
		self._ShrhldgBal = value if type(value) != auto else self.make_default("ShrhldgBal")

	@ShrhldgBal.deleter
	def ShrhldgBal(self):
		del self._ShrhldgBal
		self._ShrhldgBal = None

	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctHldr', type=PartyIdentification276, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrhldgBal', type=ShareholdingBalance1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

