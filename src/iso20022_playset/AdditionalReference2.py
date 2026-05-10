import base_types
import PartyIdentification1Choice
import Max35Text

class AdditionalReference2(base_types._BaseFieldType):

	__slots__ = ["_RefIssr", "_Ref", "_MsgNm"]
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
	def MsgNm(self):
		return self._MsgNm

	@MsgNm.setter
	def MsgNm(self, value):
		self._MsgNm = value if type(value) != auto else self.make_default("MsgNm")

	@MsgNm.deleter
	def MsgNm(self):
		del self._MsgNm
		self._MsgNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RefIssr', type=PartyIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

