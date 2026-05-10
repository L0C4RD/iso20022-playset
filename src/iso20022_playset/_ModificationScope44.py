from . import base_types
from ._DocumentToSend4 import DocumentToSend4
from ._DataModification1Code import DataModification1Code

class ModificationScope44(base_types._BaseFieldType):

	__slots__ = ["_ModScpIndctn", "_SvcLvlAgrmt"]
	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if type(value) != base_types.auto else self.make_default("ModScpIndctn")

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = None

	@property
	def SvcLvlAgrmt(self):
		return self._SvcLvlAgrmt

	@SvcLvlAgrmt.setter
	def SvcLvlAgrmt(self, value):
		self._SvcLvlAgrmt = value if type(value) != base_types.auto else self.make_default("SvcLvlAgrmt")

	@SvcLvlAgrmt.deleter
	def SvcLvlAgrmt(self):
		del self._SvcLvlAgrmt
		self._SvcLvlAgrmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcLvlAgrmt', type=DocumentToSend4, min=1, max=1, mutex_group=None, array=False),
	))

