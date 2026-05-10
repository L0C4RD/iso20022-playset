from . import base_types
from .Max35Text import Max35Text
from .CountryCode import CountryCode

class IdentificationSource5Choice(base_types._BaseFieldType):

	__slots__ = ["_DmstIdSrc", "_PrtryIdSrc"]
	@property
	def DmstIdSrc(self):
		return self._DmstIdSrc

	@DmstIdSrc.setter
	def DmstIdSrc(self, value):
		self._DmstIdSrc = value if type(value) != base_types.auto else self.make_default("DmstIdSrc")

	@DmstIdSrc.deleter
	def DmstIdSrc(self):
		del self._DmstIdSrc
		self._DmstIdSrc = None

	@property
	def PrtryIdSrc(self):
		return self._PrtryIdSrc

	@PrtryIdSrc.setter
	def PrtryIdSrc(self, value):
		self._PrtryIdSrc = value if type(value) != base_types.auto else self.make_default("PrtryIdSrc")

	@PrtryIdSrc.deleter
	def PrtryIdSrc(self):
		del self._PrtryIdSrc
		self._PrtryIdSrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DmstIdSrc', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryIdSrc', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

