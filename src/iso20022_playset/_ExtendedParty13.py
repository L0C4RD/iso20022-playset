# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContactAttributes5
from . import GenericIdentification36

class ExtendedParty13(base_types._BaseFieldType):

	__slots__ = ["_OthrPtyDtls", "_PtyRole"]
	@property
	def OthrPtyDtls(self):
		return self._OthrPtyDtls

	@OthrPtyDtls.setter
	def OthrPtyDtls(self, value):
		self._OthrPtyDtls = value if value is not None else base_types.UninitialisedField(self, 'OthrPtyDtls', ContactAttributes5, False)

	@OthrPtyDtls.deleter
	def OthrPtyDtls(self):
		del self._OthrPtyDtls
		self._OthrPtyDtls = base_types.UninitialisedField(self, 'OthrPtyDtls', ContactAttributes5, False)

	@property
	def PtyRole(self):
		return self._PtyRole

	@PtyRole.setter
	def PtyRole(self, value):
		self._PtyRole = value if value is not None else base_types.UninitialisedField(self, 'PtyRole', GenericIdentification36, False)

	@PtyRole.deleter
	def PtyRole(self):
		del self._PtyRole
		self._PtyRole = base_types.UninitialisedField(self, 'PtyRole', GenericIdentification36, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPtyDtls', type=ContactAttributes5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyRole', type=GenericIdentification36, min=1, max=1, mutex_group=None, array=False),
	))