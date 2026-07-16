# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import Max35Text

class AlternateSecurityIdentification1(base_types._BaseFieldType):

	__slots__ = ["_DmstIdSrc", "_Id", "_PrtryIdSrc"]
	@property
	def DmstIdSrc(self):
		return self._DmstIdSrc

	@DmstIdSrc.setter
	def DmstIdSrc(self, value):
		self._DmstIdSrc = value if value is not None else base_types.UninitialisedField(self, 'DmstIdSrc', CountryCode, False)

	@DmstIdSrc.deleter
	def DmstIdSrc(self):
		del self._DmstIdSrc
		self._DmstIdSrc = base_types.UninitialisedField(self, 'DmstIdSrc', CountryCode, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def PrtryIdSrc(self):
		return self._PrtryIdSrc

	@PrtryIdSrc.setter
	def PrtryIdSrc(self, value):
		self._PrtryIdSrc = value if value is not None else base_types.UninitialisedField(self, 'PrtryIdSrc', Max35Text, False)

	@PrtryIdSrc.deleter
	def PrtryIdSrc(self):
		del self._PrtryIdSrc
		self._PrtryIdSrc = base_types.UninitialisedField(self, 'PrtryIdSrc', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DmstIdSrc', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryIdSrc', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))