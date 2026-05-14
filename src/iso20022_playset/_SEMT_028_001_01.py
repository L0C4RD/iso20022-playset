# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._IntraPositionMovementQueryV01 import IntraPositionMovementQueryV01

class SEMT_028_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraPosMvmntQry"]
		@property
		def IntraPosMvmntQry(self):
			return self._IntraPosMvmntQry

		@IntraPosMvmntQry.setter
		def IntraPosMvmntQry(self, value):
			self._IntraPosMvmntQry = value if type(value) != base_types.auto else self.make_default("IntraPosMvmntQry")

		@IntraPosMvmntQry.deleter
		def IntraPosMvmntQry(self):
			del self._IntraPosMvmntQry
			self._IntraPosMvmntQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntQry', type=IntraPositionMovementQueryV01, min=1, max=1, mutex_group=None, array=False),
		))