from . import base_types
from .DataModification2Code import DataModification2Code
from .CitizenshipInformation2 import CitizenshipInformation2

class ModificationScope39(base_types._BaseFieldType):

	__slots__ = ["_Ctznsh", "_ModScpIndctn"]
	@property
	def Ctznsh(self):
		return self._Ctznsh

	@Ctznsh.setter
	def Ctznsh(self, value):
		self._Ctznsh = value if type(value) != base_types.auto else self.make_default("Ctznsh")

	@Ctznsh.deleter
	def Ctznsh(self):
		del self._Ctznsh
		self._Ctznsh = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ctznsh', type=CitizenshipInformation2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification2Code, min=1, max=1, mutex_group=None, array=False),
	))

