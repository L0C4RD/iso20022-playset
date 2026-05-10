import base_types
import NetworkType2Code
import NetworkParameters7

class NetworkParameters8(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Accs"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Accs(self):
		return self._Accs

	@Accs.setter
	def Accs(self, value):
		self._Accs = value if type(value) != auto else self.make_default("Accs")

	@Accs.deleter
	def Accs(self):
		del self._Accs
		self._Accs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=NetworkType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Accs', type=NetworkParameters7, min=1, max=1, mutex_group=None, array=False),
	))

