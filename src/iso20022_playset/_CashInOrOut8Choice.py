# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaymentInstrument28Choice
from . import PaymentInstrument30Choice

class CashInOrOut8Choice(base_types._BaseFieldType):

	__slots__ = ["_CshInPmtInstrm", "_CshOutPmtInstrm"]
	@property
	def CshInPmtInstrm(self):
		return self._CshInPmtInstrm

	@CshInPmtInstrm.setter
	def CshInPmtInstrm(self, value):
		self._CshInPmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'CshInPmtInstrm', PaymentInstrument30Choice, False)

	@CshInPmtInstrm.deleter
	def CshInPmtInstrm(self):
		del self._CshInPmtInstrm
		self._CshInPmtInstrm = base_types.UninitialisedField(self, 'CshInPmtInstrm', PaymentInstrument30Choice, False)

	@property
	def CshOutPmtInstrm(self):
		return self._CshOutPmtInstrm

	@CshOutPmtInstrm.setter
	def CshOutPmtInstrm(self, value):
		self._CshOutPmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'CshOutPmtInstrm', PaymentInstrument28Choice, False)

	@CshOutPmtInstrm.deleter
	def CshOutPmtInstrm(self):
		del self._CshOutPmtInstrm
		self._CshOutPmtInstrm = base_types.UninitialisedField(self, 'CshOutPmtInstrm', PaymentInstrument28Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshInPmtInstrm', type=PaymentInstrument30Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CshOutPmtInstrm', type=PaymentInstrument28Choice, min=0, max=1, mutex_group=1, array=False),
	))