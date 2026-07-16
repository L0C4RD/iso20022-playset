# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max2000Text
from . import PartyAndSignature2
from . import Undertaking1

class UndertakingApplicationV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_InstrsToBk", "_UdrtkgApplDtls"]
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
	def InstrsToBk(self):
		return self._InstrsToBk

	@InstrsToBk.setter
	def InstrsToBk(self, value):
		self._InstrsToBk = value if value is not None else base_types.UninitialisedField(self, 'InstrsToBk', Max2000Text, True)

	@InstrsToBk.deleter
	def InstrsToBk(self):
		del self._InstrsToBk
		self._InstrsToBk = base_types.UninitialisedField(self, 'InstrsToBk', Max2000Text, True)

	@property
	def UdrtkgApplDtls(self):
		return self._UdrtkgApplDtls

	@UdrtkgApplDtls.setter
	def UdrtkgApplDtls(self, value):
		self._UdrtkgApplDtls = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgApplDtls', Undertaking1, False)

	@UdrtkgApplDtls.deleter
	def UdrtkgApplDtls(self):
		del self._UdrtkgApplDtls
		self._UdrtkgApplDtls = base_types.UninitialisedField(self, 'UdrtkgApplDtls', Undertaking1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrsToBk', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='UdrtkgApplDtls', type=Undertaking1, min=1, max=1, mutex_group=None, array=False),
	))