from . import base_types
import DocumentNumber17Choice
import IdentificationReference8Choice

class Linkages52(base_types._BaseFieldType):

	__slots__ = ["_MsgNb", "_Ref"]
	@property
	def MsgNb(self):
		return self._MsgNb

	@MsgNb.setter
	def MsgNb(self, value):
		self._MsgNb = value if type(value) != auto else self.make_default("MsgNb")

	@MsgNb.deleter
	def MsgNb(self):
		del self._MsgNb
		self._MsgNb = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber17Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=IdentificationReference8Choice, min=1, max=1, mutex_group=None, array=False),
	))

