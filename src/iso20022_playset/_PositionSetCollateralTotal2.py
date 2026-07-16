# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max20PositiveNumber
from . import PostedMarginOrCollateral6
from . import ReceivedMarginOrCollateral6

class PositionSetCollateralTotal2(base_types._BaseFieldType):

	__slots__ = ["_NbOfRpts", "_PstdMrgnOrColl", "_RcvdMrgnOrColl"]
	@property
	def NbOfRpts(self):
		return self._NbOfRpts

	@NbOfRpts.setter
	def NbOfRpts(self, value):
		self._NbOfRpts = value if value is not None else base_types.UninitialisedField(self, 'NbOfRpts', Max20PositiveNumber, False)

	@NbOfRpts.deleter
	def NbOfRpts(self):
		del self._NbOfRpts
		self._NbOfRpts = base_types.UninitialisedField(self, 'NbOfRpts', Max20PositiveNumber, False)

	@property
	def PstdMrgnOrColl(self):
		return self._PstdMrgnOrColl

	@PstdMrgnOrColl.setter
	def PstdMrgnOrColl(self, value):
		self._PstdMrgnOrColl = value if value is not None else base_types.UninitialisedField(self, 'PstdMrgnOrColl', PostedMarginOrCollateral6, False)

	@PstdMrgnOrColl.deleter
	def PstdMrgnOrColl(self):
		del self._PstdMrgnOrColl
		self._PstdMrgnOrColl = base_types.UninitialisedField(self, 'PstdMrgnOrColl', PostedMarginOrCollateral6, False)

	@property
	def RcvdMrgnOrColl(self):
		return self._RcvdMrgnOrColl

	@RcvdMrgnOrColl.setter
	def RcvdMrgnOrColl(self, value):
		self._RcvdMrgnOrColl = value if value is not None else base_types.UninitialisedField(self, 'RcvdMrgnOrColl', ReceivedMarginOrCollateral6, False)

	@RcvdMrgnOrColl.deleter
	def RcvdMrgnOrColl(self):
		del self._RcvdMrgnOrColl
		self._RcvdMrgnOrColl = base_types.UninitialisedField(self, 'RcvdMrgnOrColl', ReceivedMarginOrCollateral6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfRpts', type=Max20PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstdMrgnOrColl', type=PostedMarginOrCollateral6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvdMrgnOrColl', type=ReceivedMarginOrCollateral6, min=0, max=1, mutex_group=None, array=False),
	))