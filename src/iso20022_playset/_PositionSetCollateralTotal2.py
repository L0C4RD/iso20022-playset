from . import base_types
from .Max20PositiveNumber import Max20PositiveNumber
from .ReceivedMarginOrCollateral6 import ReceivedMarginOrCollateral6
from .PostedMarginOrCollateral6 import PostedMarginOrCollateral6

class PositionSetCollateralTotal2(base_types._BaseFieldType):

	__slots__ = ["_RcvdMrgnOrColl", "_NbOfRpts", "_PstdMrgnOrColl"]
	@property
	def RcvdMrgnOrColl(self):
		return self._RcvdMrgnOrColl

	@RcvdMrgnOrColl.setter
	def RcvdMrgnOrColl(self, value):
		self._RcvdMrgnOrColl = value if type(value) != base_types.auto else self.make_default("RcvdMrgnOrColl")

	@RcvdMrgnOrColl.deleter
	def RcvdMrgnOrColl(self):
		del self._RcvdMrgnOrColl
		self._RcvdMrgnOrColl = None

	@property
	def NbOfRpts(self):
		return self._NbOfRpts

	@NbOfRpts.setter
	def NbOfRpts(self, value):
		self._NbOfRpts = value if type(value) != base_types.auto else self.make_default("NbOfRpts")

	@NbOfRpts.deleter
	def NbOfRpts(self):
		del self._NbOfRpts
		self._NbOfRpts = None

	@property
	def PstdMrgnOrColl(self):
		return self._PstdMrgnOrColl

	@PstdMrgnOrColl.setter
	def PstdMrgnOrColl(self, value):
		self._PstdMrgnOrColl = value if type(value) != base_types.auto else self.make_default("PstdMrgnOrColl")

	@PstdMrgnOrColl.deleter
	def PstdMrgnOrColl(self):
		del self._PstdMrgnOrColl
		self._PstdMrgnOrColl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcvdMrgnOrColl', type=ReceivedMarginOrCollateral6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfRpts', type=Max20PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstdMrgnOrColl', type=PostedMarginOrCollateral6, min=0, max=1, mutex_group=None, array=False),
	))

