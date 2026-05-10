from . import base_types
import Max35Text
import DocumentNumber5Choice

class GenericDocumentIdentification4(base_types._BaseFieldType):

	__slots__ = ["_MsgNb", "_Id"]
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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgNb', type=DocumentNumber5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

