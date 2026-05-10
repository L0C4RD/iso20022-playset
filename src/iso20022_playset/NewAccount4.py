from . import base_types
import IndividualPerson44
import CashAccount43
import Organisation43

class NewAccount4(base_types._BaseFieldType):

	__slots__ = ["_AcctPty", "_Acct", "_Org"]
	@property
	def AcctPty(self):
		return self._AcctPty

	@AcctPty.setter
	def AcctPty(self, value):
		self._AcctPty = value if type(value) != auto else self.make_default("AcctPty")

	@AcctPty.deleter
	def AcctPty(self):
		del self._AcctPty
		self._AcctPty = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def Org(self):
		return self._Org

	@Org.setter
	def Org(self, value):
		self._Org = value if type(value) != auto else self.make_default("Org")

	@Org.deleter
	def Org(self):
		del self._Org
		self._Org = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctPty', type=IndividualPerson44, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Acct', type=CashAccount43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Org', type=Organisation43, min=0, max=1, mutex_group=None, array=False),
	))

