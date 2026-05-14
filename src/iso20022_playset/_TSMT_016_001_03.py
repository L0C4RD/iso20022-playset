# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ErrorReportV03 import ErrorReportV03

class TSMT_016_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ErrRpt"]
		@property
		def ErrRpt(self):
			return self._ErrRpt

		@ErrRpt.setter
		def ErrRpt(self, value):
			self._ErrRpt = value if type(value) != base_types.auto else self.make_default("ErrRpt")

		@ErrRpt.deleter
		def ErrRpt(self):
			del self._ErrRpt
			self._ErrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ErrRpt', type=ErrorReportV03, min=1, max=1, mutex_group=None, array=False),
		))