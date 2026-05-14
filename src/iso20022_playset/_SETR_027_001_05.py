# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SecuritiesTradeConfirmationV05 import SecuritiesTradeConfirmationV05

class SETR_027_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesTradConf"]
		@property
		def SctiesTradConf(self):
			return self._SctiesTradConf

		@SctiesTradConf.setter
		def SctiesTradConf(self, value):
			self._SctiesTradConf = value if type(value) != base_types.auto else self.make_default("SctiesTradConf")

		@SctiesTradConf.deleter
		def SctiesTradConf(self):
			del self._SctiesTradConf
			self._SctiesTradConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesTradConf', type=SecuritiesTradeConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))