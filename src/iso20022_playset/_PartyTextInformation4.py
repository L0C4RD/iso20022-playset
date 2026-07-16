# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINXMax140Text
from . import RestrictedFINXMax350Text

class PartyTextInformation4(base_types._BaseFieldType):

	__slots__ = ["_DclrtnDtls", "_PtyCtctDtls"]
	@property
	def DclrtnDtls(self):
		return self._DclrtnDtls

	@DclrtnDtls.setter
	def DclrtnDtls(self, value):
		self._DclrtnDtls = value if value is not None else base_types.UninitialisedField(self, 'DclrtnDtls', RestrictedFINXMax350Text, False)

	@DclrtnDtls.deleter
	def DclrtnDtls(self):
		del self._DclrtnDtls
		self._DclrtnDtls = base_types.UninitialisedField(self, 'DclrtnDtls', RestrictedFINXMax350Text, False)

	@property
	def PtyCtctDtls(self):
		return self._PtyCtctDtls

	@PtyCtctDtls.setter
	def PtyCtctDtls(self, value):
		self._PtyCtctDtls = value if value is not None else base_types.UninitialisedField(self, 'PtyCtctDtls', RestrictedFINXMax140Text, False)

	@PtyCtctDtls.deleter
	def PtyCtctDtls(self):
		del self._PtyCtctDtls
		self._PtyCtctDtls = base_types.UninitialisedField(self, 'PtyCtctDtls', RestrictedFINXMax140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DclrtnDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyCtctDtls', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
	))