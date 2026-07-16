# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ProcessingStatus99Choice
from . import ProprietaryReason4
from . import SettlementStatus34Choice

class IntraPositionStatusAndReason4(base_types._BaseFieldType):

	__slots__ = ["_PrcgSts", "_Sttld", "_SttlmSts"]
	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if value is not None else base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus99Choice, True)

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = base_types.UninitialisedField(self, 'PrcgSts', ProcessingStatus99Choice, True)

	@property
	def Sttld(self):
		return self._Sttld

	@Sttld.setter
	def Sttld(self, value):
		self._Sttld = value if value is not None else base_types.UninitialisedField(self, 'Sttld', ProprietaryReason4, False)

	@Sttld.deleter
	def Sttld(self):
		del self._Sttld
		self._Sttld = base_types.UninitialisedField(self, 'Sttld', ProprietaryReason4, False)

	@property
	def SttlmSts(self):
		return self._SttlmSts

	@SttlmSts.setter
	def SttlmSts(self, value):
		self._SttlmSts = value if value is not None else base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus34Choice, True)

	@SttlmSts.deleter
	def SttlmSts(self):
		del self._SttlmSts
		self._SttlmSts = base_types.UninitialisedField(self, 'SttlmSts', SettlementStatus34Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus99Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sttld', type=ProprietaryReason4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmSts', type=SettlementStatus34Choice, min=0, max=None, mutex_group=None, array=True),
	))