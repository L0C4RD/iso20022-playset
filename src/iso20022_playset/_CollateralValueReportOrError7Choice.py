# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CollateralValueReport4 import CollateralValueReport4
from ._ErrorHandling5 import ErrorHandling5

class CollateralValueReportOrError7Choice(base_types._BaseFieldType):

	__slots__ = ["_BizRpt", "_OprlErr"]
	@property
	def BizRpt(self):
		return self._BizRpt

	@BizRpt.setter
	def BizRpt(self, value):
		self._BizRpt = value if type(value) != base_types.auto else self.make_default("BizRpt")

	@BizRpt.deleter
	def BizRpt(self):
		del self._BizRpt
		self._BizRpt = None

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != base_types.auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizRpt', type=CollateralValueReport4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))