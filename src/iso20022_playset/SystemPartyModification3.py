from . import base_types
import SystemPartyModification3Choice
import DataModification1Code

class SystemPartyModification3(base_types._BaseFieldType):

	__slots__ = ["_ReqdMod", "_ScpIndctn"]
	@property
	def ReqdMod(self):
		return self._ReqdMod

	@ReqdMod.setter
	def ReqdMod(self, value):
		self._ReqdMod = value if type(value) != auto else self.make_default("ReqdMod")

	@ReqdMod.deleter
	def ReqdMod(self):
		del self._ReqdMod
		self._ReqdMod = None

	@property
	def ScpIndctn(self):
		return self._ScpIndctn

	@ScpIndctn.setter
	def ScpIndctn(self, value):
		self._ScpIndctn = value if type(value) != auto else self.make_default("ScpIndctn")

	@ScpIndctn.deleter
	def ScpIndctn(self):
		del self._ScpIndctn
		self._ScpIndctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqdMod', type=SystemPartyModification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))

