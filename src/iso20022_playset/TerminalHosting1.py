import base_types
import Max35Text
import TransactionEnvironment3Code

class TerminalHosting1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Ctgy"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if type(value) != auto else self.make_default("Ctgy")

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctgy', type=TransactionEnvironment3Code, min=0, max=1, mutex_group=None, array=False),
	))

