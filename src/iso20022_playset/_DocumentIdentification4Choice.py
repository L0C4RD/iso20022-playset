# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RestrictedFINXMax16Text

class DocumentIdentification4Choice(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnrDocId", "_AcctSvcrDocId"]
	@property
	def AcctOwnrDocId(self):
		return self._AcctOwnrDocId

	@AcctOwnrDocId.setter
	def AcctOwnrDocId(self, value):
		self._AcctOwnrDocId = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnrDocId', RestrictedFINXMax16Text, False)

	@AcctOwnrDocId.deleter
	def AcctOwnrDocId(self):
		del self._AcctOwnrDocId
		self._AcctOwnrDocId = base_types.UninitialisedField(self, 'AcctOwnrDocId', RestrictedFINXMax16Text, False)

	@property
	def AcctSvcrDocId(self):
		return self._AcctSvcrDocId

	@AcctSvcrDocId.setter
	def AcctSvcrDocId(self, value):
		self._AcctSvcrDocId = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrDocId', RestrictedFINXMax16Text, False)

	@AcctSvcrDocId.deleter
	def AcctSvcrDocId(self):
		del self._AcctSvcrDocId
		self._AcctSvcrDocId = base_types.UninitialisedField(self, 'AcctSvcrDocId', RestrictedFINXMax16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnrDocId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AcctSvcrDocId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
	))