# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionMovementConfirmationV16 import CorporateActionMovementConfirmationV16

class SEEV_036_001_16():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CorpActnMvmntConf"]
		@property
		def CorpActnMvmntConf(self):
			return self._CorpActnMvmntConf

		@CorpActnMvmntConf.setter
		def CorpActnMvmntConf(self, value):
			self._CorpActnMvmntConf = value if type(value) != base_types.auto else self.make_default("CorpActnMvmntConf")

		@CorpActnMvmntConf.deleter
		def CorpActnMvmntConf(self):
			del self._CorpActnMvmntConf
			self._CorpActnMvmntConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnMvmntConf', type=CorporateActionMovementConfirmationV16, min=1, max=1, mutex_group=None, array=False),
		))