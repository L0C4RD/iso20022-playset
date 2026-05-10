import base_types
import Max70Text
import CountryCode
import Max35Text

class AlternateSecurityIdentification3(base_types._BaseFieldType):

	__slots__ = ["_DmstIdSrc", "_Id", "_PrtryIdSrc"]
	@property
	def DmstIdSrc(self):
		return self._DmstIdSrc

	@DmstIdSrc.setter
	def DmstIdSrc(self, value):
		self._DmstIdSrc = value if type(value) != auto else self.make_default("DmstIdSrc")

	@DmstIdSrc.deleter
	def DmstIdSrc(self):
		del self._DmstIdSrc
		self._DmstIdSrc = None

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
	def PrtryIdSrc(self):
		return self._PrtryIdSrc

	@PrtryIdSrc.setter
	def PrtryIdSrc(self, value):
		self._PrtryIdSrc = value if type(value) != auto else self.make_default("PrtryIdSrc")

	@PrtryIdSrc.deleter
	def PrtryIdSrc(self):
		del self._PrtryIdSrc
		self._PrtryIdSrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DmstIdSrc', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryIdSrc', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

