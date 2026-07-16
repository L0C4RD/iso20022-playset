# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorRejection2
from . import Header41

class SaleToPOIMessageRejectionV02(base_types._BaseFieldType):

	__slots__ = ["_Hdr", "_Rjct"]
	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header41, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header41, False)

	@property
	def Rjct(self):
		return self._Rjct

	@Rjct.setter
	def Rjct(self, value):
		self._Rjct = value if value is not None else base_types.UninitialisedField(self, 'Rjct', AcceptorRejection2, False)

	@Rjct.deleter
	def Rjct(self):
		del self._Rjct
		self._Rjct = base_types.UninitialisedField(self, 'Rjct', AcceptorRejection2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hdr', type=Header41, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rjct', type=AcceptorRejection2, min=1, max=1, mutex_group=None, array=False),
	))