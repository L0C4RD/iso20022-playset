# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification43
from . import Undertaking7

class UndertakingNonExtensionStatusAdvice1(base_types._BaseFieldType):

	__slots__ = ["_NtifngPty", "_UdrtkgId"]
	@property
	def NtifngPty(self):
		return self._NtifngPty

	@NtifngPty.setter
	def NtifngPty(self, value):
		self._NtifngPty = value if value is not None else base_types.UninitialisedField(self, 'NtifngPty', PartyIdentification43, False)

	@NtifngPty.deleter
	def NtifngPty(self):
		del self._NtifngPty
		self._NtifngPty = base_types.UninitialisedField(self, 'NtifngPty', PartyIdentification43, False)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking7, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtifngPty', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking7, min=1, max=1, mutex_group=None, array=False),
	))