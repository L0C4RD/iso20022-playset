from . import base_types
import Requirement1
import MarginRequirement1

class MarginRequirement1Choice(base_types._BaseFieldType):

	__slots__ = ["_MrgnRqrmnt", "_SgrtdIndpdntAmtRqrmnt"]
	@property
	def MrgnRqrmnt(self):
		return self._MrgnRqrmnt

	@MrgnRqrmnt.setter
	def MrgnRqrmnt(self, value):
		self._MrgnRqrmnt = value if type(value) != auto else self.make_default("MrgnRqrmnt")

	@MrgnRqrmnt.deleter
	def MrgnRqrmnt(self):
		del self._MrgnRqrmnt
		self._MrgnRqrmnt = None

	@property
	def SgrtdIndpdntAmtRqrmnt(self):
		return self._SgrtdIndpdntAmtRqrmnt

	@SgrtdIndpdntAmtRqrmnt.setter
	def SgrtdIndpdntAmtRqrmnt(self, value):
		self._SgrtdIndpdntAmtRqrmnt = value if type(value) != auto else self.make_default("SgrtdIndpdntAmtRqrmnt")

	@SgrtdIndpdntAmtRqrmnt.deleter
	def SgrtdIndpdntAmtRqrmnt(self):
		del self._SgrtdIndpdntAmtRqrmnt
		self._SgrtdIndpdntAmtRqrmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MrgnRqrmnt', type=Requirement1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SgrtdIndpdntAmtRqrmnt', type=MarginRequirement1, min=0, max=1, mutex_group=1, array=False),
	))

