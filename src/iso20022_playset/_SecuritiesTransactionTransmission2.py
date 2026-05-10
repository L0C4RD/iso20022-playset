from . import base_types
from ._TrueFalseIndicator import TrueFalseIndicator
from ._LEIIdentifier import LEIIdentifier

class SecuritiesTransactionTransmission2(base_types._BaseFieldType):

	__slots__ = ["_TrnsmssnInd", "_TrnsmttgSellr", "_TrnsmttgBuyr"]
	@property
	def TrnsmssnInd(self):
		return self._TrnsmssnInd

	@TrnsmssnInd.setter
	def TrnsmssnInd(self, value):
		self._TrnsmssnInd = value if type(value) != base_types.auto else self.make_default("TrnsmssnInd")

	@TrnsmssnInd.deleter
	def TrnsmssnInd(self):
		del self._TrnsmssnInd
		self._TrnsmssnInd = None

	@property
	def TrnsmttgBuyr(self):
		return self._TrnsmttgBuyr

	@TrnsmttgBuyr.setter
	def TrnsmttgBuyr(self, value):
		self._TrnsmttgBuyr = value if type(value) != base_types.auto else self.make_default("TrnsmttgBuyr")

	@TrnsmttgBuyr.deleter
	def TrnsmttgBuyr(self):
		del self._TrnsmttgBuyr
		self._TrnsmttgBuyr = None

	@property
	def TrnsmttgSellr(self):
		return self._TrnsmttgSellr

	@TrnsmttgSellr.setter
	def TrnsmttgSellr(self, value):
		self._TrnsmttgSellr = value if type(value) != base_types.auto else self.make_default("TrnsmttgSellr")

	@TrnsmttgSellr.deleter
	def TrnsmttgSellr(self):
		del self._TrnsmttgSellr
		self._TrnsmttgSellr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrnsmssnInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmttgBuyr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrnsmttgSellr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))

