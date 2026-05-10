from . import base_types
from .Max4AlphaNumericText import Max4AlphaNumericText
from .Modification1Code import Modification1Code
from .PartyAndCertificate7 import PartyAndCertificate7

class Group5(base_types._BaseFieldType):

	__slots__ = ["_GrpId", "_Pty", "_ModCd"]
	@property
	def GrpId(self):
		return self._GrpId

	@GrpId.setter
	def GrpId(self, value):
		self._GrpId = value if type(value) != base_types.auto else self.make_default("GrpId")

	@GrpId.deleter
	def GrpId(self):
		del self._GrpId
		self._GrpId = None

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != base_types.auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if type(value) != base_types.auto else self.make_default("ModCd")

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpId', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=PartyAndCertificate7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
	))

