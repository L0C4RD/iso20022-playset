# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DebitAuthorisationRequestV10 import DebitAuthorisationRequestV10

class CAMT_037_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DbtAuthstnReq"]
		@property
		def DbtAuthstnReq(self):
			return self._DbtAuthstnReq

		@DbtAuthstnReq.setter
		def DbtAuthstnReq(self, value):
			self._DbtAuthstnReq = value if type(value) != base_types.auto else self.make_default("DbtAuthstnReq")

		@DbtAuthstnReq.deleter
		def DbtAuthstnReq(self):
			del self._DbtAuthstnReq
			self._DbtAuthstnReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DbtAuthstnReq', type=DebitAuthorisationRequestV10, min=1, max=1, mutex_group=None, array=False),
		))