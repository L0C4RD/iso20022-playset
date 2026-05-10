from . import base_types
from ._Number import Number
from ._Max9NumericText import Max9NumericText
from ._TimeUnit1Code import TimeUnit1Code

class ProcessRetry3(base_types._BaseFieldType):

	__slots__ = ["_MaxNb", "_UnitOfTm", "_Dely"]
	@property
	def Dely(self):
		return self._Dely

	@Dely.setter
	def Dely(self, value):
		self._Dely = value if type(value) != base_types.auto else self.make_default("Dely")

	@Dely.deleter
	def Dely(self):
		del self._Dely
		self._Dely = None

	@property
	def MaxNb(self):
		return self._MaxNb

	@MaxNb.setter
	def MaxNb(self, value):
		self._MaxNb = value if type(value) != base_types.auto else self.make_default("MaxNb")

	@MaxNb.deleter
	def MaxNb(self):
		del self._MaxNb
		self._MaxNb = None

	@property
	def UnitOfTm(self):
		return self._UnitOfTm

	@UnitOfTm.setter
	def UnitOfTm(self, value):
		self._UnitOfTm = value if type(value) != base_types.auto else self.make_default("UnitOfTm")

	@UnitOfTm.deleter
	def UnitOfTm(self):
		del self._UnitOfTm
		self._UnitOfTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dely', type=Max9NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxNb', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfTm', type=TimeUnit1Code, min=0, max=1, mutex_group=None, array=False),
	))

