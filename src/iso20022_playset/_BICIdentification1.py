# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentifier

class BICIdentification1(base_types._BaseFieldType):

	__slots__ = ["_BIC"]
	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if value is not None else base_types.UninitialisedField(self, 'BIC', BICIdentifier, False)

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = base_types.UninitialisedField(self, 'BIC', BICIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BIC', type=BICIdentifier, min=1, max=1, mutex_group=None, array=False),
	))