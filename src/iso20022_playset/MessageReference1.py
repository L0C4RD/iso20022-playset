from . import base_types
from .Max35Text import Max35Text
from .PartyIdentification136 import PartyIdentification136

class MessageReference1(base_types._BaseFieldType):

	__slots__ = ["_MsgNm", "_Ref", "_RefIssr"]
	@property
	def MsgNm(self):
		return self._MsgNm

	@MsgNm.setter
	def MsgNm(self, value):
		self._MsgNm = value if type(value) != auto else self.make_default("MsgNm")

	@MsgNm.deleter
	def MsgNm(self):
		del self._MsgNm
		self._MsgNm = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def RefIssr(self):
		return self._RefIssr

	@RefIssr.setter
	def RefIssr(self, value):
		self._RefIssr = value if type(value) != auto else self.make_default("RefIssr")

	@RefIssr.deleter
	def RefIssr(self):
		del self._RefIssr
		self._RefIssr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefIssr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
	))

