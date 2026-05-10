from . import base_types
from ._FundParameters5 import FundParameters5
from ._NoCriteria1Code import NoCriteria1Code

class FundParameters4Choice(base_types._BaseFieldType):

	__slots__ = ["_NoCrit", "_Params"]
	@property
	def NoCrit(self):
		return self._NoCrit

	@NoCrit.setter
	def NoCrit(self, value):
		self._NoCrit = value if type(value) != base_types.auto else self.make_default("NoCrit")

	@NoCrit.deleter
	def NoCrit(self):
		del self._NoCrit
		self._NoCrit = None

	@property
	def Params(self):
		return self._Params

	@Params.setter
	def Params(self, value):
		self._Params = value if type(value) != base_types.auto else self.make_default("Params")

	@Params.deleter
	def Params(self):
		del self._Params
		self._Params = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NoCrit', type=NoCriteria1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Params', type=FundParameters5, min=0, max=1, mutex_group=1, array=False),
	))

