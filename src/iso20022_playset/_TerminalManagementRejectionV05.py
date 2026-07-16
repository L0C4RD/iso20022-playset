# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorRejection3
from . import TMSHeader1

class TerminalManagementRejectionV05(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_Rjct"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', TMSHeader1, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', TMSHeader1, False)

	@property
	def Rjct(self):
		return self._Rjct

	@Rjct.setter
	def Rjct(self, value):
		self._Rjct = value if value is not None else base_types.UninitialisedField(self, 'Rjct', AcceptorRejection3, False)

	@Rjct.deleter
	def Rjct(self):
		del self._Rjct
		self._Rjct = base_types.UninitialisedField(self, 'Rjct', AcceptorRejection3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=TMSHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rjct', type=AcceptorRejection3, min=1, max=1, mutex_group=None, array=False),
	))