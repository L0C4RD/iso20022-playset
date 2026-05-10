from . import base_types
from .Max35Text import Max35Text
from .CollateralValueSearchCriteria4 import CollateralValueSearchCriteria4
from .CollateralValueReturnCriteria1 import CollateralValueReturnCriteria1

class CollateralValueCriteria4(base_types._BaseFieldType):

	__slots__ = ["_RtrCrit", "_QryNm", "_SchCrit"]
	@property
	def RtrCrit(self):
		return self._RtrCrit

	@RtrCrit.setter
	def RtrCrit(self, value):
		self._RtrCrit = value if type(value) != auto else self.make_default("RtrCrit")

	@RtrCrit.deleter
	def RtrCrit(self):
		del self._RtrCrit
		self._RtrCrit = None

	@property
	def QryNm(self):
		return self._QryNm

	@QryNm.setter
	def QryNm(self, value):
		self._QryNm = value if type(value) != auto else self.make_default("QryNm")

	@QryNm.deleter
	def QryNm(self):
		del self._QryNm
		self._QryNm = None

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if type(value) != auto else self.make_default("SchCrit")

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RtrCrit', type=CollateralValueReturnCriteria1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=CollateralValueSearchCriteria4, min=0, max=1, mutex_group=None, array=False),
	))

