# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._StatusReportV14 import StatusReportV14

class CATM_001_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_StsRpt"]
		@property
		def StsRpt(self):
			return self._StsRpt

		@StsRpt.setter
		def StsRpt(self, value):
			self._StsRpt = value if type(value) != base_types.auto else self.make_default("StsRpt")

		@StsRpt.deleter
		def StsRpt(self):
			del self._StsRpt
			self._StsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsRpt', type=StatusReportV14, min=1, max=1, mutex_group=None, array=False),
		))