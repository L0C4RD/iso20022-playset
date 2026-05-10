from . import base_types
from .ProcessingPosition7Choice import ProcessingPosition7Choice
from .DocumentNumber5Choice import DocumentNumber5Choice
from .References41Choice import References41Choice
from .PartyIdentification127Choice import PartyIdentification127Choice

class Linkages59(base_types._BaseFieldType):

	__slots__ = ["_RefOwnr", "_Ref", "_PrcgPos", "_MsgNb"]
	@property
	def RefOwnr(self):
		return self._RefOwnr

	@RefOwnr.setter
	def RefOwnr(self, value):
		self._RefOwnr = value if type(value) != base_types.auto else self.make_default("RefOwnr")

	@RefOwnr.deleter
	def RefOwnr(self):
		del self._RefOwnr
		self._RefOwnr = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def PrcgPos(self):
		return self._PrcgPos

	@PrcgPos.setter
	def PrcgPos(self, value):
		self._PrcgPos = value if type(value) != base_types.auto else self.make_default("PrcgPos")

	@PrcgPos.deleter
	def PrcgPos(self):
		del self._PrcgPos
		self._PrcgPos = None

	@property
	def MsgNb(self):
		return self._MsgNb

	@MsgNb.setter
	def MsgNb(self, value):
		self._MsgNb = value if type(value) != base_types.auto else self.make_default("MsgNb")

	@MsgNb.deleter
	def MsgNb(self):
		del self._MsgNb
		self._MsgNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RefOwnr', type=PartyIdentification127Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References41Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgPos', type=ProcessingPosition7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber5Choice, min=0, max=1, mutex_group=None, array=False),
	))

