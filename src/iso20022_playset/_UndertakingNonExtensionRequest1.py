# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification43
from . import Undertaking9

class UndertakingNonExtensionRequest1(base_types._BaseFieldType):

	__slots__ = ["_RqstngPty", "_UdrtkgId"]
	@property
	def RqstngPty(self):
		return self._RqstngPty

	@RqstngPty.setter
	def RqstngPty(self, value):
		self._RqstngPty = value if value is not None else base_types.UninitialisedField(self, 'RqstngPty', PartyIdentification43, False)

	@RqstngPty.deleter
	def RqstngPty(self):
		del self._RqstngPty
		self._RqstngPty = base_types.UninitialisedField(self, 'RqstngPty', PartyIdentification43, False)

	@property
	def UdrtkgId(self):
		return self._UdrtkgId

	@UdrtkgId.setter
	def UdrtkgId(self, value):
		self._UdrtkgId = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	@UdrtkgId.deleter
	def UdrtkgId(self):
		del self._UdrtkgId
		self._UdrtkgId = base_types.UninitialisedField(self, 'UdrtkgId', Undertaking9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RqstngPty', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgId', type=Undertaking9, min=1, max=1, mutex_group=None, array=False),
	))