from . import base_types
from .References76Choice import References76Choice
from .DocumentNumber16Choice import DocumentNumber16Choice
from .PartyIdentification136Choice import PartyIdentification136Choice
from .ProcessingPosition18Choice import ProcessingPosition18Choice

class Linkages66(base_types._BaseFieldType):

	__slots__ = ["_MsgNb", "_PrcgPos", "_Ref", "_RefOwnr"]
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
	def RefOwnr(self):
		return self._RefOwnr

	@RefOwnr.setter
	def RefOwnr(self, value):
		self._RefOwnr = value if type(value) != base_types.auto else self.make_default("RefOwnr")

	@RefOwnr.deleter
	def RefOwnr(self):
		del self._RefOwnr
		self._RefOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber16Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgPos', type=ProcessingPosition18Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References76Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefOwnr', type=PartyIdentification136Choice, min=0, max=1, mutex_group=None, array=False),
	))

