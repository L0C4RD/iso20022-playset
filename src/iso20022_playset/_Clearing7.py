from . import base_types
from ._PartyIdentification253Choice import PartyIdentification253Choice
from ._NonGuaranteedTrade4 import NonGuaranteedTrade4
from ._YesNoIndicator import YesNoIndicator
from ._NettingEligible1Code import NettingEligible1Code

class Clearing7(base_types._BaseFieldType):

	__slots__ = ["_NonGrntedTrad", "_ClrSgmt", "_SttlmNetgElgblCd", "_GrntedTrad"]
	@property
	def NonGrntedTrad(self):
		return self._NonGrntedTrad

	@NonGrntedTrad.setter
	def NonGrntedTrad(self, value):
		self._NonGrntedTrad = value if type(value) != base_types.auto else self.make_default("NonGrntedTrad")

	@NonGrntedTrad.deleter
	def NonGrntedTrad(self):
		del self._NonGrntedTrad
		self._NonGrntedTrad = None

	@property
	def ClrSgmt(self):
		return self._ClrSgmt

	@ClrSgmt.setter
	def ClrSgmt(self, value):
		self._ClrSgmt = value if type(value) != base_types.auto else self.make_default("ClrSgmt")

	@ClrSgmt.deleter
	def ClrSgmt(self):
		del self._ClrSgmt
		self._ClrSgmt = None

	@property
	def SttlmNetgElgblCd(self):
		return self._SttlmNetgElgblCd

	@SttlmNetgElgblCd.setter
	def SttlmNetgElgblCd(self, value):
		self._SttlmNetgElgblCd = value if type(value) != base_types.auto else self.make_default("SttlmNetgElgblCd")

	@SttlmNetgElgblCd.deleter
	def SttlmNetgElgblCd(self):
		del self._SttlmNetgElgblCd
		self._SttlmNetgElgblCd = None

	@property
	def GrntedTrad(self):
		return self._GrntedTrad

	@GrntedTrad.setter
	def GrntedTrad(self, value):
		self._GrntedTrad = value if type(value) != base_types.auto else self.make_default("GrntedTrad")

	@GrntedTrad.deleter
	def GrntedTrad(self):
		del self._GrntedTrad
		self._GrntedTrad = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonGrntedTrad', type=NonGuaranteedTrade4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSgmt', type=PartyIdentification253Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmNetgElgblCd', type=NettingEligible1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedTrad', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

