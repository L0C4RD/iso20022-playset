from . import base_types
from .StandingOrderCriteria5 import StandingOrderCriteria5
from .Max35Text import Max35Text

class StandingOrderCriteria5Choice(base_types._BaseFieldType):

	__slots__ = ["_QryNm", "_NewCrit"]
	@property
	def QryNm(self):
		return self._QryNm

	@QryNm.setter
	def QryNm(self, value):
		self._QryNm = value if type(value) != base_types.auto else self.make_default("QryNm")

	@QryNm.deleter
	def QryNm(self):
		del self._QryNm
		self._QryNm = None

	@property
	def NewCrit(self):
		return self._NewCrit

	@NewCrit.setter
	def NewCrit(self, value):
		self._NewCrit = value if type(value) != base_types.auto else self.make_default("NewCrit")

	@NewCrit.deleter
	def NewCrit(self):
		del self._NewCrit
		self._NewCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryNm', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NewCrit', type=StandingOrderCriteria5, min=0, max=1, mutex_group=1, array=False),
	))

