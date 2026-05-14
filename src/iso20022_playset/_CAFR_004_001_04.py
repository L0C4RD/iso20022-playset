# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FraudDispositionResponseV04 import FraudDispositionResponseV04

class CAFR_004_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FrdDspstnRspn"]
		@property
		def FrdDspstnRspn(self):
			return self._FrdDspstnRspn

		@FrdDspstnRspn.setter
		def FrdDspstnRspn(self, value):
			self._FrdDspstnRspn = value if type(value) != base_types.auto else self.make_default("FrdDspstnRspn")

		@FrdDspstnRspn.deleter
		def FrdDspstnRspn(self):
			del self._FrdDspstnRspn
			self._FrdDspstnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FrdDspstnRspn', type=FraudDispositionResponseV04, min=1, max=1, mutex_group=None, array=False),
		))