from . import base_types
from .CutOff1 import CutOff1
from .NettingIdentification2Choice import NettingIdentification2Choice

class NettingCutOff2(base_types._BaseFieldType):

	__slots__ = ["_NewCutOff", "_NetgId"]
	@property
	def NewCutOff(self):
		return self._NewCutOff

	@NewCutOff.setter
	def NewCutOff(self, value):
		self._NewCutOff = value if type(value) != base_types.auto else self.make_default("NewCutOff")

	@NewCutOff.deleter
	def NewCutOff(self):
		del self._NewCutOff
		self._NewCutOff = None

	@property
	def NetgId(self):
		return self._NetgId

	@NetgId.setter
	def NetgId(self, value):
		self._NetgId = value if type(value) != base_types.auto else self.make_default("NetgId")

	@NetgId.deleter
	def NetgId(self):
		del self._NetgId
		self._NetgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NewCutOff', type=CutOff1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetgId', type=NettingIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
	))

