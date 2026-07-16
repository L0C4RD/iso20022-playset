# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashPaymentStatus2Code
from . import FinalStatusCode
from . import PendingStatus4Code

class PaymentStatusCodeSearch2Choice(base_types._BaseFieldType):

	__slots__ = ["_FnlSts", "_PdgAndFnlSts", "_PdgSts"]
	@property
	def FnlSts(self):
		return self._FnlSts

	@FnlSts.setter
	def FnlSts(self, value):
		self._FnlSts = value if value is not None else base_types.UninitialisedField(self, 'FnlSts', FinalStatusCode, False)

	@FnlSts.deleter
	def FnlSts(self):
		del self._FnlSts
		self._FnlSts = base_types.UninitialisedField(self, 'FnlSts', FinalStatusCode, False)

	@property
	def PdgAndFnlSts(self):
		return self._PdgAndFnlSts

	@PdgAndFnlSts.setter
	def PdgAndFnlSts(self, value):
		self._PdgAndFnlSts = value if value is not None else base_types.UninitialisedField(self, 'PdgAndFnlSts', CashPaymentStatus2Code, False)

	@PdgAndFnlSts.deleter
	def PdgAndFnlSts(self):
		del self._PdgAndFnlSts
		self._PdgAndFnlSts = base_types.UninitialisedField(self, 'PdgAndFnlSts', CashPaymentStatus2Code, False)

	@property
	def PdgSts(self):
		return self._PdgSts

	@PdgSts.setter
	def PdgSts(self, value):
		self._PdgSts = value if value is not None else base_types.UninitialisedField(self, 'PdgSts', PendingStatus4Code, False)

	@PdgSts.deleter
	def PdgSts(self):
		del self._PdgSts
		self._PdgSts = base_types.UninitialisedField(self, 'PdgSts', PendingStatus4Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FnlSts', type=FinalStatusCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgAndFnlSts', type=CashPaymentStatus2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgSts', type=PendingStatus4Code, min=0, max=1, mutex_group=1, array=False),
	))