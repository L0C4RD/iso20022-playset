# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMDepositResponseV02 import ATMDepositResponseV02

class CATP_013_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMDpstRspn"]
		@property
		def ATMDpstRspn(self):
			return self._ATMDpstRspn

		@ATMDpstRspn.setter
		def ATMDpstRspn(self, value):
			self._ATMDpstRspn = value if type(value) != base_types.auto else self.make_default("ATMDpstRspn")

		@ATMDpstRspn.deleter
		def ATMDpstRspn(self):
			del self._ATMDpstRspn
			self._ATMDpstRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDpstRspn', type=ATMDepositResponseV02, min=1, max=1, mutex_group=None, array=False),
		))