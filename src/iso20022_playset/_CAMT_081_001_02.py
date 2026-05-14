# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraBalanceMovementModificationReportV02 import IntraBalanceMovementModificationReportV02

class CAMT_081_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraBalMvmntModRpt"]
		@property
		def IntraBalMvmntModRpt(self):
			return self._IntraBalMvmntModRpt

		@IntraBalMvmntModRpt.setter
		def IntraBalMvmntModRpt(self, value):
			self._IntraBalMvmntModRpt = value if type(value) != base_types.auto else self.make_default("IntraBalMvmntModRpt")

		@IntraBalMvmntModRpt.deleter
		def IntraBalMvmntModRpt(self):
			del self._IntraBalMvmntModRpt
			self._IntraBalMvmntModRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraBalMvmntModRpt', type=IntraBalanceMovementModificationReportV02, min=1, max=1, mutex_group=None, array=False),
		))