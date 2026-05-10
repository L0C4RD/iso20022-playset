from . import base_types
from ._MarginRequirement1 import MarginRequirement1
from ._Requirement1 import Requirement1

class MarginRequirement1Choice(base_types._BaseFieldType):

	__slots__ = ["_SgrtdIndpdntAmtRqrmnt", "_MrgnRqrmnt"]
	@property
	def SgrtdIndpdntAmtRqrmnt(self):
		return self._SgrtdIndpdntAmtRqrmnt

	@SgrtdIndpdntAmtRqrmnt.setter
	def SgrtdIndpdntAmtRqrmnt(self, value):
		self._SgrtdIndpdntAmtRqrmnt = value if type(value) != base_types.auto else self.make_default("SgrtdIndpdntAmtRqrmnt")

	@SgrtdIndpdntAmtRqrmnt.deleter
	def SgrtdIndpdntAmtRqrmnt(self):
		del self._SgrtdIndpdntAmtRqrmnt
		self._SgrtdIndpdntAmtRqrmnt = None

	@property
	def MrgnRqrmnt(self):
		return self._MrgnRqrmnt

	@MrgnRqrmnt.setter
	def MrgnRqrmnt(self, value):
		self._MrgnRqrmnt = value if type(value) != base_types.auto else self.make_default("MrgnRqrmnt")

	@MrgnRqrmnt.deleter
	def MrgnRqrmnt(self):
		del self._MrgnRqrmnt
		self._MrgnRqrmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SgrtdIndpdntAmtRqrmnt', type=MarginRequirement1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MrgnRqrmnt', type=Requirement1, min=0, max=1, mutex_group=1, array=False),
	))

