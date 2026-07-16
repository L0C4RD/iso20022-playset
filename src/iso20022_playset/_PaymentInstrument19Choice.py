# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Cheque4

class PaymentInstrument19Choice(base_types._BaseFieldType):

	__slots__ = ["_BkrsDrftDtls", "_ChqDtls"]
	@property
	def BkrsDrftDtls(self):
		return self._BkrsDrftDtls

	@BkrsDrftDtls.setter
	def BkrsDrftDtls(self, value):
		self._BkrsDrftDtls = value if value is not None else base_types.UninitialisedField(self, 'BkrsDrftDtls', Cheque4, False)

	@BkrsDrftDtls.deleter
	def BkrsDrftDtls(self):
		del self._BkrsDrftDtls
		self._BkrsDrftDtls = base_types.UninitialisedField(self, 'BkrsDrftDtls', Cheque4, False)

	@property
	def ChqDtls(self):
		return self._ChqDtls

	@ChqDtls.setter
	def ChqDtls(self, value):
		self._ChqDtls = value if value is not None else base_types.UninitialisedField(self, 'ChqDtls', Cheque4, False)

	@ChqDtls.deleter
	def ChqDtls(self):
		del self._ChqDtls
		self._ChqDtls = base_types.UninitialisedField(self, 'ChqDtls', Cheque4, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkrsDrftDtls', type=Cheque4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChqDtls', type=Cheque4, min=0, max=1, mutex_group=1, array=False),
	))