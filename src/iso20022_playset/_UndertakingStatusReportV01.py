# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyAndSignature2 import PartyAndSignature2
from ._UndertakingStatusAdvice1 import UndertakingStatusAdvice1

class UndertakingStatusReportV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_UdrtkgStsRptDtls"]
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
	def UdrtkgStsRptDtls(self):
		return self._UdrtkgStsRptDtls

	@UdrtkgStsRptDtls.setter
	def UdrtkgStsRptDtls(self, value):
		self._UdrtkgStsRptDtls = value if type(value) != base_types.auto else self.make_default("UdrtkgStsRptDtls")

	@UdrtkgStsRptDtls.deleter
	def UdrtkgStsRptDtls(self):
		del self._UdrtkgStsRptDtls
		self._UdrtkgStsRptDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UdrtkgStsRptDtls', type=UndertakingStatusAdvice1, min=1, max=1, mutex_group=None, array=False),
	))