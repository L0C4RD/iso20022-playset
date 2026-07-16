# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SafekeepingAccountIdentification1Code

class AccountIdentification10(base_types._BaseFieldType):

	__slots__ = ["_IdCd"]
	@property
	def IdCd(self):
		return self._IdCd

	@IdCd.setter
	def IdCd(self, value):
		self._IdCd = value if value is not None else base_types.UninitialisedField(self, 'IdCd', SafekeepingAccountIdentification1Code, False)

	@IdCd.deleter
	def IdCd(self):
		del self._IdCd
		self._IdCd = base_types.UninitialisedField(self, 'IdCd', SafekeepingAccountIdentification1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdCd', type=SafekeepingAccountIdentification1Code, min=1, max=1, mutex_group=None, array=False),
	))