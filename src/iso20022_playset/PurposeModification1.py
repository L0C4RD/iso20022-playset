from . import base_types
import Max140Text
import Modification1Code

class PurposeModification1(base_types._BaseFieldType):

	__slots__ = ["_ModCd", "_Purp"]
	@property
	def ModCd(self):
		return self._ModCd

	@ModCd.setter
	def ModCd(self, value):
		self._ModCd = value if type(value) != auto else self.make_default("ModCd")

	@ModCd.deleter
	def ModCd(self):
		del self._ModCd
		self._ModCd = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModCd', type=Modification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))

