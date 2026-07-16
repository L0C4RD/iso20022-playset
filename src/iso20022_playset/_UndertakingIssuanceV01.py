# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2000Text
from . import PartyAndSignature2
from . import Undertaking3

class UndertakingIssuanceV01(base_types._BaseFieldType):

	__slots__ = ["_BkToBkInf", "_BkToBnfcryInf", "_DgtlSgntr", "_UdrtkgIssncDtls"]
	@property
	def BkToBkInf(self):
		return self._BkToBkInf

	@BkToBkInf.setter
	def BkToBkInf(self, value):
		self._BkToBkInf = value if value is not None else base_types.UninitialisedField(self, 'BkToBkInf', Max2000Text, True)

	@BkToBkInf.deleter
	def BkToBkInf(self):
		del self._BkToBkInf
		self._BkToBkInf = base_types.UninitialisedField(self, 'BkToBkInf', Max2000Text, True)

	@property
	def BkToBnfcryInf(self):
		return self._BkToBnfcryInf

	@BkToBnfcryInf.setter
	def BkToBnfcryInf(self, value):
		self._BkToBnfcryInf = value if value is not None else base_types.UninitialisedField(self, 'BkToBnfcryInf', Max2000Text, True)

	@BkToBnfcryInf.deleter
	def BkToBnfcryInf(self):
		del self._BkToBnfcryInf
		self._BkToBnfcryInf = base_types.UninitialisedField(self, 'BkToBnfcryInf', Max2000Text, True)

	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, True)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, True)

	@property
	def UdrtkgIssncDtls(self):
		return self._UdrtkgIssncDtls

	@UdrtkgIssncDtls.setter
	def UdrtkgIssncDtls(self, value):
		self._UdrtkgIssncDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgIssncDtls', Undertaking3, False)

	@UdrtkgIssncDtls.deleter
	def UdrtkgIssncDtls(self):
		del self._UdrtkgIssncDtls
		self._UdrtkgIssncDtls = base_types.UninitialisedField(self, 'UdrtkgIssncDtls', Undertaking3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkToBkInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='BkToBnfcryInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UdrtkgIssncDtls', type=Undertaking3, min=1, max=1, mutex_group=None, array=False),
	))