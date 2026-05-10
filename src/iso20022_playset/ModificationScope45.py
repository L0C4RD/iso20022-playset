from . import base_types
import AdditiononalInformation13
import DataModification1Code

class ModificationScope45(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ModScpIndctn"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ModScpIndctn(self):
		return self._ModScpIndctn

	@ModScpIndctn.setter
	def ModScpIndctn(self, value):
		self._ModScpIndctn = value if type(value) != auto else self.make_default("ModScpIndctn")

	@ModScpIndctn.deleter
	def ModScpIndctn(self):
		del self._ModScpIndctn
		self._ModScpIndctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditiononalInformation13, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ModScpIndctn', type=DataModification1Code, min=1, max=1, mutex_group=None, array=False),
	))

