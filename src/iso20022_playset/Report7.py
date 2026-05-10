from . import base_types
import SettlementObligation9
import PartyIdentificationAndAccount227

class Report7(base_types._BaseFieldType):

	__slots__ = ["_NonClrMmb", "_SttlmOblgtnDtls"]
	@property
	def NonClrMmb(self):
		return self._NonClrMmb

	@NonClrMmb.setter
	def NonClrMmb(self, value):
		self._NonClrMmb = value if type(value) != auto else self.make_default("NonClrMmb")

	@NonClrMmb.deleter
	def NonClrMmb(self):
		del self._NonClrMmb
		self._NonClrMmb = None

	@property
	def SttlmOblgtnDtls(self):
		return self._SttlmOblgtnDtls

	@SttlmOblgtnDtls.setter
	def SttlmOblgtnDtls(self, value):
		self._SttlmOblgtnDtls = value if type(value) != auto else self.make_default("SttlmOblgtnDtls")

	@SttlmOblgtnDtls.deleter
	def SttlmOblgtnDtls(self):
		del self._SttlmOblgtnDtls
		self._SttlmOblgtnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonClrMmb', type=PartyIdentificationAndAccount227, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmOblgtnDtls', type=SettlementObligation9, min=1, max=None, mutex_group=None, array=True),
	))

