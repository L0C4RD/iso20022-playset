# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PaymentInstrument21Choice import PaymentInstrument21Choice

class PaymentTransaction72(base_types._BaseFieldType):

	__slots__ = ["_PmtInstrm"]
	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if type(value) != base_types.auto else self.make_default("PmtInstrm")

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtInstrm', type=PaymentInstrument21Choice, min=1, max=1, mutex_group=None, array=False),
	))