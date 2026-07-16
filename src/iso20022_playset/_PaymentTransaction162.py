# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaymentInstrument27Choice

class PaymentTransaction162(base_types._BaseFieldType):

	__slots__ = ["_PmtInstrm"]
	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrument27Choice, False)

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = base_types.UninitialisedField(self, 'PmtInstrm', PaymentInstrument27Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrument27Choice, min=1, max=1, mutex_group=None, array=False),
	))