# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LEIIdentifier
from . import TrueFalseIndicator

class SecuritiesTransactionTransmission2(base_types._BaseFieldType):

	__slots__ = ["_TrnsmssnInd", "_TrnsmttgBuyr", "_TrnsmttgSellr"]
	@property
	def TrnsmssnInd(self):
		return self._TrnsmssnInd

	@TrnsmssnInd.setter
	def TrnsmssnInd(self, value):
		self._TrnsmssnInd = value if value is not None else base_types.UninitialisedField(self, 'TrnsmssnInd', TrueFalseIndicator, False)

	@TrnsmssnInd.deleter
	def TrnsmssnInd(self):
		del self._TrnsmssnInd
		self._TrnsmssnInd = base_types.UninitialisedField(self, 'TrnsmssnInd', TrueFalseIndicator, False)

	@property
	def TrnsmttgBuyr(self):
		return self._TrnsmttgBuyr

	@TrnsmttgBuyr.setter
	def TrnsmttgBuyr(self, value):
		self._TrnsmttgBuyr = value if value is not None else base_types.UninitialisedField(self, 'TrnsmttgBuyr', LEIIdentifier, False)

	@TrnsmttgBuyr.deleter
	def TrnsmttgBuyr(self):
		del self._TrnsmttgBuyr
		self._TrnsmttgBuyr = base_types.UninitialisedField(self, 'TrnsmttgBuyr', LEIIdentifier, False)

	@property
	def TrnsmttgSellr(self):
		return self._TrnsmttgSellr

	@TrnsmttgSellr.setter
	def TrnsmttgSellr(self, value):
		self._TrnsmttgSellr = value if value is not None else base_types.UninitialisedField(self, 'TrnsmttgSellr', LEIIdentifier, False)

	@TrnsmttgSellr.deleter
	def TrnsmttgSellr(self):
		del self._TrnsmttgSellr
		self._TrnsmttgSellr = base_types.UninitialisedField(self, 'TrnsmttgSellr', LEIIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrnsmssnInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmttgBuyr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmttgSellr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))