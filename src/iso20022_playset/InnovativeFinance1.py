import base_types
import Max350Text
import GenericIdentification36

class InnovativeFinance1(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Inf"]
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
	def Inf(self):
		return self._Inf

	@Inf.setter
	def Inf(self, value):
		self._Inf = value if type(value) != auto else self.make_default("Inf")

	@Inf.deleter
	def Inf(self):
		del self._Inf
		self._Inf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=GenericIdentification36, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Inf', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))

