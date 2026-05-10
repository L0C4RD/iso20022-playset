from . import base_types
from .Max15PlusSignedNumericText import Max15PlusSignedNumericText
from .PartyOrGroup3Choice import PartyOrGroup3Choice
from .Authorisation2 import Authorisation2

class PartyAndAuthorisation7(base_types._BaseFieldType):

	__slots__ = ["_Authstn", "_SgntrOrdr", "_PtyOrGrp"]
	@property
	def Authstn(self):
		return self._Authstn

	@Authstn.setter
	def Authstn(self, value):
		self._Authstn = value if type(value) != base_types.auto else self.make_default("Authstn")

	@Authstn.deleter
	def Authstn(self):
		del self._Authstn
		self._Authstn = None

	@property
	def SgntrOrdr(self):
		return self._SgntrOrdr

	@SgntrOrdr.setter
	def SgntrOrdr(self, value):
		self._SgntrOrdr = value if type(value) != base_types.auto else self.make_default("SgntrOrdr")

	@SgntrOrdr.deleter
	def SgntrOrdr(self):
		del self._SgntrOrdr
		self._SgntrOrdr = None

	@property
	def PtyOrGrp(self):
		return self._PtyOrGrp

	@PtyOrGrp.setter
	def PtyOrGrp(self, value):
		self._PtyOrGrp = value if type(value) != base_types.auto else self.make_default("PtyOrGrp")

	@PtyOrGrp.deleter
	def PtyOrGrp(self):
		del self._PtyOrGrp
		self._PtyOrGrp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Authstn', type=Authorisation2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrOrdr', type=Max15PlusSignedNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyOrGrp', type=PartyOrGroup3Choice, min=1, max=1, mutex_group=None, array=False),
	))

