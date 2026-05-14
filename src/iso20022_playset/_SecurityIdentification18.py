# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IdentificationType2Code import IdentificationType2Code
from ._Max35Text import Max35Text

class SecurityIdentification18(base_types._BaseFieldType):

	__slots__ = ["_SctyId", "_SctyIdSrc"]
	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	@property
	def SctyIdSrc(self):
		return self._SctyIdSrc

	@SctyIdSrc.setter
	def SctyIdSrc(self, value):
		self._SctyIdSrc = value if type(value) != base_types.auto else self.make_default("SctyIdSrc")

	@SctyIdSrc.deleter
	def SctyIdSrc(self):
		del self._SctyIdSrc
		self._SctyIdSrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyIdSrc', type=IdentificationType2Code, min=1, max=1, mutex_group=None, array=False),
	))