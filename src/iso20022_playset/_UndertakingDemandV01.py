# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Demand1
from . import Max2000Text
from . import PartyAndSignature2

class UndertakingDemandV01(base_types._BaseFieldType):

	__slots__ = ["_BkToBkInf", "_DgtlSgntr", "_UdrtkgDmndDtls"]
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
	def UdrtkgDmndDtls(self):
		return self._UdrtkgDmndDtls

	@UdrtkgDmndDtls.setter
	def UdrtkgDmndDtls(self, value):
		self._UdrtkgDmndDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgDmndDtls', Demand1, False)

	@UdrtkgDmndDtls.deleter
	def UdrtkgDmndDtls(self):
		del self._UdrtkgDmndDtls
		self._UdrtkgDmndDtls = base_types.UninitialisedField(self, 'UdrtkgDmndDtls', Demand1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BkToBkInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgDmndDtls', type=Demand1, min=1, max=1, mutex_group=None, array=False),
	))