import base_types
import AssetClassAndSubClassIdentification2
import InstrumentAndSubClassIdentification2

class InstrumentOrSubClassIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_AsstClssAndSubClss", "_ISINAndSubClss"]
	@property
	def AsstClssAndSubClss(self):
		return self._AsstClssAndSubClss

	@AsstClssAndSubClss.setter
	def AsstClssAndSubClss(self, value):
		self._AsstClssAndSubClss = value if type(value) != auto else self.make_default("AsstClssAndSubClss")

	@AsstClssAndSubClss.deleter
	def AsstClssAndSubClss(self):
		del self._AsstClssAndSubClss
		self._AsstClssAndSubClss = None

	@property
	def ISINAndSubClss(self):
		return self._ISINAndSubClss

	@ISINAndSubClss.setter
	def ISINAndSubClss(self, value):
		self._ISINAndSubClss = value if type(value) != auto else self.make_default("ISINAndSubClss")

	@ISINAndSubClss.deleter
	def ISINAndSubClss(self):
		del self._ISINAndSubClss
		self._ISINAndSubClss = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstClssAndSubClss', type=AssetClassAndSubClassIdentification2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISINAndSubClss', type=InstrumentAndSubClassIdentification2, min=0, max=1, mutex_group=1, array=False),
	))

