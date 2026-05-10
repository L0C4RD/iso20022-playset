from . import base_types
from ._DocumentNumber5Choice import DocumentNumber5Choice
from ._Max35Text import Max35Text
from ._PartyIdentification247Choice import PartyIdentification247Choice

class AdditionalReference14(base_types._BaseFieldType):

	__slots__ = ["_MsgNb", "_MsgNm", "_Ref", "_RefIssr"]
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
	def MsgNm(self):
		return self._MsgNm

	@MsgNm.setter
	def MsgNm(self, value):
		self._MsgNm = value if type(value) != base_types.auto else self.make_default("MsgNm")

	@MsgNm.deleter
	def MsgNm(self):
		del self._MsgNm
		self._MsgNm = None

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
	def RefIssr(self):
		return self._RefIssr

	@RefIssr.setter
	def RefIssr(self, value):
		self._RefIssr = value if type(value) != base_types.auto else self.make_default("RefIssr")

	@RefIssr.deleter
	def RefIssr(self):
		del self._RefIssr
		self._RefIssr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefIssr', type=PartyIdentification247Choice, min=0, max=1, mutex_group=None, array=False),
	))

