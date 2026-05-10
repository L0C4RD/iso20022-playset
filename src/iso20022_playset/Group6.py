import base_types
import PartyAndCertificate6
import Max4AlphaNumericText

class Group6(base_types._BaseFieldType):

	__slots__ = ["_GrpId", "_Pty"]
	@property
	def GrpId(self):
		return self._GrpId

	@GrpId.setter
	def GrpId(self, value):
		self._GrpId = value if type(value) != auto else self.make_default("GrpId")

	@GrpId.deleter
	def GrpId(self):
		del self._GrpId
		self._GrpId = None

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GrpId', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=PartyAndCertificate6, min=1, max=None, mutex_group=None, array=True),
	))

