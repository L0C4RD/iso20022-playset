# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralValueReport4
from . import ErrorHandling5

class CollateralValueReportOrError7Choice(base_types._BaseFieldType):

	__slots__ = ["_BizRpt", "_OprlErr"]
	@property
	def BizRpt(self):
		return self._BizRpt

	@BizRpt.setter
	def BizRpt(self, value):
		self._BizRpt = value if value is not None else base_types.UninitialisedField(self, 'BizRpt', CollateralValueReport4, True)

	@BizRpt.deleter
	def BizRpt(self):
		del self._BizRpt
		self._BizRpt = base_types.UninitialisedField(self, 'BizRpt', CollateralValueReport4, True)

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
		base_types.FieldEntry(name='BizRpt', type=CollateralValueReport4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))