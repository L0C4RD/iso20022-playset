# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentificationAndAccount227
from . import SettlementObligation9

class Report7(base_types._BaseFieldType):

	__slots__ = ["_NonClrMmb", "_SttlmOblgtnDtls"]
	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if value is not None else base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount227, True)

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = base_types.UninitialisedField(self, 'NonClrMmb', PartyIdentificationAndAccount227, True)

	@property
	def SttlmOblgtnDtls(self):
		return self._SttlmOblgtnDtls

	@SttlmOblgtnDtls.setter
	def SttlmOblgtnDtls(self, value):
		self._SttlmOblgtnDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmOblgtnDtls', SettlementObligation9, True)

	@SttlmOblgtnDtls.deleter
	def SttlmOblgtnDtls(self):
		del self._SttlmOblgtnDtls
		self._SttlmOblgtnDtls = base_types.UninitialisedField(self, 'SttlmOblgtnDtls', SettlementObligation9, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount227, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmOblgtnDtls', type=SettlementObligation9, min=1, max=None, mutex_group=None, array=True),
	))