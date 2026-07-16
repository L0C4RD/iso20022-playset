# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaymentInstrument20Choice
from . import PaymentInstrument21Choice

class CashInOrOut7Choice(base_types._BaseFieldType):

	__slots__ = ["_CshInPmtInstrm", "_CshOutPmtInstrm"]
	@property
	def CshInPmtInstrm(self):
		return self._CshInPmtInstrm

	@CshInPmtInstrm.setter
	def CshInPmtInstrm(self, value):
		self._CshInPmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'CshInPmtInstrm', PaymentInstrument20Choice, False)

	@CshInPmtInstrm.deleter
	def CshInPmtInstrm(self):
		del self._CshInPmtInstrm
		self._CshInPmtInstrm = base_types.UninitialisedField(self, 'CshInPmtInstrm', PaymentInstrument20Choice, False)

	@property
	def CshOutPmtInstrm(self):
		return self._CshOutPmtInstrm

	@CshOutPmtInstrm.setter
	def CshOutPmtInstrm(self, value):
		self._CshOutPmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'CshOutPmtInstrm', PaymentInstrument21Choice, False)

	@CshOutPmtInstrm.deleter
	def CshOutPmtInstrm(self):
		del self._CshOutPmtInstrm
		self._CshOutPmtInstrm = base_types.UninitialisedField(self, 'CshOutPmtInstrm', PaymentInstrument21Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInPmtInstrm', type=PaymentInstrument20Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshOutPmtInstrm', type=PaymentInstrument21Choice, min=0, max=1, mutex_group=1, array=False),
	))