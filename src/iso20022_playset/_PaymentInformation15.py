# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccount7
from . import PaymentMethod4Code

class PaymentInformation15(base_types._BaseFieldType):

	__slots__ = ["_PmtAcct", "_PmtMtd"]
	@property
	def PmtAcct(self):
		return self._PmtAcct

	@PmtAcct.setter
	def PmtAcct(self, value):
		self._PmtAcct = value if value is not None else base_types.UninitialisedField(self, 'PmtAcct', CashAccount7, False)

	@PmtAcct.deleter
	def PmtAcct(self):
		del self._PmtAcct
		self._PmtAcct = base_types.UninitialisedField(self, 'PmtAcct', CashAccount7, False)

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if value is not None else base_types.UninitialisedField(self, 'PmtMtd', PaymentMethod4Code, False)

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = base_types.UninitialisedField(self, 'PmtMtd', PaymentMethod4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtAcct', type=CashAccount7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=PaymentMethod4Code, min=1, max=1, mutex_group=None, array=False),
	))