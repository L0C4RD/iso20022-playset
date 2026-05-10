from . import base_types
from .GenericIdentification47 import GenericIdentification47
from .CorporateActionEventType1Code import CorporateActionEventType1Code

class CorporateAction1Choice(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Prtry"]
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
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=CorporateActionEventType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=GenericIdentification47, min=0, max=1, mutex_group=1, array=False),
	))

