# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import Limits8

class LimitReportOrError5Choice(base_types._BaseFieldType):

	__slots__ = ["_BizRpt", "_OprlErr"]
	@property
	def BizRpt(self):
		return self._BizRpt

	@BizRpt.setter
	def BizRpt(self, value):
		self._BizRpt = value if value is not None else base_types.UninitialisedField(self, 'BizRpt', Limits8, False)

	@BizRpt.deleter
	def BizRpt(self):
		del self._BizRpt
		self._BizRpt = base_types.UninitialisedField(self, 'BizRpt', Limits8, False)

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if value is not None else base_types.UninitialisedField(self, 'OprlErr', ErrorHandling5, True)

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = base_types.UninitialisedField(self, 'OprlErr', ErrorHandling5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizRpt', type=Limits8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))