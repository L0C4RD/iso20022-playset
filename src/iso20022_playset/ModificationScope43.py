from . import base_types
from .DataModification1Code import DataModification1Code
from .ReferredAgent3 import ReferredAgent3

class ModificationScope43(base_types._BaseFieldType):

	__slots__ = ["_Plcmnt", "_ModScpIndctn"]
	@property
	def Plcmnt(self):
		return self._Plcmnt

	@Plcmnt.setter
	def Plcmnt(self, value):
		self._Plcmnt = value if type(value) != base_types.auto else self.make_default("Plcmnt")

	@Plcmnt.deleter
	def Plcmnt(self):
		del self._Plcmnt
		self._Plcmnt = None

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
		base_types.FieldEntry(name='Plcmnt', type=ReferredAgent3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))

