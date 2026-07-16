# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyAndSignature2
from . import UndertakingDemandWithdrawal1

class DemandWithdrawalNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_DmndWdrwlNtfctnDtls"]
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
	def DmndWdrwlNtfctnDtls(self):
		return self._DmndWdrwlNtfctnDtls

	@DmndWdrwlNtfctnDtls.setter
	def DmndWdrwlNtfctnDtls(self, value):
		self._DmndWdrwlNtfctnDtls = value if value is not None else base_types.UninitialisedField(self, 'DmndWdrwlNtfctnDtls', UndertakingDemandWithdrawal1, False)

	@DmndWdrwlNtfctnDtls.deleter
	def DmndWdrwlNtfctnDtls(self):
		del self._DmndWdrwlNtfctnDtls
		self._DmndWdrwlNtfctnDtls = base_types.UninitialisedField(self, 'DmndWdrwlNtfctnDtls', UndertakingDemandWithdrawal1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmndWdrwlNtfctnDtls', type=UndertakingDemandWithdrawal1, min=1, max=1, mutex_group=None, array=False),
	))