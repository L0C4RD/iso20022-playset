from . import base_types
from .Max35Text import Max35Text
from .CorporateActionPreliminaryAdviceType1Code import CorporateActionPreliminaryAdviceType1Code
from .CorporateActionMovementPreliminaryAdviceFunction1Code import CorporateActionMovementPreliminaryAdviceFunction1Code

class CorporateActionPreliminaryAdviceType4(base_types._BaseFieldType):

	__slots__ = ["_Fctn", "_MvmntPrlimryAdvcId", "_Tp"]
	@property
	def Fctn(self):
		return self._Fctn

	@Fctn.setter
	def Fctn(self, value):
		self._Fctn = value if type(value) != auto else self.make_default("Fctn")

	@Fctn.deleter
	def Fctn(self):
		del self._Fctn
		self._Fctn = None

	@property
	def MvmntPrlimryAdvcId(self):
		return self._MvmntPrlimryAdvcId

	@MvmntPrlimryAdvcId.setter
	def MvmntPrlimryAdvcId(self, value):
		self._MvmntPrlimryAdvcId = value if type(value) != auto else self.make_default("MvmntPrlimryAdvcId")

	@MvmntPrlimryAdvcId.deleter
	def MvmntPrlimryAdvcId(self):
		del self._MvmntPrlimryAdvcId
		self._MvmntPrlimryAdvcId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fctn', type=CorporateActionMovementPreliminaryAdviceFunction1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntPrlimryAdvcId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CorporateActionPreliminaryAdviceType1Code, min=1, max=1, mutex_group=None, array=False),
	))

