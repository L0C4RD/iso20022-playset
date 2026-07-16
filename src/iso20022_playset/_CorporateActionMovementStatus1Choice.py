# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionMovementFailedStatus1
from . import CorporateActionMovementProcessingStatus1
from . import CorporateActionMovementRejectionStatus1

class CorporateActionMovementStatus1Choice(base_types._BaseFieldType):

	__slots__ = ["_FaildSts", "_PrcdSts", "_RjctdSts"]
	@property
	def FaildSts(self):
		return self._FaildSts

	@FaildSts.setter
	def FaildSts(self, value):
		self._FaildSts = value if value is not None else base_types.UninitialisedField(self, 'FaildSts', CorporateActionMovementFailedStatus1, False)

	@FaildSts.deleter
	def FaildSts(self):
		del self._FaildSts
		self._FaildSts = base_types.UninitialisedField(self, 'FaildSts', CorporateActionMovementFailedStatus1, False)

	@property
	def PrcdSts(self):
		return self._PrcdSts

	@PrcdSts.setter
	def PrcdSts(self, value):
		self._PrcdSts = value if value is not None else base_types.UninitialisedField(self, 'PrcdSts', CorporateActionMovementProcessingStatus1, False)

	@PrcdSts.deleter
	def PrcdSts(self):
		del self._PrcdSts
		self._PrcdSts = base_types.UninitialisedField(self, 'PrcdSts', CorporateActionMovementProcessingStatus1, False)

	@property
	def RjctdSts(self):
		return self._RjctdSts

	@RjctdSts.setter
	def RjctdSts(self, value):
		self._RjctdSts = value if value is not None else base_types.UninitialisedField(self, 'RjctdSts', CorporateActionMovementRejectionStatus1, False)

	@RjctdSts.deleter
	def RjctdSts(self):
		del self._RjctdSts
		self._RjctdSts = base_types.UninitialisedField(self, 'RjctdSts', CorporateActionMovementRejectionStatus1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FaildSts', type=CorporateActionMovementFailedStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrcdSts', type=CorporateActionMovementProcessingStatus1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RjctdSts', type=CorporateActionMovementRejectionStatus1, min=0, max=1, mutex_group=1, array=False),
	))