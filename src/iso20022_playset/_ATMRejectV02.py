# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMReject2
from . import Header33

class ATMRejectV02(base_types._BaseFieldType):

	__slots__ = ["_ATMRjct", "_Hdr"]
	@property
	def ATMRjct(self):
		return self._ATMRjct

	@ATMRjct.setter
	def ATMRjct(self, value):
		self._ATMRjct = value if value is not None else base_types.UninitialisedField(self, 'ATMRjct', ATMReject2, False)

	@ATMRjct.deleter
	def ATMRjct(self):
		del self._ATMRjct
		self._ATMRjct = base_types.UninitialisedField(self, 'ATMRjct', ATMReject2, False)

	@property
	def Hdr(self):
		return self._Hdr

	@Hdr.setter
	def Hdr(self, value):
		self._Hdr = value if value is not None else base_types.UninitialisedField(self, 'Hdr', Header33, False)

	@Hdr.deleter
	def Hdr(self):
		del self._Hdr
		self._Hdr = base_types.UninitialisedField(self, 'Hdr', Header33, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMRjct', type=ATMReject2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hdr', type=Header33, min=1, max=1, mutex_group=None, array=False),
	))