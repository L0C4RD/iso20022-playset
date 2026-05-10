from . import base_types
from ._ProcessingPosition7Choice import ProcessingPosition7Choice
from ._DocumentNumber5Choice import DocumentNumber5Choice
from ._PartyIdentification127Choice import PartyIdentification127Choice
from ._References34Choice import References34Choice

class Linkages57(base_types._BaseFieldType):

	__slots__ = ["_MsgNb", "_Ref", "_RefOwnr", "_PrcgPos"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=References34Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefOwnr', type=PartyIdentification127Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgPos', type=ProcessingPosition7Choice, min=0, max=1, mutex_group=None, array=False),
	))

