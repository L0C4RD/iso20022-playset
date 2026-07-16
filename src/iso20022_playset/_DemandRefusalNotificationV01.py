# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DemandRefusal1
from . import PartyAndSignature2

class DemandRefusalNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_DmndRfslNtfctnDtls"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@property
	def DmndRfslNtfctnDtls(self):
		return self._DmndRfslNtfctnDtls

	@DmndRfslNtfctnDtls.setter
	def DmndRfslNtfctnDtls(self, value):
		self._DmndRfslNtfctnDtls = value if value is not None else base_types.UninitialisedField(self, 'DmndRfslNtfctnDtls', DemandRefusal1, True)

	@DmndRfslNtfctnDtls.deleter
	def DmndRfslNtfctnDtls(self):
		del self._DmndRfslNtfctnDtls
		self._DmndRfslNtfctnDtls = base_types.UninitialisedField(self, 'DmndRfslNtfctnDtls', DemandRefusal1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndRfslNtfctnDtls', type=DemandRefusal1, min=0, max=None, mutex_group=None, array=True),
	))