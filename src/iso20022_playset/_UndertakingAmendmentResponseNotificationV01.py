# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amendment9
from . import Max2000Text
from . import PartyAndSignature2

class UndertakingAmendmentResponseNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_DgtlSgntr", "_UdrtkgAmdmntRspnNtfctnDtls"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max2000Text, False)

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
	def UdrtkgAmdmntRspnNtfctnDtls(self):
		return self._UdrtkgAmdmntRspnNtfctnDtls

	@UdrtkgAmdmntRspnNtfctnDtls.setter
	def UdrtkgAmdmntRspnNtfctnDtls(self, value):
		self._UdrtkgAmdmntRspnNtfctnDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgAmdmntRspnNtfctnDtls', Amendment9, False)

	@UdrtkgAmdmntRspnNtfctnDtls.deleter
	def UdrtkgAmdmntRspnNtfctnDtls(self):
		del self._UdrtkgAmdmntRspnNtfctnDtls
		self._UdrtkgAmdmntRspnNtfctnDtls = base_types.UninitialisedField(self, 'UdrtkgAmdmntRspnNtfctnDtls', Amendment9, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgAmdmntRspnNtfctnDtls', type=Amendment9, min=1, max=1, mutex_group=None, array=False),
	))