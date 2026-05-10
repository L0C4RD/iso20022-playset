from . import base_types
import PositionSetCollateralTotal2

class PositionSetCollateralMetrics2(base_types._BaseFieldType):

	__slots__ = ["_Clean", "_Ttl"]
	@property
	def Clean(self):
		return self._Clean

	@Clean.setter
	def Clean(self, value):
		self._Clean = value if type(value) != auto else self.make_default("Clean")

	@Clean.deleter
	def Clean(self):
		del self._Clean
		self._Clean = None

	@property
	def Ttl(self):
		return self._Ttl

	@Ttl.setter
	def Ttl(self, value):
		self._Ttl = value if type(value) != auto else self.make_default("Ttl")

	@Ttl.deleter
	def Ttl(self):
		del self._Ttl
		self._Ttl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clean', type=PositionSetCollateralTotal2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ttl', type=PositionSetCollateralTotal2, min=0, max=1, mutex_group=None, array=False),
	))

