# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTradeConfirmationStatusAdviceV04 import SecuritiesTradeConfirmationStatusAdviceV04

class SETR_044_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTradConfStsAdvc"]
		@property
		def SctiesTradConfStsAdvc(self):
			return self._SctiesTradConfStsAdvc

		@SctiesTradConfStsAdvc.setter
		def SctiesTradConfStsAdvc(self, value):
			self._SctiesTradConfStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesTradConfStsAdvc")

		@SctiesTradConfStsAdvc.deleter
		def SctiesTradConfStsAdvc(self):
			del self._SctiesTradConfStsAdvc
			self._SctiesTradConfStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTradConfStsAdvc', type=SecuritiesTradeConfirmationStatusAdviceV04, min=1, max=1, mutex_group=None, array=False),
		))