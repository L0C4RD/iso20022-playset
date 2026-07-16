# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ProcessingStatus66Choice
from . import SettlementStatus16Choice

class PendingStatusAndReason2(base_types._BaseFieldType):

	__slots__ = ["_PrcgSts", "_SttlmSts"]
	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus66Choice, True)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus66Choice, True)

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus16Choice, True)

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus16Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus66Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus16Choice, min=0, max=None, mutex_group=None, array=True),
	))