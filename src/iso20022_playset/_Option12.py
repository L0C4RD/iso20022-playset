from . import base_types
from ._OptionType1Code import OptionType1Code
from ._OptionDateOrPeriod1Choice import OptionDateOrPeriod1Choice

class Option12(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_DtOrPrd"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def DtOrPrd(self):
		return self._DtOrPrd

	@DtOrPrd.setter
	def DtOrPrd(self, value):
		self._DtOrPrd = value if type(value) != base_types.auto else self.make_default("DtOrPrd")

	@DtOrPrd.deleter
	def DtOrPrd(self):
		del self._DtOrPrd
		self._DtOrPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=OptionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOrPrd', type=OptionDateOrPeriod1Choice, min=1, max=1, mutex_group=None, array=False),
	))

