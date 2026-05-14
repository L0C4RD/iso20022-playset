# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DebitAuthorisationResponseV06 import DebitAuthorisationResponseV06

class CAMT_036_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DbtAuthstnRspn"]
		@property
		def DbtAuthstnRspn(self):
			return self._DbtAuthstnRspn

		@DbtAuthstnRspn.setter
		def DbtAuthstnRspn(self, value):
			self._DbtAuthstnRspn = value if type(value) != base_types.auto else self.make_default("DbtAuthstnRspn")

		@DbtAuthstnRspn.deleter
		def DbtAuthstnRspn(self):
			del self._DbtAuthstnRspn
			self._DbtAuthstnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DbtAuthstnRspn', type=DebitAuthorisationResponseV06, min=1, max=1, mutex_group=None, array=False),
		))