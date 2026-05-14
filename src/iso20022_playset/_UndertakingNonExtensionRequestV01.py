# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyAndSignature2 import PartyAndSignature2
from ._UndertakingNonExtensionRequest1 import UndertakingNonExtensionRequest1

class UndertakingNonExtensionRequestV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgNonXtnsnReqDtls"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != base_types.auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def UdrtkgNonXtnsnReqDtls(self):
		return self._UdrtkgNonXtnsnReqDtls

	@UdrtkgNonXtnsnReqDtls.setter
	def UdrtkgNonXtnsnReqDtls(self, value):
		self._UdrtkgNonXtnsnReqDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgNonXtnsnReqDtls")

	@UdrtkgNonXtnsnReqDtls.deleter
	def UdrtkgNonXtnsnReqDtls(self):
		del self._UdrtkgNonXtnsnReqDtls
		self._UdrtkgNonXtnsnReqDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgNonXtnsnReqDtls', type=UndertakingNonExtensionRequest1, min=1, max=1, mutex_group=None, array=False),
	))