# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Cleared23Choice
from . import ClearingObligationType1Code
from . import TrueFalseIndicator

class TradeClearing11(base_types._BaseFieldType):

	__slots__ = ["_ClrOblgtn", "_ClrSts", "_IntraGrp"]
	@property
	def ClrOblgtn(self):
		return self._ClrOblgtn

	@ClrOblgtn.setter
	def ClrOblgtn(self, value):
		self._ClrOblgtn = value if value is not None else base_types.UninitialisedField(self, 'ClrOblgtn', ClearingObligationType1Code, False)

	@ClrOblgtn.deleter
	def ClrOblgtn(self):
		del self._ClrOblgtn
		self._ClrOblgtn = base_types.UninitialisedField(self, 'ClrOblgtn', ClearingObligationType1Code, False)

	@property
	def ClrSts(self):
		return self._ClrSts

	@ClrSts.setter
	def ClrSts(self, value):
		self._ClrSts = value if value is not None else base_types.UninitialisedField(self, 'ClrSts', Cleared23Choice, False)

	@ClrSts.deleter
	def ClrSts(self):
		del self._ClrSts
		self._ClrSts = base_types.UninitialisedField(self, 'ClrSts', Cleared23Choice, False)

	@property
	def IntraGrp(self):
		return self._IntraGrp

	@IntraGrp.setter
	def IntraGrp(self, value):
		self._IntraGrp = value if value is not None else base_types.UninitialisedField(self, 'IntraGrp', TrueFalseIndicator, False)

	@IntraGrp.deleter
	def IntraGrp(self):
		del self._IntraGrp
		self._IntraGrp = base_types.UninitialisedField(self, 'IntraGrp', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrOblgtn', type=ClearingObligationType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSts', type=Cleared23Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntraGrp', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))