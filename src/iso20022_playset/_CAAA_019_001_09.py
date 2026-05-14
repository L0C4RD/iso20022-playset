# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcceptorCurrencyConversionAdviceResponseV09 import AcceptorCurrencyConversionAdviceResponseV09

class CAAA_019_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCcyConvsAdvcRspn"]
		@property
		def AccptrCcyConvsAdvcRspn(self):
			return self._AccptrCcyConvsAdvcRspn

		@AccptrCcyConvsAdvcRspn.setter
		def AccptrCcyConvsAdvcRspn(self, value):
			self._AccptrCcyConvsAdvcRspn = value if type(value) != base_types.auto else self.make_default("AccptrCcyConvsAdvcRspn")

		@AccptrCcyConvsAdvcRspn.deleter
		def AccptrCcyConvsAdvcRspn(self):
			del self._AccptrCcyConvsAdvcRspn
			self._AccptrCcyConvsAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCcyConvsAdvcRspn', type=AcceptorCurrencyConversionAdviceResponseV09, min=1, max=1, mutex_group=None, array=False),
		))