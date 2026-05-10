from . import base_types
from .RestrictedFINXMax16Text import RestrictedFINXMax16Text
from .CorporateActionMovementPreliminaryAdviceFunction1Code import CorporateActionMovementPreliminaryAdviceFunction1Code
from .CorporateActionPreliminaryAdviceType1Code import CorporateActionPreliminaryAdviceType1Code

class CorporateActionPreliminaryAdviceType5(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_MvmntPrlimryAdvcId", "_Fctn"]
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
	def MvmntPrlimryAdvcId(self):
		return self._MvmntPrlimryAdvcId

	@MvmntPrlimryAdvcId.setter
	def MvmntPrlimryAdvcId(self, value):
		self._MvmntPrlimryAdvcId = value if type(value) != base_types.auto else self.make_default("MvmntPrlimryAdvcId")

	@MvmntPrlimryAdvcId.deleter
	def MvmntPrlimryAdvcId(self):
		del self._MvmntPrlimryAdvcId
		self._MvmntPrlimryAdvcId = None

	@property
	def Fctn(self):
		return self._Fctn

	@Fctn.setter
	def Fctn(self, value):
		self._Fctn = value if type(value) != base_types.auto else self.make_default("Fctn")

	@Fctn.deleter
	def Fctn(self):
		del self._Fctn
		self._Fctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=CorporateActionPreliminaryAdviceType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntPrlimryAdvcId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fctn', type=CorporateActionMovementPreliminaryAdviceFunction1Code, min=1, max=1, mutex_group=None, array=False),
	))

