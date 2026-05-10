import base_types
import AssetHolding1
import GenericIdentification165

class CollateralAccount4(base_types._BaseFieldType):

	__slots__ = ["_Id", "_AsstHldg"]
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

	@property
	def AsstHldg(self):
		return self._AsstHldg

	@AsstHldg.setter
	def AsstHldg(self, value):
		self._AsstHldg = value if type(value) != auto else self.make_default("AsstHldg")

	@AsstHldg.deleter
	def AsstHldg(self):
		del self._AsstHldg
		self._AsstHldg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstHldg', type=AssetHolding1, min=1, max=None, mutex_group=None, array=True),
	))

