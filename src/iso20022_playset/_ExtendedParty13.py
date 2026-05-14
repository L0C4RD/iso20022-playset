# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ContactAttributes5 import ContactAttributes5
from ._GenericIdentification36 import GenericIdentification36

class ExtendedParty13(base_types._BaseFieldType):

	__slots__ = ["_OthrPtyDtls", "_PtyRole"]
	@property
	def OthrPtyDtls(self):
		return self._OthrPtyDtls

	@OthrPtyDtls.setter
	def OthrPtyDtls(self, value):
		self._OthrPtyDtls = value if type(value) != base_types.auto else self.make_default("OthrPtyDtls")

	@OthrPtyDtls.deleter
	def OthrPtyDtls(self):
		del self._OthrPtyDtls
		self._OthrPtyDtls = None

	@property
	def PtyRole(self):
		return self._PtyRole

	@PtyRole.setter
	def PtyRole(self, value):
		self._PtyRole = value if type(value) != base_types.auto else self.make_default("PtyRole")

	@PtyRole.deleter
	def PtyRole(self):
		del self._PtyRole
		self._PtyRole = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPtyDtls', type=ContactAttributes5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyRole', type=GenericIdentification36, min=1, max=1, mutex_group=None, array=False),
	))